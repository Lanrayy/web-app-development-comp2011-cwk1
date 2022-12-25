from app import db

class Assessments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), index=True)
    module_code = db.Column(db.String(1000))
    status = db.Column(db.String(1000), default='Uncompleted')
    deadline = db.Column(db.Date)
    description = db.Column(db.String(10000))
