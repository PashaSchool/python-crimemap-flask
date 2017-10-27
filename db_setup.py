import pymysql
import dbconfig

connection = pymysql.connect(
	host="localhost",
	user=dbconfig.db_user,
	password=dbconfig.db_password)

try:
	with connection.cursor as cursor:
		sql = "CREATE DATABASE IF NOT EXIST crimemap"
		cursor.execute(sql)
		sql = """
			CREATE TABLE IF NOT EXIST crimemap.crimes(
				id int NOT NULL AUTO_INCREMENT,
				latitude FLOAT(10, 6),
				longitude FLOAT(10, 6),
				date DATETIME,
				category VARCHAR(50),
				description VARCHAR(1000),
				PRIMARY KEY (id)
			)
		"""
		cursor.execute(sql);
		connection.commit()
finally:
	connection.close()
