from tkinter import *

root=Tk()
tFrame=Frame(root)
bFrame=Frame(root)

tFrame.pack()
bFrame.pack(side=BOTTOM)

btn1=Button(tFrame,text="FirstButton",fg="green")
btn2=Button(tFrame,text="SecondButton",fg="red")
btn3=Button(bFrame,text="ThirdButton",fg="blue")
btn4=Button(bFrame,text="4Button",fg="yellow")
btn3.pack()
btn1.pack()
btn2.pack()
btn4.pack()
root.title("Buttons")
root.mainloop()