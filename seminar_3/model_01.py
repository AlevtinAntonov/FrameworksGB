import enum

from flask_sqlalchemy import SQLAlchemy

from lesson_3.app_01 import db


class GenderEnum(enum.Enum):
   MALE = 'male'
   FEMALE = 'female'


class Student(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(80), nullable=False)
   surname = db.Column(db.String(80), nullable=False)
   age = db.Column(db.Integer)
   gender = db.Column(db.Enum(GenderEnum))
   group = db.Column(db.Integer)
   faculty = db.Column(db.Integer, db.ForeignKey('faculty.id'))

   def __repr__(self):
       return f'Student ({self.name})'


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    students = db.relationship('Student', backref='faculty', lazy=True)

    def __repr__(self):
        return f'Faculty ({self.title})'