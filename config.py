class config(object):
    DEBUG = True
    SECRET_KEY = "secret"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///appDB.db'
