from .database import db 
from flask_security import UserMixin, RoleMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String, unique = True, nullable = False)
    username = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    # Required for flask security.
    fs_uniquifier = db.Column(db.String, unique = True, nullable = False)
    active = db.Column(db.Boolean, nullable = False)
    roles = db.relationship('Role', backref='bearer', secondary = 'users_roles') # secondary means association kounsi table me store hoga. (camelcase to kebabcase)
    # Extra attributes jo dono admin aur user m common nhi hai woh idhr aayenge.

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique =True, nullable = False)
    description = db.Column(db.String)

# Many-to-Many association table.
class UsersRoles(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

