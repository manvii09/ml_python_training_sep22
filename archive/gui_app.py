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

msg= ttk.Variable(app)
print(msg.get())
msg.set('empty')
print(msg.get())


ttk.Label(app, text ='a simple text label').place(x=50,y=50)
ttk.Label(app,textvariable=msg, font=('Arial', 25)).place(x=100,y=70)

# a function can be assigned as an identifier.
# a function can be taken as an input argument for another function.
# a function can be defined inside a python function.
# a function can be returned from a function.

def abc():
    print ('wow')
    msg.set('jo tera man kare')

ttk.Button(app,text='click on it', command= abc).place(x=100,y=100)
ttk.Button(app,text='this ones too', font=('Arial', 25), command= lambda:msg.set('pata nhi')).place(x=100,y=170)

f1=ttk.Variable(app)
f1.set('0')
f2=ttk.Variable(app)
f2.set('0')
result=ttk.Variable(app)

ttk.Entry(app, textvariable=f1, font=('Arial',22)).place(x=50,y=250)
ttk.Entry(app, textvariable=f2, font=('Arial',22)).place(x=150,y=250)
ttk.Label(app,text='Result').place(x=300,y=30)
ttk.Label(app, textvariable=result,font=('Arial',22)).place(x=300,y=50)

def calci(op):
    print('i will calculate')
    result.set(eval(f1.get()+op+f2.get()))

ttk.Button(app, text='+', command=lambda:calci('+'), font=('Arial', 22)).place(x=50,y=300)
ttk.Button(app, text='-', command=lambda:calci('-'), font=('Arial', 22)).place(x=100,y=300)
ttk.Button(app, text='*', command=lambda:calci('*'), font=('Arial', 22)).place(x=150,y=300)
ttk.Button(app, text='/', command=lambda:calci('/'), font=('Arial', 22)).place(x=200,y=300)

#list box

box = ttk.Listbox(app,height=5,fg='red',activestyle='dotbox')
box.insert(1, 'sample1')
box.insert(2, 'sample2')
box.insert(3, 'sample3')
box.place(x=350, y=40)

def show():
    print(box.get(box.curselection()))
    
ttk.Button(app,text='show', command=show).place(x=350,y=250)

app.mainloop()