from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root,borderwidth=2,width=35)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def mybutton(x):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(x))
    
def clearbutton():
    e.delete(0,END)
    
def sum_button():
    global num
    first_num = e.get()
    num = first_num
    e.delete(0,END)
    
def equal_button():
    second_num = e.get()
    e.delete(0,END)
    e.insert(0,int(num) + int(second_num))
    
    
#defining buttons

button_1 = Button(root,text="1",padx=40,pady=20,command=lambda: mybutton(1))
button_2 = Button(root,text="2",padx=40,pady=20,command=lambda: mybutton(2))
button_3 = Button(root,text="3",padx=40,pady=20,command=lambda: mybutton(3))
button_4 = Button(root,text="4",padx=40,pady=20,command=lambda: mybutton(4))
button_5 = Button(root,text="5",padx=40,pady=20,command=lambda: mybutton(5))
button_6 = Button(root,text="6",padx=40,pady=20,command=lambda: mybutton(6))
button_7 = Button(root,text="7",padx=40,pady=20,command=lambda: mybutton(7))
button_8 = Button(root,text="8",padx=40,pady=20,command=lambda: mybutton(8))
button_9 = Button(root,text="9",padx=40,pady=20,command=lambda: mybutton(9))
button_0 = Button(root,text="0",padx=40,pady=20,command=lambda: mybutton(0))
button_sum = Button(root,text="+",padx=39,pady=20,command=sum_button)
button_equal = Button(root,text="= ",padx=85,pady=20,command=equal_button)
button_clear = Button(root,text="Clear",padx=77.1,pady=20,command=clearbutton)

#buttons on the screen

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_sum.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)

root.mainloop()