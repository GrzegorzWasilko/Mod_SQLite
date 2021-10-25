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
        helpers.add_new(title, description, done)
    todos = helpers.print_all()
    return render_template("todos.html", form=form, todos=todos, error=error)


@app.route('/todo_id/<int:id>/', methods=['GET','POST'])
def update(id):
    todo=helpers.get_by_id(id)
    print ("w todo znajduje się {todo}")
    form=TodoForm( data = todo )# form=TodoForm(data = todo)
    print(todo[0])
    for i in form:
        print(i)
    print(form('description'))
    print("=======>> =======>> wykonało się get")
    if request.method =='POST':
        print("=======>> =======>> wykonało się początek update")
        id = request.form.get('id')
        title = request.form.get('title')
        description = request.form.get('description')
        done = request.form.get('done')
        helpers.update(id,title, description, done)
        print(' <<====<<<====<<====<<<==== został wywołany POOST UPDATE zwracam  form ')
        return redirect ( url_for('todos_list')) #return render_template("todos.html",form=form,todo=todo)
    return (render_template("todo_id.html", id=id, form=form, todo=todo))

if __name__ == "__main__":
    app.run(debug=True) 