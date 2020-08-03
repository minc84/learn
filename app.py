from flask import Flask
from config import Configuration
import os
from flask import render_template, flash, redirect, url_for, request, session, abort, g
import sqlite3
from FDataBase import FDataBase

app = Flask(__name__)
app.config.from_object(Configuration)
app.config.update(dict(DATABASE=os.path.join(app.root_path,'flsite.db')))

def connect_db():
	conn=sqlite3.connect(app.config['DATABASE'])
	conn.row_factory = sqlite3.Row 
	return conn

def create_db():
	db = connect_db()
	with app.open_resource('sq_db.sql', mode='r') as f:
		db.cursor().executescript(f.read())
	db.commit()
	db.close()

def get_db():
	if not hasattr(g, 'link_db'):
		g.link_db = connect_db()
	return g.link_db

@app.teardown_appcontext
def close(error):
		if hasattr(g, 'link_db'):
			g.link_db.close()



menu = [{'name': 'Главная', 'url': '/'},
		{'name': 'Логин', 'url': 'login'},
		{'name': 'Форма', 'url': 'form'}]


@app.route('/')
def index():
	db = get_db()
	dbase = FDataBase(db)
	
	return render_template("index.html", menu=dbase.getMenu())

@app.route('/form', methods=['POST', 'GET'])

def form():
	
	if request.method == 'POST':
		if len(request.form['username']) > 2:
			flash('сообщение отправлена', category='succes')
		else:
			flash('Ошибка', category='error')

	return render_template("form.html", menu=menu)

@app.route("/profile/<username>")
def profile(username):
	if 'userLogged' not in session or session['userLogged'] != username:
		abort(401)
			
		return f"Пользователь: {username}"

@app.route('/login', methods=['POST', 'GET'])
def login():
	if 'userLogged' in session:
		return redirect(url_for('profile', username=session['userLogged']))
	elif request.method == 'POST' and request.form['username'] == "selfa" and request.form['psw'] == "123":
		session['userLogged'] = request.form['username']
		return redirect(url_for('profile', username=session['userLogged']))
	
	return render_template("login.html", menu=menu)



@app.errorhandler(404)

def pageNotFount(error):
 	return render_template('page404.html', menu=menu), 404

if __name__ == '__main__':
      app.run(host=os.getenv('IP', '127.0.0.1'),
            port=int(os.getenv('PORT', 4000)))
      