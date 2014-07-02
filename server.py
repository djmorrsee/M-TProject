#Copyright (C) 2014 Andrey Shprengel <andrey.shprengel@colorado.edu> Daniel Morrissey <daniel.morrissey@colorado.edu>
#This work is free. You can redistribute it and/or modify it under the
#terms of the Do What The Fuck You Want To Public License, Version 2,
#as published by Sam Hocevar. See the COPYING file for more details.
""" Server

The main server program. Acts as an interaction point for posting and getting
and displaying data from the database.
"""
from flask import Flask, render_template, request, url_for, jsonify
from jinja2 import FileSystemLoader
from bin.db.db_schema import *
from bin.db.db_actions import *
from bin.util.authorization import *
from bin.util.status_codes import SC
import json

db_actor = DBActor(db)

app = Flask(__name__)

@app.route('/')
def home():
  """ Project Home Page

  Defines the route for displaying the module data in a webpage.
  """
  return render_template('base.html')

@app.route('/all/', methods=['GET'])
def get_all_data():
  """ Dump Database Data

  """
  return json.dumps(db_actor.GetAllData())

@app.route('/module/', methods=['GET'])
def get_module_list():
  return json.dumps(db_actor.module_ids)

@app.route('/module/<m_id>/', methods=['GET', 'POST', 'DELETE'])
def handle_module_request(m_id):
  """ Module Admin Route

  """
  r_method = request.method
  m_id = int(m_id)

  if r_method == 'GET':
    readings = db_actor.GetReadingsForModule(m_id)
    if readings == None:
      return SC.BadMID()

    j_data = ReadingsToHistoryJSON(m_id, readings)
    return json.dumps(j_data)

  else:
    data = request.json
    VerifyAuthData(data)

    if r_method == 'POST':
      return json.dumps(db_actor.RegisterID(m_id))
    elif r_method == 'DELETE':
      return json.dumps(db_actor.RemoveID(m_id))
    else:
      return SC.Fauilure()

@app.route('/module/post_reading/', methods=['POST'])
def post_data():
  """ Module Data Posting Route

  """
  data = request.json
  return json.dumps(db_actor.AddReading(data))

@app.route('/reset/', methods=['DELETE'])
def reset_data():
  """ Table Reset Route

  """
  data = request.json
  if not VerifyAuthData(data):
    return SC.BadForm()
  if not AuthorizeAuthData(data):
    return SC.BadAuth()
  return json.dumps(db_actor.ResetTable())

@app.route('/drop/', methods=['DELETE'])
def drop_old_data():
  data = request.json
  ## Do Authrorization ##
  if not VerifyAuthData(data):
    return SC.BadForm()
  if not AuthorizeAuthData(data):
    return SC.BadAuth()

  return json.dumps(db_actor.DropOldData(24))

## Scripts Routes ##
# These routes are helper methods for loading static js files on our web page
@app.route('/scripts/plot_dict')
def get_plotDict_script():
  v = url_for('static', filename='js/plotDict.js')
  return v


## Start The Server
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
