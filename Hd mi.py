from tkinter import *
root=Tk()
root.geometry("400x500")
root.minsize(200,300)
root.title("Pycharm")
a="""5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
"""
c="""












"""
def printing1():
    for i in range(1):
        Label(text=a,font="mango 10 bold",fg="Cyan",bg="Black").grid(row=i,column=1)
def printing():
    Label(root,text="Python",font="mango 20 bold").grid(row=1,column=1)


'''m1=Menu(root)
m1.add_command(label = "File",command=printing1 )
m1.add_command(label="Exit",command=quit)
root.config(menu=m1)
# m1.add_command(label="my first")
# root.config(menu=m1)
'''
def delete():
    Label(root,text=c,font="mango 20 bold").grid(row=1,column=1)

yourmenubar=Menu(root)
m1=Menu(yourmenubar)
m1.add_command(label="Save",command=printing1)
m1.add_command(label="Save as",command=printing)
m1.add_command(label="Open",command=delete)
root.config(menu=yourmenubar)
yourmenubar.add_cascade(label="File",menu=m1)




"""filemenu=Menu(root)
m1=Menu(filemenu,tearoff=0)
m1.add_command(label="Save",command=printing1)
m1.add_command(label="Save as",command=printing)
m1.add_command(label="Open",command=delete)
root.config(menu=filemenu)
filemenu.add_cascade(label="File",menu=m1)"""



# maianmenu=Menu(root)
# m1=Menu(maianmenu,tearoff=0)
# m1.add_command(label="Save",command=printing1)
# m1.add_command(label="Save as",command=printing)
# m1.add_separator()
# m1.add_command(label="Open",command=delete)
# root.config(menu=maianmenu)
# maianmenu.add_cascade(label="File",menu=m1)







if __name__ == '__main__':
    root.mainloop()
