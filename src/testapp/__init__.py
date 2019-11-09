#server file
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from .views import main

# instantiate the database object
try:
    db = SQLAlchemy()
except Exception as e:
    return 'can not initialize db', 500

def create_app():
    try:
        app = Flask(__name__, instance_relative_config=True)
        app.config['SECRET_KEY'] = 'DontTellAnyone'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/db.sqlite3'
        
        db.init_app(app)
        
        @app.before_first_request
        def create_tables():
            from .models import Comment
            db.create_all()
        
        app.register_blueprint(main)
        
        Bootstrap(app)
        
        return app
    except Exception as e:
        return "Error in create_app: {}".format(e), 500




