from basic import db,Pradip

##create
my_pradi=Pradip('pradip',21)
db.session.add(my_pradi)
db.session.commit()


##read

all_pradi=Pradip.query.all()
print(all_pradi)

#select by id
pradi_one=Pradip.query.get(1)

print(pradi_one.name)

 ##filter
pradi_filter=Pradip.query.filter_by(name='pradip')
print(pradi_filter.all())

first_pradi=Pradip.query.get(1)
first_pradi.age=40
db.session.add(first_pradi)
db.session.commit()

second_one=Pradip.query.get(2)
db.session.delete(second_one)
db.session.commit()

all_p=Pradip.query.all()
print(all_p)