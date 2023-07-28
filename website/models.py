import datetime
from . import db
from datetime import date, timedelta
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    username = db.Column(db.String(60))
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    card = db.relationship('CopyBook', backref='user', lazy=True)
    status = db.Column(db.String(9), nullable=False, default='Student')

    def __repr__(self):
        return f"User({self.first_name!r}, {self.last_name!r}, " \
               f"{self.email!r}, {self.image_file!r}, {self.card})"


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), unique=True, nullable=False)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    year_first_published = db.Column(db.DateTime, nullable=False, default=date.today() - timedelta(1))
    genre = db.Column(db.String(60), nullable=False)
    copybooks = db.relationship('CopyBook', backref='book', lazy=True)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"Book({self.title!r}, {self.isbn!r}, " \
               f"{self.genre!r}, {self.year_first_published})"


class CopyBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    isbn_copy = db.Column(db.String(13), unique=True, nullable=False)
    borrowed_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.today())
    year_published = db.Column(db.DateTime, nullable=False, default=datetime.datetime.today())
    condition_rating = db.Column(db.Integer, nullable=False, default=10)
    loan = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"CopyBook({self.book_id}, {self.isbn_copy!r}, " \
               f"{self.year_published}, {self.borrowed_date}, " \
               f"{self.condition_rating}, {self.loan}, {self.student_id})" \
