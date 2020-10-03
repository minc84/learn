import sqlite3 as sq

with sq.connect('customer.db') as con:
	cur = con.cursor()
	
	cur.execute("select * from customers order by first_name ASC")
	
	

	results = cur.fetchall()
	for result in results:
		print(result)







"""
	

	base= cur.execute("CREATE TABLE customers(id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT,last_name TEXT, email TEXT)")
	if base:
		print("Create base")
	else:
		print("not db")

		cur.execute("INSERT INTO customers(first_name,last_name,email) VALUES('Yraslava','Nesterovich','yara@mail.ru')")
	cur.execute("INSERT INTO customers(first_name,last_name,email) VALUES('Vasilisa','Nesterovich','vasilisa@mail.ru')")
	cur.execute("INSERT INTO customers(first_name,last_name,email) VALUES('Yliana','Nesterovich','ylay@mail.ru')")
	cur.execute("INSERT INTO customers(first_name,last_name,email) VALUES('Boris','Nesterovich','boris-britva@mail.ru')")

	many_customer = [
						('Elena','Nesterovich','lenasha@yandex.ru'),
						('Tamara','Golub','toma@mail.ru'),
						('Alexander','Golub', 'sasha@mail.ru')
	]
	cur.executemany("INSERT INTO customers(first_name,last_name,email) VALUES(?,?,?)", many_customer)

res = cur.fetchall()//всех
	print(res)
	print('-----------')
	res1 = cur.fetchmany(4) первык 4
	print(res1)
	print('-----------')

	res1 = cur.fetchone()[3] // выводит третье значение емаил
	res1 = cur.fetchall()[3] // выводи третью строку из таблицы

	results = cur.fetchall() вывод по строчно
	for result in results:
		print(result)

	results = cur.fetchall() вывод всем имен first_name [0] это id
	for result in results:
		print(result[1])

	results = cur.fetchall() выводим фамилии
	for result in results:
		print(result[1] +' ' + result[2])

		cur.execute("select * from customers where last_name like '%vich'")
		выводим всех у кого фамилия на vich заканчивается


ur.execute("update customers set first_name='Vita' where first_name = 'Vitalina' " )
	Меняем имя виталина на вита


	cur.execute("update customers set first_name='Kolya' where id = 1 " )
	меняем имя по ид

	cur.execute("delete * from customers where id = 6" )
Удаляем 6 запись

cur.execute("select * from customers order by id DESC")
	
Команда ORDER BY задает поле для сортировки записей при выборе из базы

"""
