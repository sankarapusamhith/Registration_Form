from home import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30))
    email=db.Column(db.String(100),unique=True,nullable=False)
    country=db.Column(db.String(30))
    nationality=db.Column(db.String(30))
    phone=db.Column(db.String(10))
    role=db.Column(db.String(10))
    password=db.Column(db.String(30),nullable=False)
