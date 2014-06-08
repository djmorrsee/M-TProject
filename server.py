from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('base.html')

@app.route('/echo/', methods=['POST'])
def echo():
	if request.method == 'POST':
		print(request.data)
	return ''

if __name__ == '__main__':
	app.run(debug=True)
