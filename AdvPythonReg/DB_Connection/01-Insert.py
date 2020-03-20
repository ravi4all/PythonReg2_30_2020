import pymysql

connection = pymysql.connect(host='localhost', user='root',
		port = 3306, database = 'movie_db',
		autocommit = True)

cur = connection.cursor()
id = 4
name = 'Aman'
m_id = 101

# query = "insert into users values (3,'ramesh',103)"

query = "insert into users values ({}, '{}', {})".format(id,name,m_id)
cur.execute(query)

connection.close()