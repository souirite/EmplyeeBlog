from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

with app.app_context():
    from .routes import main_bp
    app.register_blueprint(main_bp)

