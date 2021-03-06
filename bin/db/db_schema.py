#Copyright (C) 2014 Andrey Shprengel <andrey.shprengel@colorado.edu> Daniel Morrissey <daniel.morrissey@colorado.edu>
#This work is free. You can redistribute it and/or modify it under the
#terms of the Do What The Fuck You Want To Public License, Version 2,
#as published by Sam Hocevar. See the COPYING file for more details.
""" This file contains the schema for the database

Using the flask-sqlalchemy tools, the ModuleReading class is created as a
mapping between our python interface and the underlying sqlite database.
"""
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, Column

import os, sys, time

from datetime import datetime
from bin.data.conversions import MakeTimeStamp

app = Flask(__name__)
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../db/db01.db')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.abspath(db_path)
db = SQLAlchemy(app)

class ModuleReading(db.Model):
  """ The Database Model Class

  :ivar _id: Autoincrementing Table ID
  :ivar time_stamp: Time Stamp of Creation
  :ivar light: 12 bit light reading
  :ivar temp: 12 bit temp reading
  :ivar m_id: The ID of the module to query
  """

  def __init__(self, _light, _temp, _m_id):
    """ Initialization

    :param _light: 12 bit light reading
    :type _light: int

    :param _temp: 12 bit temp reading
    :type _temp: int

    :param _m_id: The ID of the module to query
    :type _m_id: int
    """
    self.light = _light
    self.temp = _temp
    self.m_id = _m_id

    self.time_stamp = MakeTimeStamp()

  _id = Column(Integer, primary_key = True, unique = True)
  time_stamp = Column(Integer)
  light = Column(Integer)
  temp = Column(Integer)
  m_id = Column(Integer)
