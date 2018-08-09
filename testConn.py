import mysql.connector


con  = mysql.connector.connect(user="root",password="root",host="localhost",database="django_app")
cr = con.cursor()

#write
cr.execute("insert into user_info(name,email) values('satyam','sat@gmail.com')")
con.commit()

##read
cr.execute("select * from user_info")
rs  = cr.fetchall()

for r in rs:
     print(r)
     

print('data is saved')

