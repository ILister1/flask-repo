from application import app, db
from application.models import Todos
from flask import render_template, redirect, url_for, request
from application.forms import TodoForm


#class BasicForm(FlaskForm):
#    task_name = StringField('Task Name')
#    submit = SubmitField('Add Task')

@app.route('/')
def index():
    all_todos = Todos.query.all()
    return render_template('index.html', all_todos=all_todos)

@app.route('/add', methods=['POST'])
def add():
    form = TodoForm()
    if form.validate_on_submit():
        new_todo = Todos(task=form.task.data)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.route('/complete/<int:todo_id>')
def complete(todo_id):
    todo_to_update = Todos.query.get(todo_id)
    todo_to_update.complete = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/incomplete/<int:todo_id>')
def incomplete(todo_id):
    todo_to_update = Todos.query.get(todo_id)
    todo_to_update.complete = False
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:todo_id>', methods=['GET', 'POST'])
def update(todo_id):
    form = TodoForm()
    todo_to_update = Todos.query.get(todo_id)
    if form.validate_on_submit():
        todo_to_update.task = form.task.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == "GET":
        form.task.data = todo_to_update.task
    return render_template('update.html', form=form)
#def update(task):
 #   todo_to_update = Todos.query.first()
  #  todo_to_update.task = task
   # db.session.commit()
   # return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo_to_delete = Todos.query.get(todo_id)
    db.session.delete(todo_to_delete)
    db.session.commit()
    return redirect(url_for('index'))



    

#@app.route('/read')
#def read():
 #   all_tasks = Tasks.query.all()
  #  tasks_string = ""
   # for task in all_tasks:
    #    tasks_string += "<br>" + task.name
   
   # return tasks_string

#@app.route('/add')
#def add():
#    new_task = Tasks(name="New Task", description="first task")
#    db.session.add(new_task)
#    db.session.commit()
#    return "Added new task to todo list"

#@app.route('/update/<name>')
#def update(name):
#    first_task = Tasks.query.first()
#    first_task.name = name
#    db.session.commit()
#    return first_task.name
#
#@app.route('/delete/<int:id>')
#def delete(id):
#    task_to_delete = Tasks.query.filter_by(id=int(id)
#    db.session.delete(task_to_delete)
#    db.session.commit()
#    return "You have deleted a task"


#@app.route('/complete/<id>')
#def complete(id):
##
#    task = Tasks.query.filter_by(id=int(id)).first()
#    todo.complete = True
#    db.session.commit()
#
#    return redirect(url_for('index'))


#@app.route('/incomplete/<id>')
#def incomplete(id):
#
 #   task = Tasks.query.filter_by(id=int(id)).first()
 #   task.complete = False
 #   db.session.commit()

#    return redirect(url_for('index'))
