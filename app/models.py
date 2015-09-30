from app import db
from datetime import datetime

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    body = db.Column(db.String(5000), nullable=True)
    timestamp = db.Column(db.DateTime, nullable=True)
    due_date = db.Column(db.DateTime, nullable=True)
    priority = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Post %r>' % (self.body)

    def __init__(self, name, body="", timestamp=datetime.now(), priority=5):
        self.name = name
        self.body = body
        self.timestamp = timestamp
        self.priority = priority

    def set_body(self, body):
        self.body = body

    def set_due_date(self, duedate):
        self.due_date = duedate
