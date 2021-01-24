#step 1 import mysql package
#file->settings->project->interpreter->+button->mysql-connector

#step 2 establish connection
#step 3 curser object creation
#step 3 execute queries
#step 4 close database connection

# ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Password@123'
# FLUSH PRIVILEGES;

import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    auth_plugin="mysql_native_password"
)

curser=db.cursor()
sql="SELECT VERSION()"

curser.execute(sql)
data=curser.fetchone()
print(data)