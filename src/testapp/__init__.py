#server file
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy



# instantiate the database object
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'DontTellAnyone'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/db.sqlite3'
    
    db.init_app(app)
    
    from .views import main
    
    app.register_blueprint(main)
    
    Bootstrap(app)
    
    return app




