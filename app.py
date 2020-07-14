from flask import Flask
from config import Configuration
import os
from flask import render_template, flash, redirect, url_for

app = Flask(__name__)
app.config.from_object(Configuration)



menu = ["Главная", "Регистрация", "Контакты"]
@app.route('/')
def index():
	print(url_for('index'))
	return render_template("index.html", menu=menu)

@app.route('/login')
def login1():
	print(url_for('login1'))
	return render_template("login.html", menu=menu)

@app.route("/profile/<int:username>/<path>")
def profile(username, path):
    return f"Пользователь: {username},{path}"

if __name__ == '__main__':
      app.run(host=os.getenv('IP', '127.0.0.1'),
            port=int(os.getenv('PORT', 4000)))