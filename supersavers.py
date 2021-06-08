from flask import Flask, redirect, url_for, render_template
import time

app = Flask(__name__)

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/savings')
def savings():
	return render_template('savings.html')

@app.route('/achievements')
def achievements():
	return render_template('achievements.html')

@app.route('/milestones')
def milestones():
	return render_template('milestones.html')

if __name__ == "__main__":
	app.run(debug=True) 