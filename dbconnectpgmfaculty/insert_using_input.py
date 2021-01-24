from dbconnectpgmfaculty.db_connect_faculty import *
db=get_connection()
cursor=db.cursor()
f_id=input("FacultyId")
f_name=input("Name")
f_subject=input("Subject")
cursor.execute("""insert into faculty1(id,name,subject)
values(%s,%s,%s)""",(f_id,f_name,f_subject))

print("inserted")

db.commit()
db.close()