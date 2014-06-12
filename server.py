## @package server
# The main server program. Acts as an interaction point for posting and getting
# and displaying data from the database.

from flask import Flask, render_template, request, url_for
from bin.db.db_schema import *
from bin.db.db_actions import *
from bin.data.graphs import *
import json

from pprint import pprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'db/db01.db'
db = SQLAlchemy(app)

@app.route('/')
def home():
  return render_template('html/base.html')

@app.route('/post_reading', methods=['POST'])
def post_reading():
  if request.method == 'POST':
    data = json.loads(request.data)

    if 'light' in data and 'temp' in data and 'm_id' in data:
      light = data['light']
      temp = data['temp']
      m_id = data['m_id']
    else:
      print('INVALID DATA!')
      return None

    new_reading = ModuleReading(light, temp, m_id)
    AddReading(new_reading)

  return ''

@app.route('/get_data', methods=['GET'])
def get_data():
  data = DictionaryForModules()
  return json.dumps(data)

@app.route('/scripts/plot_dict')
def get_plotDict_script():
  v = url_for('static', filename='js/plotDict.js')
  print('file: ' + str(v))
  return v

if __name__ == '__main__':
  
  print('Initialized: Waiting for Connections!')
  app.run(debug=True)
