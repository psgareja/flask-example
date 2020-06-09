from flask import Flask
from flask_restful import Resource,Api
from secure_api import authenticate ,identity
from flask_jwt import JWT,jwt_required

from flask_sqlalchemy import SQLALchemy 
from flask_migrate import Migrate 
app=Flask(__name__)

basedir=os.path.abspath(os.path.dirname(__file__))
app.config=['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
db=SQLALchemy(app)
Migrate(app,db)

app.config['SECRET_KEY']="daijdjd"
api=Api(app)
jwt=JWT(app,authenticate,identity)
puppies=[]


#############################
class Puppy(db.Model):
    name=db.Column(db.String(80,primary_key=True))
    def __init__(self,name):
        self.name=name

    def json(self):
        return {'name':self.name}



class PuppyName(Resource):
   
    def get(self,name):
        pup=Puppy.query.filter_by(name=name).first()
        if pup:
            return pup.json()
        else:


            return {'name':None}
        
    def post(self,name):
        pup=Puppy(name=name)
        db.session().add(pup)
        db.session.commit()

        return pup.json()


    

        
    def delete(self,name):
        pup=Puppy.query.filter_by(name=name).first()
        db.session.delete(pup)
        db.session.commit()
        return "delete succcess"

class AllName(Resource):
    #@jwt_required()
    def get(self):
        puppies=Puppy.query.all()
        return [pup.json() for pup in puppies ]


        
api.add_resource(PuppyName,'/puppy/<string:name>')
api.add_resource(AllName,'/puppies')
if __name__=='__main__':
    app.run()
