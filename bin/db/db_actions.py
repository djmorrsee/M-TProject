from db_schema import db, ModuleReading

def AddReading(reading):
  db.session.add(reading)
  db.session.commit()

def AddManyReadings(readings):
  for r in readings:
    db.session.add(r)

  db.session.commit()
