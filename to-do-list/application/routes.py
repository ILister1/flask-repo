from application import app, db
from application.models import Lists, Tasks, Lists_Tasks
from flask import render_template
@app.route('/')
def read():
    all_tasks = Tasks.query.all()
    tasks_string = ""
    for task in all_tasks:
        tasks_string += "<br>" + task.name
   
    return tasks_string

@app.route('/add')
def add():
    new_task = Tasks(name="New Task", description="first task")
    db.session.add(new_task)
    db.session.commit()
    return "Added new task to todo list"

@app.route('/update/<name>')
def update(name):
    first_task = Tasks.query.first()
    first_task.name = name
    db.session.commit()
    return first_task.name

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Tasks.query.get(id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return "You have deleted a task!"

