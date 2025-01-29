from flask_sqlalchemy import SQLAlchemy
from config import Config

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = Config.SECRET_KEY
    
    db = SQLAlchemy(app)
    return db



