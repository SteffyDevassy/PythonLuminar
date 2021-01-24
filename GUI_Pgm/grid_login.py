from tkinter import *
from tkinter import messagebox
root=Tk()

from dbconnectpgmfaculty.db_connect_faculty import get_connection

def db_connect(username,password):
    print("inside")
    db=get_connection()
    cursor=db.cursor()
    try:

        cursor.execute(("select * from users where username=%s AND password=%s"),(username,password))
        user=cursor.fetchone()
        return user

    except Exception as e:
        print(e.args)


def authenticate_user():
    uname=uentry.get()
    pwd=pentry.get()
    user=db_connect(uname,pwd)
    if(user==None):
        messagebox.showerror("invalid ","error")
    else:
        messagebox.showinfo("user successfully logged","Info")


# def click_bnt():
#     print("hii")
ulabel=Label(root,text="username")
plabel=Label(root,text="password")
uentry=Entry(root)
pentry=Entry(root)
btn=Button(root,text="ok",fg="black",command=authenticate_user)


ulabel.grid(row=0,column=0)
plabel.grid(row=1,column=0)
btn.grid(columnspan=2)
uentry.grid(row=0,column=1)
pentry.grid(row=1,column=1)

root.mainloop()
