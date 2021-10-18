from flask import Flask, request, render_template, redirect, url_for

from forms import TodoForm
import sqlite3

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route('/todos/', methods=["GET", 'POST'])
def todos_list():
    form = TodoForm()
    error = ""
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        done = request.form.get('done')

        sql = '''INSERT INTO todos(title, description, done)
             VALUES(?,?,?)'''
        conn = sqlite3.connect('todos.db')
        cur = conn.cursor()
        cur.execute(sql, (title, description, done))
        conn.commit()
        conn.close()
    conn = sqlite3.connect('todos.db')
    cur = conn.cursor()
    todos = cur.execute("SELECT title,description,done FROM todos").fetchall()
    conn.commit()
    conn.close()

    return render_template("todos.html", form=form, todos=todos, error=error)


@app.route('/todos/<int:id>/', methods=['GET','POST'])
def update(id):
    if request.method=='GET':
        conn = sqlite3.connect('todos.db')
        cursor=conn.cursor()
        todo1=cursor.execute("SELECT * FROM todos WHERE id=?", (id,))
        todo1= cursor.fetchall()
        conn.commit()
        cursor.close()
        return (render_template("todo.html", todo1=todo1))


    if request.method =='POST':
        conn = sqlite3.connect('todos.db')
        #fetch form data
        todo= request.form
        #P_ID=productDetails['P_ID']
        id= todo['id']
        title=todo['title']
        description= todo['description']
        done= todo['done']
        cursor = conn.cursor()
        cursor.execute("UPDATE todo SET id=?, title=?, description=?, done=? WHERE todo_id=?",(id,title,description,done))
        conn.commit()
        cursor.close()
        conn.commit()
        conn.close()
    return render_template("todo.html", id=id)

if __name__ == "__main__":
    app.run(debug=True)