# # from tkinter import *
# # root=Tk()
# # #############################################
# # height=400
# # width=500
# # root.title("Creating a window")
# # root.geometry(f"{width}x{height}")
# #
# # ############################################
# # '''def re():
# #     root.geometry(f"{i.get()}x{ii.get()}")'''
# #
# #
# # '''if True:
# #     Label(text="Width").grid(row=0,column=1)
# #     Label(text="Height").grid(row=1,column=1)
# #     i=StringVar()
# #     ii=StringVar()
# #     Entry(root,textvariable=i).grid(row=0,column=2)
# #     Entry(root,textvariable=ii).grid(row=1,column=2)
# #     Button(text="Apply", command=re).grid(row=2, column=1)'''
# #
# #
# #
# # ############################################
# #
# # m1=Menu(root)
# # m2=Menu(m1,tearoff=0)
# # m2.add_command(label="New project")
# # m2.add_command(label="New")
# # m2.add_command(label="Increase",)
# # m2.add_command(label="Save as")
# # m2.add_command(label="Open")
# # m2.add_separator()
# # a=m2.add_command(label="Setting")
# # m3=Menu(a)
# # m2.add_separator()
# # m2.add_command(label="Save All")
# # m2.add_command(label="Print")
# # m2.add_separator()
# # m2.add_command(label="Exit",command=quit)
# # root.config(menu=m1)
# # m1.add_cascade(label="File",menu=m2)
# # #############################################
# # f1=Frame(root,bg="Black",borderwidth=5,relief=SUNKEN)
# # f1.grid(row=4,column=3)
# # Label(f1,text="Name",bg="White",fg="Black",font="mango 10 bold").grid(row=4,column=1)
# # Checkbutton(f1,text="Check!",font="mango 10 bold").grid(row=5,column=1)
# # Button(f1,text="Submit",bg="White",fg="Black",font="mango 10 bold").grid(row=4,column=2)
# # i1=StringVar()
# # Entry(textvariable=i1).grid(row=6,column=2)
# # root.mainloop()
# #
# #
# #
# #
#
#
#
# """m1=Menu(root)
# m2=Menu(m1,tearoff=0)
# m3=Menu(m2,tearoff=0)
# m2.add_command(label="New")
# m2.add_command(label="New Project")
# m3.add_command(label="Save as")
# root.config(menu=m1)
# m1.add_cascade(label="File",menu=m2)
# m2.add_separator()
# m2.add_cascade(label="Setting",menu=m3)"""
# '''
# def apply():
#     f1.grid(row=0, column=3)
#     Label(f1, text="Height").grid(row=0, column=1)
#     Label(f1, text=" Width ").grid(row=1, column=1)
#     height = StringVar()
#     width = StringVar()
#     Entry(f1, textvariable=height).grid(row=0, column=2)
#     Entry(f1, textvariable=width).grid(row=1, column=2)
#     Button(f1, text="Submit", command=apply).grid(row=2, column=1)
#     root.geometry(f"{width}x{height}")
# def resize():
#    pass
# def font_size():
#     f1=Frame(root,borderwidth=3,relief=SUNKEN,bg="Black")
#     f1.grid(row=0,column=3)
#     Label(f1,text="Height").grid(row=0,column=1)
#     Label(f1,text=" Width ").grid(row=1,column=1)
#     height=StringVar()
#     width=StringVar()
#     # textvariable
#     Entry(f1,textvariable=height).grid(row=0,column=2)
#     Entry(f1,textvariable=width).grid(row=1,column=2)
#     Button(f1,text="Submit",command=apply).grid(row=2,column=1)'''
#
# # textvariable
#
# from tkinter import*
# root=Tk()
# #########################
# width=500
# height=300
# root.geometry(f"{width}x{height}")
# #########################
# f1 = Frame(root, borderwidth=3, relief=SUNKEN, bg="Black")
#
#
#
#
# ##########################
# m1=Menu(root)
# m2=Menu(m1,tearoff=0)
# m3=Menu(m2,tearoff=0)
# m4=Menu(m3,tearoff=0)
# #########################################
# m2.add_command(label="New")
# m2.add_command(label="Save")
# m2.add_separator()
# m2.add_command(label="Save as")
# m3.add_command(label="Font size")
# m3.add_command(label="Editor")
# m3.add_separator()
# m4.add_command(label="Show History")
# m4.add_command(label="Put label...")
# m4.add_separator()
# m4.add_command(label="Exit",command=exit)
# m4.add_command(label="Quit",command=quit)
# #########################################
# root.config(menu=m1)
# m1.add_cascade(label="File",menu=m2)
# m2.add_cascade(label="Setting",menu=m3)
# m2.add_command(label="File data")
# m3.add_cascade(label="History",menu=m4)
# m3.add_command(label="Save all")
#
#
#
#
#
#
#
#
#
# if __name__ == '__main__':
#     root.mainloop()



from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
def apj():
    print("I will help you.")
    a=tmsg.showinfo("Help","I will help you.")
    print(a)
m1=Menu(root)
m1.add_command(label="Help",command=apj)
root.config(menu=m1)



root.mainloop()