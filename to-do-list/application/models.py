from application import db

class Lists_Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    list_id = db.Column('lists_id', db.Integer, db.ForeignKey('lists.id'))
    task_id = db.Column('tasks_id', db.Integer, db.ForeignKey('tasks.id'))

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    description = db.Column(db.String(255))
    lists_tasks = db.relationship('Lists_Tasks', backref='tasks')


class Lists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    lists_tasks = db.relationship('Lists_Tasks', backref='lists')


