## @package db_schema
# This file contains the schema for the database
#
# Using the flask-sqlalchemy tools, the ModuleReading class is created as a
# mapping between our python interface and the underlying sqlite database

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os, sys, time, calendar
import __main__ as main

app = Flask(__name__)
#db_path = os.path.join(os.path.dirname(os.path.abspath(main.__file__)), 'db/db01.db')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

db = SQLAlchemy(app)

## ModuleReading
# The database model class.
class ModuleReading(db.Model):
  ## Autoincrementing table id
  _id = db.Column(db.Integer, primary_key = True, unique = True)

  ## Datetime of object creation
  time_stamp = db.Column(db.Integer)

  ## 12 bit integer light reading
  light = db.Column(db.Integer)

  ## 12 bit integer temperature reading
  temp = db.Column(db.Integer)

  ## ID of the module from which data was sent
  m_id = db.Column(db.Integer)

  ## ModuleReading Init
  # @param _light Integer Light Reading
  # @param _temp Integer Temperature Reading
  # @param _m_id Module ID
  def __init__(self, _light, _temp, _m_id):
    self.light = _light
    self.temp = _temp
    self.m_id = _m_id
    self.time_stamp = calendar.timegm(time.gmtime())
