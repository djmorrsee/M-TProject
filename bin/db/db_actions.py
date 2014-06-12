## @package db_actions
# This file contains a series of database wrapper functions
import random, time
from db_schema import *

## Resets the reinitializes the db
def ResetTable():
  db.drop_all()
  db.create_all()

## Adds a ModuleReading to the database and commits
def AddReading(reading):
  db.session.add(reading)
  db.session.commit()

## Adds an array of ModuleReadings to the db and commits it
def AddManyReadings(readings):
  for r in readings:
    db.session.add(r)
  db.session.commit()

## Creates a dummy ModuleReading and calls AddReading
def AddDummyReading():
  r = ModuleReading(random.randint(0, 4096), random.randint(0,4096), random.randint(0,5))
  AddReading(r)

## Populates the database with module readings
def AddDummyPopulation(mnum=1, rnum=5):
  ResetTable()
  readings = []
  for i in range(0, mnum):
    for j in range(0, rnum):
      readings.append(ModuleReading((j + 1) ** (i + 1), i + j, i))
      time.sleep(1)
    time.sleep(5)
  AddManyReadings(readings)


## Returns a list of unique module ids in the db
def GetModuleIDs ():
  rs = db.session.query(ModuleReading.m_id.distinct()).all()
  return sorted(r[0] for r in rs)

## Returns a number of readings equal to count with Module ID:m_id
def GetReadings(m_id, count = 0):
  rs = ModuleReading.query.filter(ModuleReading.m_id==m_id).order_by(ModuleReading.time_stamp.desc()).all()

  if count > 0:
    return rs[:count]
  else:
    return rs
