from flask import Flask, render_template, session, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    
    passion = StringField('What is your passion?')
    submit = SubmitField('Submit')



@app.route('/', methods=['GET', 'POST'])
def index():

   
    form = InfoForm()
    
    if form.validate_on_submit():

        session['passion'] = form.passion.data
        flash(f"You just changed your breed to: {session['passion']}")
        return redirect(url_for("cli"))


    return render_template('cli.html', form=form)


if __name__ == '__main__':
    app.run()
