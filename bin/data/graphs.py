""" Graph Data Builder
This file contains functions for grouping data for display in the JQPlot library
"""

from bin.data.conversions import *
from bin.db.db_actions import *

import json

## Subject to rewrite to conform to specified JSON formats
class GraphError(Exception):
  """ Exception Class for Graph Data Errors """
  def __init__(self, msg):
    super(GraphError, self).__init__(msg)
