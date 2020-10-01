import sqlite3 as sq

with sq.connect("saper.db") as con:
	cur = con.cursor()

	cur.execute(" select * from users where old > 20 AND score < 40 ORDER BY old DESC LIMIT 1")
	res = cur.fetchall()

	for value in cur.execute(" select name, score from users WHERE name LIKE 'ВАСИЛИСА'"):
		print(value)

	cur.execute("select name, score from users WHERE name LIKE 'ВАСИЛИСА' AND score > 1100")
	res = cur.fetchone()
	print(res)


