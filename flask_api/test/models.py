from flask_api import db

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
