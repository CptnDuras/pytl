from app import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    body = db.Column(db.String(5000))
    timestamp = db.Column(db.DateTime)
    due_date = db.Column(db.DateTime)
    priority = db.Column(db.DateTime)

    def __repr__(self):
        return '<Post %r>' % (self.body)
