## @package server
# The main server program. Acts as an interaction point for posting and getting
# and displaying data from the database.

from flask import Flask, render_template, request, url_for, jsonify
from jinja2 import FileSystemLoader
from bin.db.db_schema import *
from bin.db.db_actions import *
from bin.data.graphs import *
import json

db_actor = DBActor(db)

app.jinja_loader = FileSystemLoader('templates')

@app.route('/')
def home():
  return render_template('base.html')

## REST Routes
@app.route('/all/', methods=['GET'])
def get_all_data():
  return jsonify(db_actor.GetAllData())

@app.route('/module/', methods=['GET'])
def get_module_list():
  return jsonify(db_actor.GetModuleIDs())

@app.route('/module/<m_id>/', methods=['GET', 'POST', 'DELETE'])
def handle_module_request(m_id):
  r_method = request.method

  if r_method == 'GET':
    return jsonify(db_actor.GetReadingsForModule(m_id))
  elif r_method == 'POST':
    data = request.data
    ## Do Authrorization ##

    return str(db_actor.RegisterID(m_id, data))
  elif r_method == 'DELETE':
    data = request.data
    ## Do Authrorization ##

    return str(db_actor.RemoveID(m_id, data))
  else:
    return str(702)

@app.route('/module/post_reading/', methods=['POST'])
def post_data():
  data = request.data
  ## Authorization Done On The Module Level ##
  return str(db_actor.AddReading(data))

@app.route('/reset/', methods=['DELETE'])
def reset_data():
  data = reqeust.data
  ## Do Authrorization ##

  return str(db_actor.ResetTable())

@app.route('/drop/', methods=['DELETE'])
def drop_old_data():
  data = request.data
  ## Do Authrorization ##

  return str(db_actor.DropOldData(1))


# ### Old
# @app.route('/post_reading', methods=['POST'])
# def post_reading():
#   if request.method == 'POST':
#     data = json.loads(request.data)
#
#     if 'light' in data and 'temp' in data and 'm_id' in data:
#       light = data['light']
#       temp = data['temp']
#       m_id = data['m_id']
#     else:
#       print('INVALID DATA!')
#       return None
#
#     new_reading = ModuleReading(light, temp, m_id)
#     AddReading(new_reading)
#
#   return ''

## Scripts Routes ##
# These routes are helper methods for loading static js files on our web page
@app.route('/scripts/plot_dict')
def get_plotDict_script():
  v = url_for('static', filename='js/plotDict.js')
  return v

## Start The Server
if __name__ == '__main__':
  app.run(debug=True)
