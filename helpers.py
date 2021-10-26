from flask import Flask, request
import sqlite3

def add_new(title, description, done):
    sql = '''INSERT INTO todos(title, description, done)
     VALUES(?,?,?)'''
    conn = sqlite3.connect('todos.db')
    cur = conn.cursor()
    cur.execute(sql, (title, description, done))
    conn.commit()
    conn.close()

def print_all():
    conn = sqlite3.connect('todos.db')
    cur = conn.cursor()
    tasks_list = cur.execute("SELECT title,description,done FROM todos").fetchall()
    conn.commit()
    conn.close()
    return tasks_list

def update(id,title, description, done):
    with sqlite3.connect("todos.db") as conn:
        cur = conn.cursor()
        cur.execute("UPDATE todos SET title=?, description=?, done=? WHERE id=?", (title, description, done, id))
        #cur.execute("UPDATE todo SET id=?, title=?, description=?, done=? WHERE id=?", id, title, description, done )
        #ur.execute("UPDATE todos<= SET id=?, title=?, description=?, done=? WHERE  todo_id=?",id, title, description, done )
        cur.close()
        conn.commit()
        #cur.close()


def delete(id):
    with sqlite3.connect("todos.db") as conn:
        c = conn.cursor()
        c.execute ( "DELETE from todos WHERE rowid = (?)", id )
        conn.commit()
       

def get_by_id(id):
    with sqlite3.connect("todos.db") as conn:
        cur=conn.cursor()
        cur.execute("SELECT * FROM todos WHERE id=?", (id,))
        todo= cur.fetchone() # c.fetchall() powodowało zwrot listy zmiana na c.fetchone() zwraca tuple 
        conn.commit()
        return todo