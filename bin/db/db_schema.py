from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os, sys
import __main__ as main

app = Flask(__name__)
db_path = os.path.join(os.path.dirname(os.path.abspath(main.__file__)), 'db/db01.db')
print(db_path)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + db_path

db = SQLAlchemy(app)

class ModuleReading(db.Model):
  _id = db.Column(db.Integer, primary_key = True, unique = True)
  time_stamp = db.Column(db.Time)

  light = db.Column(db.Integer)
  temp = db.Column(db.Integer)

  m_id = db.Column(db.Integer)

  def __init__(self, _light, _temp, _m_id):
    self.light = _light
    self.temp = _temp
    self._m_id = _m_id

def ResetTable():
  db.drop_all()
  db.create_all()

def AddDummyReading():
  r = ModuleReading(100, 100, 1)
  db.session.add(r)
  db.session.commit()
