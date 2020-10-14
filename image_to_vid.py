from tkinter import * #The * indicates it imports everything in tkinter
from tkinter.font import Font
from tkinter import filedialog
from copy_cut_func import rClicker
from copy_cut_func import rClickbinder

root =Tk()

root.title("Image merger") #Set title
root.geometry('1024x768+500+100') #set size of window and location it appears
root.resizable(width=True, height=True)#Prevent user from changing size of window
rClickbinder(root)#Enable copy paste as long

root.mainloop()