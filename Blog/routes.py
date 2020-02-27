from flask import Blueprint

main_bp = Blueprint("main_bp",__name__,template_folder="templates", static_folder="static")

@main_bp.route('/')
@main_bp.route('/index')
def index():
    return "index"