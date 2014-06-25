""" Graph Data Builder
This file contains functions for grouping data for display in the JQPlot library


DEPRECATED: This file is no longer needed with a common json format!
"""

import json

## Subject to rewrite to conform to specified JSON formats
class GraphError(Exception):
  """ Exception Class for Graph Data Errors """
  def __init__(self, msg):
    super(GraphError, self).__init__(msg)
