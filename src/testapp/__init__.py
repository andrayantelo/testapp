#server file
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy



# instantiate the database object
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY'] = 'DontTellAnyone'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/db.sqlite3'
    
    db.init_app(app)
    
    @app.before_first_request
    def create_tables():
        from .models import Comment
        db.create_all()
    
    from .views import main
    
    app.register_blueprint(main)
    
    Bootstrap(app)
    
    return app




