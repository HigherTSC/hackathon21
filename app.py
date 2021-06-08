from flask import Flask, render_template, Response
import time

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/progress1')
def progress1():
	def generate():
		x = 0

		#for x in range(0,100):
		while x < 101:
			yield "data:" + str(x) + "\n\n"
			x = x + (4.35)
			time.sleep(0.5)

	return Response(generate(), mimetype= 'text/event-stream')

@app.route('/progress2')
def progress2():
	def generate():
		x = 0

		#for x in range(0,100):
		while x < 1000:
			yield "data:" + str(x) + "\n\n"
			x = x + (5.24)
			time.sleep(0.5)

	return Response(generate(), mimetype= 'text/event-stream')

if __name__ == "__main__":
	app.run() 