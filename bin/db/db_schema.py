## @package db_schema
# This file contains the schema for the database
#
# Using the flask-sqlalchemy tools, the ModuleReading class is created as a
# mapping between our python interface and the underlying sqlite database

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column

import os, sys, time, calendar
import __main__ as main

app = Flask(__name__)
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../db/db01.db')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.abspath(db_path)
db = SQLAlchemy(app)

## ModuleReading
# The database model class.
class ModuleReading(db.Model):
  ## Autoincrementing table id
  _id = Column(Integer, primary_key = True, unique = True)

  ## Datetime of object creation
  time_stamp = Column(Integer)

  ## 12 bit integer light reading
  light = Column(Integer)

  ## 12 bit integer temperature reading
  temp = Column(Integer)

  ## ID of the module from which data was sent
  m_id = Column(Integer)

  ## ModuleReading Init
  # @param _light Integer Light Reading
  # @param _temp Integer Temperature Reading
  # @param _m_id Module ID
  def __init__(self, _light, _temp, _m_id):
    self.light = _light
    self.temp = _temp
    self.m_id = _m_id
    self.time_stamp = calendar.timegm(time.gmtime())
