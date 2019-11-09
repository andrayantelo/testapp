from flask import Blueprint, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Email, Length

from . import db
from .models import Comment



main = Blueprint('main', __name__)

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(message="Please provide your name")])
    comment = TextAreaField('Comment',  validators=[Length(min=2, max=280), InputRequired(message="Please leave a comment")])

@main.route('/')
def index():
    return 'Ok', 200
    try:
        return render_template('base.html')
    except Exception as e:
        return "Error in '/': {}".format(e), 500
        
@main.route('/ok', methods=['GET'])
def ok():
    return 'OK', 200
    
@main.route('/home')
def home():
    try:
        comments = Comment.query.all()
        return render_template('home.html', comments=comments)
    except Exception as e:
        return "Error in '/home': {}".format(e), 500
    
@main.route('/sign', methods=['GET', 'POST'])
def sign():
    try:
        form = RegistrationForm()
        if not form.validate_on_submit:
            return render_template('sign.html', form=form)
        if form.validate_on_submit():
            name = request.form.get('name')
            comment = request.form.get('comment')
            
            new_comment = Comment(name=name, comment_text=comment)
            db.session.add(new_comment)
            db.session.commit()
            
            return redirect(url_for('main.home'))
        return render_template('sign.html', form=form)
    except Exception as e:
        return "Error in '/sign': {}".format(e), 500
    
