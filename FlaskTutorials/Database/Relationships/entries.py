# Enter data into the db tables

from main import db, Puppy, Toy, Owner, app

app.app_context().push()    # To solve 'RuntimeError: Working outside of application context.'
db.create_all()
Puppy.query.delete()

# Creating 2 Puppies
rufus = Puppy("Rufus")
fido = Puppy("Fido")

db.session.add_all([rufus, fido])
db.session.commit()

# Verify
print(Puppy.query.all())

# Get rufus info from db
rufus = Puppy.query.filter_by(name='Rufus').first()
# Alternatively, Puppy.query.filter_by(name='Rufus').all()[0]

rufus_list = Puppy.query.filter_by(name='Rufus').all()

# Create owner for Rufus
Jim = Owner("Jim", rufus.id)

# Toys for Rufus
toy1 = Toy("Chewy", rufus.id)
toy2 = Toy("Ball", rufus.id)

db.session.add_all([Jim, toy1, toy2])
db.session.commit()
print(Puppy.query.all())


