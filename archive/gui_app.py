#GUI
#libraries
################
#1. tkinter
#2. PyQT
#3. turtle

import tkinter as ttk 

app= ttk.Tk()
app.title('my app')
app.geometry('600x400')

ttk.Label(app, text ='a simple text label').place(x=50,y=50)
ttk.Label(app, text= 'manvi').place(x=60, y=80)

app.mainloop()