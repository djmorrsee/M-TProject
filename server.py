from flask import Flask, render_template, request
from bin.db.db_schema import *
from bin.db.db_actions import *
import json

from pprint import pprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'db/db01.db'
db = SQLAlchemy(app)

@app.route('/')
def home():
  r = GetReadings()
  return render_template('base.html', temp = ModuleReading.query.count())

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

if __name__ == '__main__':
  app.run(debug=True)
