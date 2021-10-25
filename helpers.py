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
        cur.execute("UPDATE todo SET id=?, title=?, description=?, done=? WHERE tood_id=?",id, title, description, done )
        #ur.execute("UPDATE todo SET id=?, title=?, description=?, done=? WHERE      id=?",id, title, description, done )
        conn.commit()
        #cur.close()


def delete(id):
    with sqlite3.connect("todos.db") as conn:
        c = conn.cursor()
        c.execute ( "DELETE from todos WHERE rowid = (?)", id )
        conn.commit()
       

def get_by_id(id):
    with sqlite3.connect("todos.db") as conn:
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM todos WHERE id=?", (id,))
        todo= cursor.fetchall()
        conn.commit()
        return todo