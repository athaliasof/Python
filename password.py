import tkinter as tk
import tkinter.font as font
from tkinter import *

#Initialize the main window    
root = Tk()
root.title("PASSWORD")
root.resizable(False,False)
root.geometry("284x497+500+100")



#Import the image using PhotoImage function
click_btn= PhotoImage(file="C:\images\Button.png")

#Let us create a label for button event
img_label= Label(image=click_btn)

#Let us create a dummy button and pass the image
button= Button(root, image=click_btn, borderwidth=0)
button.place(x=90, y=350)


#taking inputs for password
#PassVar =  StringVar()
entPassVar = Entry(root, bd=2, font="bold", justify=LEFT)

# show entry variables to the screen
entPassVar.place(x=80, y=240, width=126, height=30)



# #icon beside the title
image_icon = PhotoImage(file="C:\images\imagetop2.png")
root.iconphoto(False,image_icon)

# #top image (Loan Calculator)
logo_image = tk.PhotoImage(file="C:\images\imagetop2.png")
Label(root,image=logo_image).place(x=115, y=55)

label_image = tk.PhotoImage(file="C:\images\Label.png")
Label(root,image=label_image).place(x=45, y=120)

label2_image = tk.PhotoImage(file="C:\images\Label2.png")
Label(root,image=label2_image).place(x=85, y=190)

line_image = tk.PhotoImage(file="C:\images\Line.png")
Label(root,image=line_image).place(x=30, y=280)



root.mainloop()
