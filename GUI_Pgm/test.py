from tkinter import *
import tkinter.messagebox as tkMessageBox
import mysql.connector
from mysql.connector import Error


NAME = StringVar()
USER = StringVar()
PASS = StringVar()


def Database():
    global conn, cursor
    conn = mysql.connector.connect(host='localhost',
                                   database='LuminarPython',
                                   user='root',
                                   password='')
    cursor = conn.cursor()


def Exit():
    result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

def Register():
    Database()
    if NAME.get == "" or USER.get() == "" or PASS.get() == "" :
        lbl_result.config(text="Please complete the required field!", fg="orange")
    else:
        cursor.execute("SELECT * FROM `users` WHERE `users` = %s",USER.get())
        if cursor.fetchone() is not None:
            lbl_result.config(text="Username is already taken", fg="red")
        else:
            cursor.execute("INSERT INTO `user` (user, pass, name, address) VALUES(%s, %s, %s, %s)", (str(USER.get()), str(PASS.get()), str(NAME.get()), str(ADDRESS.get())))
            conn.commit()
            USER.set("")
            PASS.set("")
            NAME.set("")

            lbl_result.config(text="Successfully Created!", fg="green")
        cursor.close()
        conn.close()
TitleFrame = Frame(root, height=100, width=640, bd=1, relief=SOLID)
TitleFrame.pack(side=TOP)
RegisterFrame = Frame(root)
RegisterFrame.pack(side=TOP, pady=20)

lbl_title = Label(TitleFrame, text="IT SOURCECODE - Register Form", font=('arial', 18), bd=1, width=640)
lbl_title.pack()
lbl_username = Label(RegisterFrame, text="name:", font=('arial', 18), bd=18)
lbl_username.grid(row=1)
lbl_password = Label(RegisterFrame, text="USERNAME:", font=('arial', 18), bd=18)
lbl_password.grid(row=2)
lbl_firstname = Label(RegisterFrame, text="PASSWORD:", font=('arial', 18), bd=18)
lbl_firstname.grid(row=3)
lbl_result = Label(RegisterFrame, text="", font=('arial', 18))
lbl_result.grid(row=5, columnspan=2)

# =======================================ENTRY WIDGETS===========================
name= Entry(RegisterFrame, font=('arial', 20), textvariable=USER, width=15)
name.grid(row=1, column=1)
user = Entry(RegisterFrame, font=('arial', 20), textvariable=PASS, width=15, show="*")
user.grid(row=2, column=1)
pass1 = Entry(RegisterFrame, font=('arial', 20), textvariable=NAME, width=15)
pass1.grid(row=3, column=1)

# ========================================BUTTON WIDGETS=========================
btn_register = Button(RegisterFrame, font=('arial', 20), text="Register", command=Register)
btn_register.grid(row=6, columnspan=2)
# ========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)
