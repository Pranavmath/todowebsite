from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  data = db.Column(db.String(10000))
  date = db.Column(db.DateTime(timezone=True), default=func.now())
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Todo(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  data = db.Column(db.String(10000))
  date = db.Column(db.DateTime(timezone=True), default=func.now())
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  done = db.Column(db.Boolean, default=False)


class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(150), unique=True)
  password = db.Column(db.String(150))
  first_name = db.Column(db.String(150))
  notes = db.relationship('Note')
  todos = db.relationship("Todo")
  feedbacks = db.relationship("Feedback")

class Feedback(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  data = db.Column(db.String(1000))
  rating = db.Column(db.Integer)
  user_id = user_id = db.Column(db.Integer, 
                                db.ForeignKey('user.id'))