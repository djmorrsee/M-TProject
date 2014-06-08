from flask import Flask, render_template, request
import json

app = Flask(__name__)
name = "None"
temp = "None"
@app.route('/')
def home():
    return render_template('base.html', temp = temp)

@app.route('/dj_echo/', methods=['POST'])
def dj_echo():
	if request.method == 'POST':
		print(request.data)
	return ''

@app.route('/echo/', methods = ['POST'])
def echo():
    global temp
    if request.method == 'POST':
        print temp
        temp= request.json['temp']
        return "succes"

if __name__ == '__main__':
    app.run(debug=True)
