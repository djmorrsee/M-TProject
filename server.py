## @package server
# The main server program. Acts as an interaction point for posting and getting
# and displaying data from the database.

from flask import Flask, render_template, request, url_for, jsonify
from jinja2 import FileSystemLoader
from bin.db.db_schema import *
from bin.db.db_actions import *
from bin.data.graphs import *
from bin.util.status_codes import *
import json

db_actor = DBActor(db)

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('base.html')

## REST Routes
@app.route('/all/', methods=['GET'])
def get_all_data():
  return json.dumps(db_actor.GetAllData())

@app.route('/module/', methods=['GET'])
def get_module_list():
  return str(db_actor.module_ids)

@app.route('/module/<m_id>/', methods=['GET', 'POST', 'DELETE'])
def handle_module_request(m_id):
  r_method = request.method

  if r_method == 'GET':
    readings = db_actor.GetReadingsForModule(m_id)
    if readings == None:
      return GetCode(705)
    j_data = ReadingsToHistoryJSON(m_id, readings)
    return str(j_data)

  else:
    data = request.data
    ## Do Authrorization ##
    if r_method == 'POST':
      return str(db_actor.RegisterID(m_id))
    elif r_method == 'DELETE':
      return str(db_actor.RemoveID(m_id))
    else:
      return GetCode(702)

@app.route('/module/post_reading/', methods=['POST'])
def post_data():
  data = request.json
  ## Authorization Done On The Module Level ##
  return str(db_actor.AddReading(data))

@app.route('/reset/', methods=['DELETE'])
def reset_data():
  data = reqeust.data
  ## Do Authrorization ##
  if not VerifyAuthData(data):
    return str(703)
  if not AuthorizeAuthData(data):
    return str(704)
  return str(db_actor.ResetTable())

@app.route('/drop/', methods=['DELETE'])
def drop_old_data():
  data = request.data
  ## Do Authrorization ##

  return str(db_actor.DropOldData(1))

## Scripts Routes ##
# These routes are helper methods for loading static js files on our web page
@app.route('/scripts/plot_dict')
def get_plotDict_script():
  v = url_for('static', filename='js/plotDict.js')
  return v


## Start The Server
if __name__ == '__main__':
  app.run(debug=True)
