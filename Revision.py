from tkinter import *
root=Tk()
######################################

def function():
    Label(text="I am good boy.",fg="Red",font="mango 10 bold").grid(row=1,column=1)
######################################


js=Menu(root)
sj=Menu(js,tearoff=0)
sj.add_command(label="New Project",command=function)
sj.add_command(label="New",command=function)
######################################



sj.add_separator()
######################################


sj.add_command(label="Setting",command=function)
sj.add_command(label="File Properties",command=function)
######################################

root.config(menu=js)

######################################

js.add_cascade(label="File",menu=sj)

######################################



root.mainloop()






















































