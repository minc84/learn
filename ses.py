from flask import Flask, render_template, make_response, url_for, request, session
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = '1e02c98cfc6c0185781ab26d9d4343dbdbe97dda'

@app.route("/")
def index():
	if 'visits' in session:
		session['visits'] = session.get('visits') + 1
	else:
		session['visits'] = 1
	return f"Число просмотров: {session['visits']}"

if __name__ == '__main__':
	app.run(host=os.getenv('IP', '127.0.0.1'),
            port=int(os.getenv('PORT', 7000)))