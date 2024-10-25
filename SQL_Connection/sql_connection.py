import sqlite3

from ML.ML_core import pred
import tkinter as tk
from tkinter import *

con = sqlite3.connect("C:/Users/tymur.arduch/Desktop/project/mypay2.db")  # db connection
cur = con.cursor()  # cursor

root = tk.Tk()
root.title('SQL insertion')
root.geometry('400x400')
root.iconbitmap('myicon.ico')

tk.Label(root, text='SQL insert', font=('Helvetica', 30)).pack(side='top')

preis = StringVar()
date = StringVar()
what = StringVar()


def insertion():
    predicted_value = pred(preis.get())
    # Correctly parameterized SQL query
    sql = "INSERT INTO mypay (was, preis, datum) VALUES (?, ?, ?)"
    # Execute the query with parameters
    cur.execute(sql, (predicted_value, preis.get(), date.get()))
    # Commit the transaction
    con.commit()

    preis.set('')
    date.set('')
    tk.Label(root, text=f'Inserted as {predicted_value}', font=('Calibri', 15)).place(x=165, y=225)


def delete():
    del_sql = f"DELETE FROM mypay WHERE datum == ?"
    con.execute(del_sql, [date.get()])

    con.commit()

    date.set('')


def change():
    change_sql = f"UPDATE mypay SET was = ? WHERE datum = ?"
    cur.execute(change_sql, (what.get(), date.get()))
    con.commit()

    what.set('')
    date.set('')


tk.Label(root, text='Infos', font=('Helvetica', 12)).pack(side='bottom')
tk.Entry(root, textvariable=preis).pack(side='bottom')
tk.Button(root, text='Insert', command=insertion).place(x=180, y=300)

tk.Label(root, text='Datum', font=('Helvetica', 12)).pack(side='right')
tk.Entry(root, textvariable=date).pack(side='right')

tk.Label(root, text='Change', font=('Helvetica', 12)).pack(side='left')
tk.Entry(root, textvariable=what).pack(side='left')
tk.Button(root, text='Change', command=change).place(x=5, y=300)

tk.Button(root, text='Delete', command=delete).place(x=100, y=300)

root.mainloop()
