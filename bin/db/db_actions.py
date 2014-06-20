## @package db_actions
# This file contains a series of database wrapper functions
import time, calendar
from bin.db.db_schema import ModuleReading

def ReadingsToHistoryJSON(m_id, readings):
  m_data = {} # Should Match Module_History_Reading.JSON
  m_data.update({'module_id':m_id})
  m_data.update({'reading_count':len(readings)})
  light = []
  temp = []
  for r in readings:
    light.append(r.light)
    temp.append(r.temp)
  m_data.update({'temperature':temp})
  m_data.update({'light':light})
  return m_data

class DBActor:
  def __init__(self, database):
    self.db = database
    self.module_ids = self.GetModuleIDs()

  def ResetTable(self):
    self.db.drop_all()
    self.db.create_all()
    return 701

  def RegisterID(self, m_id):
    if m_id in self.module_ids:
      return 705
    self.module_ids.append(str(m_id))
    return 701

  def RemoveID(self, m_id):
    m_id in self.module_ids
    if not m_id in self.module_ids:
      return 705

    for r in self.GetReadingsForModule(m_id):
      self.db.session.delete(r)

    self.db.session.commit()
    self.module_ids.remove(m_id)
    return 701

  def AddReading(self, data):
    m_id = data["module_id"]
    if not m_id in self.module_ids:
      return 705

    module_auth_id = data["module_auth_id"]
    ## Check The Authorization ID ##

    temp = data["reading"]["temperature"]
    light = data["reading"]["light"]

    reading = ModuleReading(light, temp, m_id)

    self.db.session.add(reading)
    self.db.session.commit()
    return 701

  def DropOldData(self, hours):
    time_stamp = calendar.timegm(time.gmtime())
    age = (60 * 60 * hours)

    old_time_stamp = time_stamp - age
    old_readings = ModuleReading.query.filter(ModuleReading.time_stamp < old_time_stamp).all()

    for r in old_readings:
      self.db.session.delete(r)

    self.db.session.commit()
    return 702

  def GetModuleIDs(self):
    rs = self.db.session.query(ModuleReading.m_id.distinct()).all()
    ids = sorted(r[0] for r in rs)
    return ids

  def GetReadingsForModule(self, m_id, count = 0):
    if not m_id in self.module_ids:
      return None

    rs = ModuleReading.query.filter(ModuleReading.m_id==m_id).order_by(ModuleReading.time_stamp.desc()).all()

    if count > 0:
      return rs[:count]
    else:
      return rs

  def GetAllData(self):
    modules = []
    for i in self.GetModuleIDs():
      readings = self.GetReadingsForModule(i)
      modules.append(ReadingsToHistoryJSON(i, readings))
    return modules
