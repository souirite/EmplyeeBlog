from flask import Blueprint, render_template
from .forms import LoginForm

main_bp = Blueprint("main_bp",__name__,template_folder="templates", static_folder="static")

@main_bp.route('/')
@main_bp.route('/index')
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
    return render_template('index.html', title='Home', user=user, posts=posts)
@main_bp.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)