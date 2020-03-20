import pymysql

connection = pymysql.connect(host='localhost', user='root',
		port = 3306, database = 'movie_db',
		autocommit = True)

cur = connection.cursor()

query = "select * from users"
cur.execute(query)
data = cur.fetchall()
print(data)

connection.close()