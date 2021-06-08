from flask import Flask, render_template, Response
from main import GoalHandler, Goal#
import datetime, time

# Create dummy dataset
goalhandler = GoalHandler()
goalhandler.store_new_goal(
	start_date=datetime.strptime('2020-06-07', "%Y-%m-%d"),
	end_date=datetime.strptime('2020-06-30', "%Y-%m-%d"),
	name="Birthday Present",
	amount_to_save=100)
goalhandler.store_new_goal(
	start_date=datetime.strptime('2020-06-07', "%Y-%m-%d"),
	end_date=datetime.strptime('2020-12-15', "%Y-%m-%d"),
	name="New Laptop",
	amount_to_save=1000)

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