from db_schema import *

def ResetTable():
  db.drop_all()
  db.create_all()

def AddReading(reading):
  db.session.add(reading)
  db.session.commit()

def AddManyReadings(readings):
  for r in readings:
    db.session.add(r)

  db.session.commit()

def AddDummyReading():
  r = ModuleReading(100, 100, 1)
  AddReading(r)

def GetMostRecentReading ():
  r = ModuleReading.query.order_by(ModuleReading._id.desc()).first()
  return r

def GetReadings(count=0):
  if count != 0:
    rs = ModuleReading.query.order_by(ModuleReading._id.desc()).all()[:count]
  else:
    rs = ModuleReading.query.order_by(ModuleReading._id.desc()).all()
  return rs
