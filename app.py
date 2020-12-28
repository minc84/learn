from flask import Flask
from config import Configuration
import os
from flask import render_template, flash, redirect, url_for, request, session, abort, g, make_response
import sqlite3
from FDataBase import FDataBase
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from UserLogin import UserLogin
from forms import LoginForm, RegisterForm
from admin.admin import admin


app = Flask(__name__)
app.config.from_object(Configuration)
app.config.update(dict(DATABASE=os.path.join(app.root_path,'flsite.db')))
app.register_blueprint(admin, url_prefix='/admin')
login_manager = LoginManager(app)

login_manager.login_view = 'login'
login_manager.login_message = 'АВТОРИЗУЙТЕСЬ!!!!'
login_manager.login_message_category = "success"

@login_manager.user_loader
def load_user(user_id):
	print("load_user")
	return UserLogin().fromDB(user_id, dbase())

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

def dbase():
	db = get_db()
	dbase = FDataBase(db)
	return dbase




menu = [{'name': 'Главная', 'url': '/'},
		{'name': 'Логин', 'url': 'login'},
		{'name': 'Форма', 'url': 'form'}]


@app.route('/')
def index():	
	return render_template("index.html", menu=dbase().getMenu(), posts=dbase().getPostsAnons())

@app.route('/form', methods=['POST', 'GET'])

def form():
	
	
	if request.method == 'POST':
		if len(request.form['username']) > 2:
			flash('сообщение отправлена', category='succes')
		else:
			flash('Ошибка', category='error')

	return render_template("form.html", menu=dbase().getMenu())

@app.route("/profile/<username>")
def profile(username):
	if 'userLogged' not in session or session['userLogged'] != username:
		abort(401)
			
		return f"Пользователь: {username}"

#@app.route('/login')
#def login():
	# if 'userLogged' in session:
	# 	return redirect(url_for('profile', username=session['userLogged']))
	# elif request.method == 'POST' and request.form['username'] == "selfa" and request.form['psw'] == "123":
	# 	session['userLogged'] = request.form['username']
	# 	return redirect(url_for('profile', username=session['userLogged']))
	
#	return render_template("login.html", menu=dbase().getMenu(), title='Авторизация')

@app.route("/register", methods=["POST", "GET"])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
			hash = generate_password_hash(request.form['psw'])
			res = dbase().addUser(form.name.data, form.email.data, hash)
			if res:
				flash("Вы успешно зарегистрированы", "success")
				return redirect(url_for('login'))
			else:
				flash("Ошибка при добавлении в БД", "error")
 
	return render_template("register.html", menu=dbase().getMenu(), title="Регистрация", form=form)

@app.route("/login", methods=["POST", "GET"])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('profil'))

	form = LoginForm()
	if form.validate_on_submit():
		user = dbase().getUserByEmail(form.email.data)
		if user and check_password_hash(user['psw'], form.psw.data):
			userlogin = UserLogin().create(user)
			rm = form.remember.data
			login_user(userlogin, remember=rm)
			return redirect(request.args.get("next") or url_for("profil"))
 
		flash("Неверная пара логин/пароль", "error")
 
	return render_template("login.html", menu=dbase().getMenu(), title="Авторизация", form=form)
	

	# if request.method == "POST":
	# 	user = dbase().getUserByEmail(request.form['email'])

	# 	if user and check_password_hash(user['psw'], request.form['psw']):
	# 		userlogin = UserLogin().create(user)
	# 		rm = True if request.form.get('remainme') else False
	# 		login_user(userlogin, remember=rm)
	# 		return redirect(url_for('profil'))
 
	# 	flash("Неверная пара логин/пароль", "error")
 
	# return render_template("login.html", menu=dbase().getMenu(), title="Авторизация")


@app.route('/logout')
@login_required
def logout():
	logout_user()
	flash("Вы вышли из аккаунта", "success")
	return redirect(url_for('login'))


@app.route('/profil')
@login_required
def profil():
	return render_template("profile.html", menu=dbase().getMenu(), title="Профиль")






@app.route('/add_post', methods=['POST', 'GET'])
@login_required
def addPost():
	
	if request.method == "POST":

		if len(request.form['name']) > 4 and len(request.form['post']) > 10:
			res = dbase().addPost(request.form['name'], request.form['post'], request.form['url'])
			if not res:
				flash("Ошибка добавления статьи!!!", category='error')				
			else:
				
				flash("статья добавлена успешно", category='success')				
		else:
			flash("Ошибка добавления статьи", category='error')	

	return render_template('add_post.html', menu=dbase().getMenu(), title='Добавление статьи')



@app.route('/userava')
@login_required
def userava():
	img = current_user.getAvatar(app)
	if not img:
		return ""
 
	h = make_response(img)
	h.headers['Content-Type'] = 'image/png'
	return h


@app.route('/<alias>')
def showPost(alias):
	title, post = dbase().getPost(alias)
	if not title:
		abort(404)
	return render_template('post.html', menu=dbase().getMenu(), title=title, post=post)


@app.route('/upload', methods=["POST", "GET"])
@login_required
def upload():
	if request.method == 'POST':
		file = request.files['file']
		if file and current_user.verifyExt(file.filename):
			try:
				img = file.read()
				res = dbase().updateUserAvatar(img, current_user.get_id())
				if not res:
					flash("Ошибка обновления аватара", "error")

				flash("Аватар обновлен", "success")
			except FileNotFoundError as e:
				flash("Ошибка чтения файла", "error")
		else:
			flash("Необходим PNG файл", "error")
 
	return redirect(url_for('profil'))


@app.errorhandler(404)

def pageNotFount(error):
 	return render_template('page404.html', menu=dbase().getMenu()), 404

if __name__ == '__main__':
      app.run(host=os.getenv('IP', '127.0.0.1'),
            port=int(os.getenv('PORT', 4000)))


