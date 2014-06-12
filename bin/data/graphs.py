## @package graphs
# This file contains functions for grouping data for display in the jqplots library.

from bin.data.conversions import *
from bin.db.db_actions import *

import json

def DictionaryForModules ():
  ms_dict = {}
  for _id in GetModuleIDs():
    label = 'module_' + str(_id)
    module_dict = DictionaryFromReadings(GetReadings(_id))
    ms_dict.update({label:module_dict})

  return ms_dict

def DictionaryFromReadings (readings):
  m_dict = {}
  time = []
  temp = []
  light = []
  for r in readings:
    time.append(r.time_stamp)
    temp.append(IntToTemp(r.temp))
    light.append(r.light)

  m_dict.update({'light':LineDictFromArrays(time, light)})
  m_dict.update({'temp':LineDictFromArrays(time, temp)})

  return m_dict

def LineDictFromArrays(xs, ys):
  d = {}
  assert(len(xs) == len(ys))

  d.update({'xs': xs})
  d.update({'ys': ys})
  return d
