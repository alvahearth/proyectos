from tkinter import *

root = Tk()


    

user_input = Entry(root)
user_input.pack()
def myclick():
    mylabel1 = Label(root,text=user_input.get())
    mylabel1.pack()

user_button = Button(root,text="Enter you name",command=myclick)
user_button.pack()



root.mainloop()