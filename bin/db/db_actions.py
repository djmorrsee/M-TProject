""" Database Actor

This file contains code for interacting with our database. The actions are
abstracted into a DBActor class. The DBActor should be the only way the db
is interacted with after creation.

Database creation may eventually be done inside of the DBActor init method
in order to fully abstract away user interaction with a database.

Status Codes will eventually be abstracted into a SC class for better readability.

"""
import time, calendar
from bin.db.db_schema import ModuleReading
from bin.util.authorization import HashModuleID

def ReadingsToHistoryJSON(m_id, readings):
  """ Helper method to build properly formated (?) JSON

  Should probably be in graphs.py
  """
  m_data = {} # Should Match Module_History_Reading.JSON
  m_data.update({'module_id':m_id})
  m_data.update({'reading_count':len(readings) or None})
  light = []
  temp = []
  for r in readings:
    light.append(r.light)
    temp.append(r.temp)
  m_data.update({'temperature':temp})
  m_data.update({'light':light})
  return m_data

class DBActor:
  """ Database Actor Class
  An instance of this class should be used for all database interactions
  """
  def __init__(self, database):
    self.db = database
    self.module_ids = self.GetModuleIDs()

  def ResetTable(self):
    """ Resets the datbase
    Returns:
      int. Status Code::
        701 -- Success
    """
    self.db.drop_all()
    self.db.create_all()
    return 701

  def RegisterID(self, m_id):
    """ Registers a module with the database
    Args:
      m_id (int): The ID To Register with the system
    Returns:
      int. Option::
        705 -- Failure Code, Module ID already registered. Should be exception (?)
        hashed_id -- A Unique (to m_id) hash id meant for pcDuino consumption
          This ID is required for module with m_id to add readings
    """
    if m_id in self.module_ids:
      return 705

    self.module_ids.append(str(m_id))
    return HashModuleID(m_id)

  def RemoveID(self, m_id):
    """ Removes a Module and all its data from the database
    Args:
      m_id (int): The ID To Unregister with the system
    Returns:
      int. Status Code::
        701 -- Success
        705 -- Failure Code, No module by ID in system. Should be exception (?)
    """
    m_id in self.module_ids
    if not m_id in self.module_ids:
      return 705

    for r in self.GetReadingsForModule(m_id):
      self.db.session.delete(r)

    self.db.session.commit()
    self.module_ids.remove(m_id)
    return 701

  def AddReading(self, data):
    """ Adds a module reading to the database
    Args:
      data (dict): Properly formatted (see the JSON data formats) reading dictionary
    Returns:
      int. Status Code::
        701 -- Success
        705 -- Failure Code, No module by ID in system. Should be exception (?)
        706 -- Failur Code, Bad authorization ID for module
    """

    m_id = data["module_id"]
    if not str(m_id) in self.module_ids:
      return 705

    module_auth_id = data["module_auth_id"]
    ## Check The Authorization ID ##

    if str(module_auth_id) != str(HashModuleID(m_id)):
      return 706

    temp = data["reading"]["temperature"]
    light = data["reading"]["light"]

    reading = ModuleReading(light, temp, m_id)

    self.db.session.add(reading)
    self.db.session.commit()
    return 701

  def DropOldData(self, hours):
    """ Drops data older than hours from the database

    Used as a trimming device for space saving.

    Args:
      hours (float): The age in hours for which data should be dumped

    Returns:
      int. Status Code::
        702 -- Success
    """
    time_stamp = calendar.timegm(time.gmtime())
    age = (60 * 60 * hours)

    old_time_stamp = time_stamp - age
    old_readings = ModuleReading.query.filter(ModuleReading.time_stamp < old_time_stamp).all()

    for r in old_readings:
      self.db.session.delete(r)

    self.db.session.commit()
    return 702

  def GetModuleIDs(self):
    """ Get a list of registered modules

    Returns:
      list. An array of all registered modules (an empty array if thats the case)
    """
    rs = self.db.session.query(ModuleReading.m_id.distinct()).all()
    ids = sorted(r[0] for r in rs)
    return ids

  def GetReadingsForModule(self, m_id, count = 0):
    """ Get a list of all (or count) readings for module m_id
    Args:
      m_id (int): The ID of the module to query
    Kwargs:
      count (int): The number of results to return. Default of 0 means all
    Returns:
      list. A list of readings for module m_id
      int. Error Code 705 - No Module By ID

    """
    if not m_id in self.module_ids:
      return 705

    rs = ModuleReading.query.filter(ModuleReading.m_id==m_id).order_by(ModuleReading.time_stamp.desc()).all()

    if count > 0:
      return rs[:count]
    else:
      return rs

  def GetAllData(self):
    """ Get a list of all module data
    Returns:
      list. A list of readings for each module in the database
    """
    modules = []
    for i in self.GetModuleIDs():
      readings = self.GetReadingsForModule(i)
      modules.append(ReadingsToHistoryJSON(i, readings))
    return modules
