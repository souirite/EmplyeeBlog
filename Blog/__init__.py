from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'main_bp.login'

with app.app_context():
    from .routes import main_bp
    app.register_blueprint(main_bp)
    from .errors import error
    app.register_blueprint(error)
