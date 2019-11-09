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
    return render_template('base.html')
    
@main.route('/home')
def home():
    comments = Comment.query.all()
    return render_template('home.html', comments=comments)
    
@main.route('/sign', methods=['GET', 'POST'])
def sign():
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
