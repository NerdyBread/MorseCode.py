from app import app

from flask import flash, render_template

@app.route('/home')
def home():
	return render_template('home.html')