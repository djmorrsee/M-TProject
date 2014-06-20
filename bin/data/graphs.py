## @package graphs
# This file contains functions for grouping data for display in the jqplots library.

from bin.data.conversions import *
from bin.db.db_actions import *

import json

## Subject to rewrite to conform to specified JSON formats

class GraphError(Exception):
  def __init__(self, msg):
    super(GraphError, self).__init__(msg)


def DictionaryForModules (db_actor):
  ms_dict = {}
  for _id in db_actor.GetModuleIDs():
    label = str(_id)
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
    light.append(IntToLight(r.light))

  m_dict.update({'light':LineDictFromArrays(time, light)})
  m_dict.update({'temp':LineDictFromArrays(time, temp)})

  return m_dict

def LineDictFromArrays(xs, ys):
  d = {}
  assert(len(xs) == len(ys))

  d.update({'xs': xs})
  d.update({'ys': ys})
  return d
