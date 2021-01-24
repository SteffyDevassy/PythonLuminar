from dbconnectpgmfaculty.db_connect_faculty import *
db=get_connection()
cursor=db.cursor()
sql="select * from faculty1"

try:
    cursor.execute(sql)
    queryset=cursor.fetchall()
    for faculty in queryset:
        print(faculty)
except Exception as e:
    print(e.args)
finally:
    db.close()


#id=input(
# name=
# subject

