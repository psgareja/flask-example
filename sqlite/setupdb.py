from basic import db,Pradip
#create all the tables
db.create_all()

pradi=Pradip('pradip',21)
bharat=Pradip('Bharat',30)

print(pradi.id)
print(bharat.id)

db.session.add_all([pradi,bharat])

db.session.commit() 
print(pradi.id)
print(bharat.id)