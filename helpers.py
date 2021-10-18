from flask import Flask, request
import sqlite3

def Add_new(title, description, done):
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

def update(todo):
    with sqlite3.connect("todos.db") as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE todo SET id=?, title=?, description=?, done=? WHERE todo_id=?", todo.get("id"), todo.get("title"),  todo.get("description"), todo.get("done"))
        conn.commit()
        cursor.close()


def delete(id):
    conn = sqlite3.connect( 'todos.db')
    c = conn.cursor()
    c.execute ( "DELETE from todos WHERE rowid = (?)", id )
    conn.commit()
    conn.close()

def get_by_id(id):
        conn = sqlite3.connect('todos.db')
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM todos WHERE id=?", (id,))
        todo1= cursor.fetchall()
        conn.commit()
        cursor.close()
        return todo1