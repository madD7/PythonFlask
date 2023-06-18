# main.py & setupdatabase.py must be in the same directory.

from main import db, Puppy, app

# Create all the tables, transforming model class to DB table
# usually we're not going to run a separate file to actually create the database.
# There are some CLI tools that make that a lot easier.
app.app_context().push()    # To solve 'RuntimeError: Working outside of application context.'
db.create_all()

# Puppy.query.delete()          # Delete all rows of table.

# Create Puppies
sam = Puppy('Sammy', 3)
frank = Puppy('Frankie', 2)

print("Printing Id before saving")
print(f"Sammy's Id: {sam.id}")
print(f"Frankie's Id: {frank.id}")


# Save Puppy details in db
# db.session.add(sam)               # Add individual entries.
db.session.add_all([sam, frank])
db.session.commit()                 # Save changes in DB


print("Printing Id after saving")
print(f"Sammy's Id: {sam.id}")
print(f"Frankie's Id: {frank.id}")


