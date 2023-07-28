import datetime
from website import db
from .models import Book, User, CopyBook
from flask_login import login_required, current_user
from flask import Blueprint, render_template, request, flash, url_for, redirect

views = Blueprint('views', __name__)


@views.route('/')
@views.route('/home')
def home():
    print(current_user.card)
    return render_template('home.html', user=current_user)


@views.route('/about')
def about():
    return render_template('about.html', user=current_user)


@views.route('/books')
@login_required
def books():
    books_data = Book.query.all()
    return render_template('books.html', books=books_data, user=current_user)


@views.route('/books/<book_title>', methods=['GET', 'POST'])
@login_required
def book_details(book_title):
    book = Book.query.filter_by(title=book_title).first()
    if request.method == 'POST':
        if book.copybooks:
            copybook = book.copybooks[0]
            copybook.student_id = current_user.id
            copybook.loan = True
            copybook.borrowed_date = datetime.datetime.today()
            button_pushed = True
            db.session.commit()
            return render_template('book_details.html', book=book, copybook_id=copybook.id,
                                   user=current_user, button_pushed=button_pushed)
        else:
            flash('There is not available book!', 'danger')
    if book:
        button_pushed = False
        copybook_id = None
        for copybook in current_user.card:
            if copybook.book.title == book.title:
                copybook_id = copybook.id
                button_pushed = True
        return render_template('book_details.html', book=book, copybook_id=copybook_id,
                               user=current_user, button_pushed=button_pushed)
    else:
        return render_template('404.html')


@views.route('/students')
@login_required
def students():
    students_data = User.query.filter_by(status='Student').all()
    return render_template('students.html', students_data=students_data, enumerate=enumerate)


@views.route('/students/<int:student_id>')
@login_required
def student_details(student_id):
    student_data = User.query.filter_by(id=student_id, status='Student').first()
    image_file = url_for('static', filename='profile_pics/' + student_data.image_file)
    return render_template('student_details.html', student_data=student_data, image_file=image_file)


@views.route('/card')
@login_required
def card():
    return render_template('card.html', user=current_user, enumerate=enumerate)


@views.route('/books/<string:book_title>/<int:copybook_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_copybook(copybook_id, book_title):
    copybook = CopyBook.query.filter_by(id=copybook_id).first()
    current_user.card.remove(copybook)
    copybook.student_id = None
    db.session.commit()
    return redirect(url_for('views.book_details', book_title=book_title))


@views.route('/books/<string:book_title>/<int:copybook_id>', methods=['GET', 'POST'])
@login_required
def copybook_details(copybook_id, book_title):
    copybook = CopyBook.query.filter_by(id=copybook_id).first()
    if request.method == 'POST':
        return redirect(url_for('views.delete_copybook', copybook_id=copybook_id, book_title=book_title))
    return render_template('copybook_details.html', copybook=copybook)
