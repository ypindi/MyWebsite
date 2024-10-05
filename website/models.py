from . import db
# from website import db
# website and . are same
from flask_login import UserMixin
# flask module which helps with flask login
# custom class that we can inherit
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone = True), default = func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # here we are storing a foreign key on a child object that references
    # every parent object. 1-many relationship.
    # for foreign key, it should be small ('user.id')
    # Foreign key is only in 1-many relationship

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    # creating an ID for all users to uniquely identify them.
    # because some of them may have the same email ID too.
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    # max 150 characters
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    # for relationship, your referencing name of class - it is capital.

    # yapindi - NEW CHANGES
    def is_active(self):
        return True