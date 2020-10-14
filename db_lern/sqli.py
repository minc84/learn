import sqlite3 as sq

# with sq.connect("learn.db") as con:
# 		cur = con.cursor()
# 		cur.execute("""CREATE TABLE books (
# 						id_books INTEGER PRIMARY KEY AUTOINCREMENT,
# 						auth_name TEXT NOT NULL,
# 						title TEXT NOT NULL,
# 						count_page INTEGER NOT NULL,
# 						price REAL NOT NULL
# 						)""")

def add_one(auth_name, title, count_page, price):
	with sq.connect('learn.db') as con:
		cur = con.cursor()
		cur.execute("INSERT INTO books (auth_name, title, count_page, price) VALUES(?,?,?,?)",(auth_name, title, count_page, price))

def show_all():
	with sq.connect('learn.db') as con:
		cur = con.cursor()
		cur.execute("SELECT * FROM books")
		resault = cur.fetchall()
		for res in resault:
			print(res)
	
if __name__ == '__main__':
	#add = tren1.add_one('Brishtileva','Svetlana', 'brish@yandex.ru')
	
	add = add_one('Л.Н. Толстой', 'Война и мир', 820, 1320.60)
	add = add_one('М.А. Шолохов', 'Тихий дон', 1121, 675)
	watch_table = show_all()
