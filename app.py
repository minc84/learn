from flask import Flask
from config import Configuration
import os
from flask import render_template, flash, redirect

app = Flask(__name__)
app.config.from_object(Configuration)



menu = ["Главная", "Регистрация", "Контакты"]
@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html", menu=menu)

def login():
	return render_template("login.html")


if __name__ == '__main__':
      app.run(host=os.getenv('IP', '127.0.0.1'),
            port=int(os.getenv('PORT', 4000)))