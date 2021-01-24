from dbconnectpgmfaculty.db_connect_faculty import *
db=get_connection()
cursor=db.cursor()
sql="insert into faculty1(id,name,subject)values(1,'ajay','maths')"
try:
    cursor.execute(sql)
    db.commit()
    print("inserted")
except Exception as e:
    print(e.args)

finally:
    db.close()