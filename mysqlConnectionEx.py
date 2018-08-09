import mysql.connector

con = mysql.connector.connect(user="root",password="root",host="localhost",database="django_app")
print(con)

cur = con.cursor()
cur.execute("insert into user_info(name,email) values('nitin','nitin@gmail.com')")

con.commit()
con.close()

print('row inserted')
