import tkinter as ttk
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import os
print(os.getcwd())

app=ttk.Tk()
app.title('movie recommendation system')
app.geometry('400x400')

cols = ['user_id', 'movie_id', 'rating', 'ts']
df = pd.read_csv('u.data', sep = '\t', names = cols).drop('ts', axis = 1)
item_cols = ['movie_id', 'title'] + [str(i) for i in range(22)]
df1 = pd.read_csv('u.item', sep = '|', names = item_cols, encoding = "ISO-8859-1")[['movie_id', 'title']]
movie = pd.merge(df, df1, on = 'movie_id')

result= ttk.Variable(app)
box= ttk.Listbox(app, height=10)
for row, val in movie.iterrows():
    box.insert(row+1, val['title'])

box.place(x=10,y=10)

def get_movie():
    pass

ttk.Button(app,text='find recommendations', font=('Arial',22), command=get_movie).place(x=200,y=50)

ttk.Label(app, textvariable=result, font=('Arial',22)).place(x=200,y=100)

app.mainloop()