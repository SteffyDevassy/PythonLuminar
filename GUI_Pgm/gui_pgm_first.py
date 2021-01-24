from tkinter import *
#minimise and close
root=Tk()
label1=Label(root,text="username")
entry1=Entry(root)
label2=Label(root,text="password")
label3=Label(root,text="email")

label1.pack()
entry1.pack()
label2.pack()
label3.pack()
root.title("Login")
root.mainloop()

