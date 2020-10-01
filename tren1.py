import sqlite3 as sq

with sq.connect('customer.db') as con:
	cur = con.cursor()
	cur.execute("INSERT INTO customers(first_name,last_name,email) VALUES('Nikolay','Nesterovich','2nc@mail.ru')")








"""
	

	base= cur.execute("CREATE TABLE customers(id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT,last_name TEXT, email TEXT)")
	if base:
		print("Create base")
	else:
		print("not db")
"""