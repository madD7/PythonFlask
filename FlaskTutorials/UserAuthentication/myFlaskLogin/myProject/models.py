from myProject import db
from werkzeug.security import generate_password_hash, check_password_hash
from myProject import login_manager

# using UserMinin, We get access to a lot of built-in attributes which will then be
# able to call in our actual views.
from flask_login import UserMixin


# Allows flash-login to load the current user and grab their id
# Thus, when some-one logins, the app will be able to show only pages/data related to that user.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# Inheriting UserMixin, as it has all management features of logging & user auth.
class User(db.Model, UserMixin):
    __tablename__ ='users'
    id = db.Column(db.Integer, primary_key=True)

    # Unique, to prevent multiple users have same email id.
    emailid = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True,index=True)
    password = db.Column(db.String(128))

    def __init__(self, emailid, username, password):
        self.emailid = emailid
        self.username = username
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)



