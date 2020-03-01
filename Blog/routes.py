from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from .forms import LoginForm, RegistrationForm, EditProfileForm
from .models import User
from Blog import db
from datetime import datetime

main_bp = Blueprint("main_bp", __name__,
                    template_folder="templates", static_folder="static")


@main_bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@main_bp.route('/')
@main_bp.route('/index')
@login_required
def index():
    user = {'username': 'Ziad'}
    posts = [
        {
            'author': {'username': 'Zaid'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'dad'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title='Home Page', posts=posts)


@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.index'))
    form = LoginForm()
    if request.method == "POST" and form.validate:
        user = User.query.filter_by(username=form.username.data).first()
        print(user.password_hash)
        if user.password_hash != form.password.data:
            flash('Invalid username or password')
            print('not pass')
            return redirect(url_for('main_bp.login'))
        else:
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('main_bp.index'))

    return render_template('login.html', title='Sign In', form=form)


@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == "POST" and form.validate:
        user = User(username=form.username.data,
                    email=form.email.data, password_hash=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main_bp.login'))
    return render_template('register.html', title='Register', form=form)


@main_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main_bp.index'))


@main_bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)


@main_bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('main_bp.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)
