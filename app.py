from flask import Flask, request, render_template, redirect, url_for,jsonify,make_response,abort
from forms import TodoForm 
import SQLmodels

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


krotka=("one","two", None)
todos = SQLmodels.create_connection('database.db')
SQLmodels.add_record(krotka)
SQLmodels.print_all()



@app.route("/todos/", methods=["GET", "POST"])
def todos_list():
    form = TodoForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            todos.create(form.data)
            todos.save_all()
        return redirect(url_for("todos_list"))

    return render_template("todos.html", form=form, todos=todos.all(), error=error)


@app.route("/todos/<int:todo_id>/", methods=["GET", "POST"])
def todo_details(todo_id):
    todo = todos.get(todo_id - 1)
    form = TodoForm(data=todo)

    if request.method == "POST":
        if form.validate_on_submit():
            todos.update(todo_id - 1, form.data)
        return redirect(url_for("todos_list"))
    return render_template("todo.html", form=form, todo_id=todo_id)
######################################################################################
###______________________Część bez formularzy______________________________________###
@app.route("/api/v1/todos/", methods=["GET"])
def todos_list_api_v1():
    return jsonify(todos.all())
###_______________________________________________________
@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)
###_________________________________________________
@app.route("/api/v1/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    todo = todos.get(todo_id)
    if not todo:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        'title' in data and not isinstance(data.get('title'), str),
        'description' in data and not isinstance(data.get('description'), str),
        'done' in data and not isinstance(data.get('done'), bool)
    ]):
        abort(400)
    todo = {
        'title': data.get('title', todo['title']),
        'description': data.get('description', todo['description']),
        'done': data.get('done', todo['done'])
    }
    todos.update(todo_id, todo)
    return jsonify({'todo': todo})
    ###________________________________________________________
@app.route("/api/v1/todos/<int:todo_id>", methods=['DELETE'])
def delete_todo(todo_id):
    result = todos.delete(todo_id)
    if not result:
        abort(404)
    return jsonify({'result': result})

if __name__ == "__main__":
#       create_connection(r"todos.db")
    app.run(debug=True)

