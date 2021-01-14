from tkinter import *
from PIL import ImageTk,Image
import os

root = Tk()
root.title("Hello bitches")

#image files root
my_img1 = ImageTk.PhotoImage(Image.open("C:/Users/tekke/Desktop/pythonfiles/images/foto1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("C:/Users/tekke/Desktop/pythonfiles/images/foto2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("C:/Users/tekke/Desktop/pythonfiles/images/foto3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("C:/Users/tekke/Desktop/pythonfiles/images/foto4.jpg"))

#list of images
my_list = [my_img1, my_img2, my_img3, my_img4]

#puts the first image on the screen
my_label = Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

#adds an status bar
status = Label(root,text="Image 1 of " + str(len(my_list)) + " ",bd=1,relief=SUNKEN,anchor=E)

#function that retrieves a number so that you can nnavigate the list
def image_next(number):
    #define global variables
    global my_label
    global image_next
    global image_back
    
    #deletes the image onscreen
    my_label.grid_forget()
    #puts the next image on the screen
    my_label = Label(image=my_list[number-1])
    my_label.grid(row=0,column=0,columnspan=3)
    
    #the "next" button is available to advance in the list
    button_next = Button(root,text=">>",command=lambda : image_next(number+1))
    #the "before" button can go backwards in the list
    button_before = Button(root,text="<<",command=lambda : image_next(number-1))
    
    #if the number is the same as the last element of the length, disable the next button
    if number == 4:
        button_next = Button(root,text=">>",state=DISABLED)
    # if the number is the same as the first element, disable the before button
    elif number == 1:
        button_before = Button(root,text="<<",state=DISABLED)
    
    #adds an status bar that dinamically changes base on the current number
    status = Label(root,text="Image "+ str(number) + " of " + str(len(my_list)) + " ",bd=1,relief=SUNKEN,anchor=E)
    
    #puts the information onscreen
    my_label.grid(row=0,column=0,columnspan=3)
    button_next.grid(row=1,column=2)
    button_before.grid(row=1,column=0)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)
    
def image_back():
    return

#buttons
button_before = Button(root,text="<<",command=image_back,state=DISABLED)
button_quit = Button(root,text="quit",command=root.quit)
button_next = Button(root,text=">>",command=lambda: image_next(2))

button_before.grid(row=1,column=0)
button_quit.grid(row=1,column=1,pady=8)
button_next.grid(row=1,column=2)

status.grid(row=2,column=0,columnspan=3,sticky=W+E)


root = mainloop()