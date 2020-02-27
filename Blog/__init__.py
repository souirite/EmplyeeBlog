from flask import Flask
from config import config

app = Flask(__name__)
app.config.from_object(config)

with app.app_context():
    from .routes import main_bp
    app.register_blueprint(main_bp)

