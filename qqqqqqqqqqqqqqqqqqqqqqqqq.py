i=int(input(":-"))
for ii in range(1,11):
    print(f"{i} * {ii} = {i*ii}")
exit()


from tkinter import *
root=Tk()
root.geometry("400x500")
f1=Frame(root,bg="Black",borderwidth=7,relief=SUNKEN)
f1.grid(row=1,column=3)
i=IntVar()
def table():
    global i
    for ii in range(1,11):
        Label(f1,text=(f"{str(i.get())} * {str(ii)} = {str(i.get() * ii)}")).grid(row=3,column=2)
Label(f1,text="Which table you want to print :",font="mango 10 bold",fg="Light blue",bg="Dark blue").grid(row=1,column=1)
Entry(f1,textvariable=i).grid(row=1,column=2)
Button(f1,text="Search",font="mango 10 bold",command=table,bg="Dark blue",fg="Light blue").grid(row=2,column=1)
Button(f1,text="Quit",font="mango 10 bold",command=quit,bg="Dark blue",fg="Light blue").grid(row=2,column=2)


root.mainloop()