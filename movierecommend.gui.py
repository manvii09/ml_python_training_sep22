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

frame = ttk.Frame(app)
frame.place(x=10, y=10)
box= ttk.Listbox(frame, height=10, width= 50, fg='red', activestyle='dotbox')
for title in movie['title'].unique():
    box.insert(ttk.END, title)

#box.grid(row=0,coloumn=0)
box.pack(side='left', fill='y')
#box place(x=10,y=10)

scroll = ttk.Scrollbar(frame,orient=ttk.VERTICAL)
scroll.config(command = box.yview)
box.config(yscrollcommand=scroll.set)
scroll.pack(side='right', fill='y')

def get_movie():
    movie_selected = box.get(box.curselection())
    print('movie _selected:', movie_selected)

     #Creating a Pivot Table
    movie_pivot = movie.pivot_table(index = 'user_id', columns = 'title', values = 'rating')
    
    #Finding the similarity for the Selected Movie
    corrs = movie_pivot.corrwith(movie_pivot[movie_selected])
    corrs_df = pd.DataFrame(corrs, columns = ['correlation'])
    corrs_df['avg_ratings'] = movie.groupby('title')['rating'].mean()
    corrs_df['count'] = movie['title'].value_counts()
    
    #Finding the top 2-3 Recommendations
    top_recom = list(corrs_df[corrs_df['count'] > 50].sort_values(by = 'correlation', ascending = False).head(3).index)
    top_recom.remove(movie_selected)

    #important
    if movie_selected in top_recom:
        top_recom.remove(movie_selected)
    print('Recommendations', top_recom)   

    if top_recom:
        result.set(top_recom[0])
    else:
        result.set('sorry no recommendations found !!')     

    result.set(top_recom[0])

ttk.Button(app,text='find recommendations', font=('Arial',22), command=get_movie).place(x=10,y=250)

ttk.Label(app, textvariable=result, font=('Arial',22)).place(x=10,y=300)

app.mainloop()