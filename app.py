from flask import Flask
from config import Configuration
import os
from flask import render_template, flash, redirect, url_for, request

app = Flask(__name__)
app.config.from_object(Configuration)



menu = [{'name': 'Главная', 'url': '/'},
		{'name': 'Логин', 'url': 'login'},
		{'name': 'Форма', 'url': 'form'}]

@app.route('/')
def index():
	print(url_for('index'))
	return render_template("index.html", menu=menu)

@app.route('/login')
def login1():
	print(url_for('login1'))
	return render_template("login.html", menu=menu)

@app.route('/form', methods=['POST', 'GET'])

def form():
	
	if request.method == 'POST':
		if len(request.form['username']) > 2:
			flash('сообщение отправлена', category='succes')
		else:
			flash('Ошибка', category='error')

	return render_template("form.html", menu=menu)

@app.route("/profile/<int:username>/<path>")
def profile(username, path):
    return f"Пользователь: {username},{path}"

@app.errorhandler(404)

def pageNotFount(error):
 	return render_template('page404.html', menu=menu)

if __name__ == '__main__':
      app.run(host=os.getenv('IP', '127.0.0.1'),
            port=int(os.getenv('PORT', 4000)))
      