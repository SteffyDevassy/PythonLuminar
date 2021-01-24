from dbconnectpgmfaculty.db_connect_faculty import get_connection
from dbconnectpgmfaculty.db_connect_faculty import *

db=get_connection()
cursor=db.cursor()
sql="create table faculty1(id int,name varchar(10),subject varchar(10))"
try:
    cursor.execute(sql)
    print("Table created")
except Exception as e:
    print(e.args)
finally:
    db.close()
