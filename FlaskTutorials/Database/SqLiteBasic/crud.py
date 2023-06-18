"""
Demonstrate CRUD (Create, Read, Update, Delete) operations
"""
from main import db, Puppy, app

app.app_context().push()  # To solve 'RuntimeError: Working outside of application context.'

# Create
pup = Puppy('Tommy', 4)
db.session.add(pup)
db.session.commit()

# Read
all_pups = Puppy.query.all()  # Returns a list of Puppies in the table
print(all_pups)

# select by Id
pup_1 = Puppy.query.get(2)  # Id = 2
print(pup_1)

# Filters
sammy = Puppy.query.filter_by(name='Sammy')
print(sammy.all())

output = Puppy.query.filter_by(age=2)
print(output.all())

# Filter (gt, ge, lt, le) on basis of age
output = Puppy.query.filter(Puppy.age >= 4)
print(output.all())


# Update
temp_pup = Puppy.query.get(1)
temp_pup.age = 6
db.session.add(temp_pup)
db.session.commit()

# Delete
rm_pup = Puppy.query.get(3)

try:
    db.session.delete(rm_pup)  # Once deleted, the entry will not be found in table
except:
    print("Unable to find entry with Id=3. Not deleted.")
db.session.commit()

# Print all Puppies
all_pups = Puppy.query.all()  # Returns a list of Puppies in the table
print(all_pups)
