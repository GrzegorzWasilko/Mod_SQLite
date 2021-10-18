from flask import Flask, request, render_template, redirect, url_for
from forms import TodoForm
import sqlite3
import helpers
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
        helpers.Add_new(title, description, done)
    todos = helpers.print_all()
    return render_template("todos.html", form=form, todos=todos, error=error)


@app.route('/todos/<int:id>/', methods=['GET','POST'])
def update(id):
    form=TodoForm()
    if request.method=='GET':
        todo=helpers.get_by_id(id)
        return (render_template("todo_id.html", todo=todo, form=form))
    if request.method =='POST':
        todo=helpers.get_by_id(id)
        helpers.update(todo)
    return render_template("todo.html", id=id,form=form,todo=todo)


if __name__ == "__main__":
    app.run(debug=True) 