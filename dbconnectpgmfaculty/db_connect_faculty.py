import mysql.connector

def get_connection():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Password@123",
        database="LuminarPython",
        auth_plugin="mysql_native_password"
    )
    return db



#db_connect+craete_table+packagedbconnectpgm