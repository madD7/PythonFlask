from myProject import db


### Model for db
class Puppy(db.Model):
    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref='Puppy', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"{self.owner.name} is owner of Puppy {self.name}. Pup Id: {self.id}."
        else:
            return f"Puppy {self.name} has no owner yet. Pup Id: {self.id}."


class Owner(db.Model):
    __tablename__ = 'owner'
    name = db.Column(db.Text)
    id = db.Column(db.Integer, primary_key=True)
    pup_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, pup_id):
        self.name = name
        self.pup_id = pup_id
