import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot
import tkinter as ttk
from tkinter import *
from PIL import Image,ImageTk

app=ttk.Tk()
app.geometry('600x300')
app.title('Treadmil User Analysis')

#Create an instance of tkinter frame
win = Tk()

#Set the geometry of tkinter frame
win.geometry("750x270")

#Create a canvas
canvas= Canvas(win, width= 600, height= 400)
canvas.pack()

#Load an image in the script
img= ImageTk.PhotoImage(Image.open("download.png"))

#Add image to the Canvas Items
canvas.create_image(10,10,anchor=NW,image=img)

win.mainloop()