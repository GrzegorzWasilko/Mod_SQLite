from flask import Flask, request
import sqlite3

def begin(title, description, done):
    sql = '''INSERT INTO todos(title, description, done)
     VALUES(?,?,?)'''
    conn = sqlite3.connect('todos.db')
    cur = conn.cursor()
    cur.execute(sql, (title, description, done))
    conn.commit()
    conn.close()

def one():
    conn = sqlite3.connect('todos.db')
    cur = conn.cursor()
    cur.execute("SELECT title,description,done FROM todos").fetchall()
    conn.commit()
    conn.close()

def update(todo):
    with sqlite3.connect("todos.db") as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE todo SET id=?, title=?, description=?, done=? WHERE todo_id=?", todo.get("id"), todo.get("title"),  todo.get("description"), todo.get("done"))
        conn.commit()
"""   def base_update(id):
    conn = sqlite3.connect('todos.db')
    cursor=conn.cursor()
    todo1=cursor.execute("SELECT * FROM todos WHERE id=?", (id,))
    todo1= cursor.fetchall()
    conn.commit()
    cursor.close() """