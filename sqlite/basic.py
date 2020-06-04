import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
basedir=os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

Migrate(app,db)
#################################################
class Pradip(db.Model):
    #manual table name
    __tablename__='pradip'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    age=db.Column(db.Integer)
    passion=db.Column(db.Text)

    def __init__(self,name,age,passion):
        self.name=name
        self.age=age
        self.passion=passion

    def __repr__(self):
        return f"pradip {self.name } is {self.age} year/s old and my passion is: {self.passion}"
