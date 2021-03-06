#Copyright (C) 2014 Andrey Shprengel <andrey.shprengel@colorado.edu> Daniel Morrissey <daniel.morrissey@colorado.edu>
#This work is free. You can redistribute it and/or modify it under the
#terms of the Do What The Fuck You Want To Public License, Version 2,
#as published by Sam Hocevar. See the COPYING file for more details.
"""

This file contains code for interacting with our database. The actions are
abstracted into a DBActor class. The DBActor should be the only way the db
is interacted with after creation.

Database creation may eventually be done inside of the DBActor init method
in order to fully abstract away user interaction with a database.
"""
import time, calendar
from bin.db.db_schema import ModuleReading
from bin.util.authorization import HashModuleID
from bin.util.status_codes import SC
from bin.data.data import ReadingsToHistoryJSON
from bin.data.conversions import MakeTimeStamp

class DBActor:
  """ Wrapper class for interacting with the sqlalchemy db

  An instance of this class should be used for all database interactions
  """
  def __init__(self, database):
    self.db = database
    self.module_ids = self.GetModuleIDs()

  def ResetTable(self):
    """ Resets the datbase

    :returns: int -- Status Code 701 SUCCESS
    """
    self.db.drop_all()
    self.db.create_all()
    return SC.Success()


  def RegisterID(self, m_id):
    """ Registers a module with the database

    :param m_id: The ID of the module to query
    :type m_id: int

    :returns: int -- A Unique (to m_id) hash id meant for pcDuino consumption
    :returns: int -- Status Code 705 FAILURE BAD M_ID

    The Unique ID is required for module with m_id to add readings after registration.
    """
    if m_id in self.module_ids:
      return SC.BadMID()

    self.module_ids.append(m_id)
    return HashModuleID(m_id)

  def RemoveID(self, m_id):
    """ Removes a Module and all its data from the database

    :param m_id: The ID of the module to query
    :type m_id: int

    :returns: int -- Status Code 701 SUCCESS
    :returns: int -- Status Code 705 FAILURE BAD M_ID
    """
    if not m_id in self.module_ids:
      return SC.BadMID()

    for r in self.GetReadingsForModule(m_id):
      self.db.session.delete(r)

    self.db.session.commit()
    self.module_ids.remove(m_id)
    return SC.Success()

  def AddReading(self, data):
    """ Adds a module reading to the database

    :param data: Properly formatted (see the JSON data formats) reading dictionary
    :type data: JSON Formatted Dictionary

    :returns: int -- Status Code 701 SUCCESS
    :returns: int -- Status Code 705 FAILURE BAD M_ID
    :returns: int -- Status Code 706 FAIURE BAD M_AUTH_ID
    """


    m_id = data["module_id"]
    if not m_id in self.module_ids:
      return SC.BadMID()

    module_auth_id = data["module_auth_id"]
    if str(module_auth_id) != str(HashModuleID(m_id)):
      return SC.BadMAuth()

    temp = data["reading"]["temperature"]
    light = data["reading"]["light"]

    reading = ModuleReading(light, temp, m_id)

    self.db.session.add(reading)
    self.db.session.commit()
    return SC.Success()

  def DropOldData(self, hours):
    """ Drops data older than hours from the database

    :param hours: The age in hours for which data should be dumped
    :type hours: float

    :returns: int -- Status Code 702 SUCCESS

    """
    time_stamp = MakeTimeStamp()
    age = (60 * 60 * hours)

    old_time_stamp = time_stamp - age
    old_readings = ModuleReading.query.filter(ModuleReading.time_stamp < old_time_stamp).all()

    for r in old_readings:
      self.db.session.delete(r)

    print('Deleted %i entries' % len(old_readings))

    self.db.session.commit()
    return SC.Success()

  def GetModuleIDs(self):
    """ Get a list of registered modules

    :returns: list -- An array of all registered module ids
    """
    rs = self.db.session.query(ModuleReading.m_id.distinct()).all()
    ids = sorted(r[0] for r in rs)
    return ids

  def GetReadingsForModule(self, m_id, count = 0):
    """ Get a list of all (or count number of) readings for module m_id

    :param m_id: The ID of the module to query
    :type m_id: int

    :param count: The Number of readings to find. Default of 0 means all
    :type count: int

    :returns: list -- A list of readings or None

    """
    if not m_id in self.module_ids:
      return None

    rs = ModuleReading.query.filter(ModuleReading.m_id==m_id).order_by(ModuleReading.time_stamp.desc()).all()

    if count > 0:
      return rs[:count]
    else:
      return rs

  def GetAllData(self):
    """ Get a list of all module data

    :returns: list -- A list of readings for each module in the database
    """
    modules = []
    for i in self.GetModuleIDs():
      readings = self.GetReadingsForModule(i)
      modules.append(ReadingsToHistoryJSON(i, readings))
    return modules
