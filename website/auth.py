import os
import secrets
from PIL import Image
from .models import User, db
from .forms import LoginForm, RegistrationForm, UpdateAccountForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import logout_user, login_required, login_user, current_user
from flask import Blueprint, flash, render_template, redirect, request, url_for

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if form.validate_on_submit():
            if user:
                if check_password_hash(user.password, password):
                    flash(f"You have been logged in!", 'success')
                    login_user(user, remember=(form.remember.data == 'y'))
                    return redirect('home')
                else:
                    flash(f"Incorrect password, try again", category='danger')
            else:
                flash('Email does not exists.', category='danger')
    return render_template('login.html', title='Login', form=form, user=current_user)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = RegistrationForm()
    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data
        status = form.status.data
        if form.validate_on_submit():
            user = User.query.filter_by(email=email).first()
            if user:
                flash('Email already exists.', category='danger')
            else:
                user = User(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            username=first_name+' '+last_name,
                            password=generate_password_hash(password, method='sha256'),
                            status=status)
                db.session.add(user)
                db.session.commit()
                flash(f"Account have been created! You are now able to log in", 'success')
                return redirect('login')
    return render_template('sign_up.html', title='Sign Up', form=form, user=current_user)


def save_picture(form_picture):
    from main import app
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (179, 179)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@auth.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.picture.data:
                picture_file = save_picture(form.picture.data)
                current_user.image_file = picture_file
            current_user.username = form.username.data
            current_user.email = form.email.data
            db.session.commit()
            flash('Your account has been updated!', 'success')
            return redirect(url_for('auth.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form, user=current_user)
