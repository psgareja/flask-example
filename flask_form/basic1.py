from flask import Flask , render_template, request, url_for,session,redirect
from flask_wtf import FlaskForm
from wtforms import (StringField,
                    BooleanField,DateTimeField,
                        RadioField,SelectField,TextField,TextAreaField,SubmitField)

from wtforms.validators import DataRequired

app=Flask(__name__)
app.config['SECRET_KEY']='mykey'


class InfoForm(FlaskForm):
    passion=StringField('What is your passion?',validators=[DataRequired()])
    student=BooleanField("Are you student?")
    department=RadioField('Please choose your department:',
                        choices=[('branch_one','CSE'),('branch_two','Mech'),('branch_three','Civ'),('branch_four','Ele')])
    subject=SelectField(u'Please Select your Subject:',choices=[('sub','A.I'),('sub2','E.H'),('sub3','I.O.T')])
    feedback=TextAreaField()
    submit=SubmitField('Submit')
@app.route('/',methods=['GET','POST'])
def index():

    form =InfoForm()
    if form.validate_on_submit():
        session['passion']=form.passion.data
        session['student']=form.student.data
        session['department']=form.department.data
        session['subject']=form.subject.data
        session['feedback']=form.feedback.data
        session['submit']=form.submit.data

        return redirect(url_for('thankyou'))

    return render_template('index.html',form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__=='__main__':
    app.run()


