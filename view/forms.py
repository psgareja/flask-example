from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField
class AddForm(FlaskForm):
    name=StringField('Name of puppy')
    submit=SubmitField('Add Puppy')

class DelForm(FlaskForm):
    id=IntegerField('Id number of puppy to Remove:')
    submit=SubmitField('Remove Puppy')

class AddOwnerForm(FlaskForm):
    name=StringField('Name of Owner')
    pup_id=IntegerField('Puppy id')
    submit=SubmitField('Add Owner')
