from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash 
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app) 

class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(50), unique=True)
	psw = db.Column(db.String(500), nullable=True)
	date = db.Column(db.DateTime, default=datetime.utcnow)
	
	pr = db.relationship('Profiles', backref='users', uselist=False)
	
	def __repr__(self):
		return f"<users {self.id}>"

class Profiles(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=True)
	old = db.Column(db.Integer)
	city = db.Column(db.String(100))
 
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
 
	def __repr__(self):
		return f"<profiles {self.id}>"

@app.route("/", methods=("POST", "GET"))
def ind():
	try:
		info = Users.query.all()
	except:
		print("Ошибка чтения из БД")
 
	return render_template("ind.html", title="Главная", info=info)

@app.route("/reg", methods=("POST", "GET"))
def reg():
	if request.method == "POST":
        # здесь должна быть проверка корректности введенных данных
		try:
			hash = generate_password_hash(request.form['psw'])
			u = Users(email=request.form['email'], psw=hash)
			db.session.add(u)
			db.session.flush()
 
			p = Profiles(name=request.form['name'], old=request.form['old'],
				city=request.form['city'], user_id = u.id)
			db.session.add(p)
			db.session.commit()
		except:
			db.session.rollback()
			print("Ошибка добавления в БД")
		return render_template("ind.html", title="Главная")

 
	return render_template("reg.html", title="Главная")

@app.route('/<int:id>')
def pos(id):
	pos = Users.query.get(id)
	pos1 = Profiles.query.get(id)
	print(pos)
	return render_template("pos.html", title="Главная", pos=pos, pos1=pos1)

@app.route('/<int:id>/delete')
def deleteUser(id):
	try:
		pos = Users.query.get_or_404(id)
		db.session.delete(pos)
		db.session.flush()

		pos1 = Profiles.query.get_or_404(id)
	
		db.session.delete(pos1)
		db.session.commit()
		
	except:
		db.session.rollback()
		print("Ошибка удаление БД")

	return render_template("ind.html", title="Ярослава")

@app.route('/<int:id>/update', methods=("POST", "GET"))
def updateUser(id):
	if request.method == "POST":
        # здесь должна быть проверка корректности введенных данных
		try:
			pos = Users.query.get_or_404(id)
	
			pos.email=request.form['email']
			db.session.flush()

			pos1 = Profiles.query.get_or_404(id)
 
			pos1.name=request.form['name']
			pos1.old=request.form['old']
			pos1.city=request.form['city']
			
			db.session.commit()
		except:
			db.session.rollback()
			print("Ошибка добавления в БД")

	return render_template("update.html", title="Главная", pos=pos, pos1=pos1)


if __name__ == "__main__":
	app.run(debug=True)