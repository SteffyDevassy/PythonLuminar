from tkinter import *
import mysql.connector
from tkinter import messagebox
root=Tk()

from dbconnectpgmfaculty.db_connect_faculty import get_connection

def db_connect(id,nam,username,password):

    db=get_connection()
    cursor=db.cursor()
    try:
        #under (,)=selection  (%)=insertion

        sql="insert into users(id,name,username,password)values('%s','%s','%s','%s')"% \
        (id,nam,username,password)
        cursor.execute(sql)
        db.commit()
        print("inserted ")

    except Exception as e:
        print(e.args)


def authenticate_user():
    id=identry.get()
    nam=nentry.get()
    uname=uentry.get()
    pwd=pentry.get()
    db_connect(id,nam,uname,pwd)
    # if(user==None):
    #     messagebox.showerror("invalid ","error")
    # else:
    #     messagebox.showinfo("user successfully logged","Info")


# def click_bnt():
#     print("hii")
idlabel=Label(root,text="id")
nlabel=Label(root,text="name")
ulabel=Label(root,text="username")
plabel=Label(root,text="password")
identry=Entry(root)
nentry=Entry(root)
uentry=Entry(root)
pentry=Entry(root)
btn=Button(root,text="ok",fg="black",command=authenticate_user)

idlabel.grid(row=0,column=0)
nlabel.grid(row=1,column=0)
ulabel.grid(row=2,column=0)
plabel.grid(row=3,column=0)
btn.grid(columnspan=2)
identry.grid(row=0,column=1)
nentry.grid(row=1,column=1)
uentry.grid(row=2,column=1)
pentry.grid(row=3,column=1)

root.mainloop()
