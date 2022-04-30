# tuong tac voi bang user trong CSDL --> Flask
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from app.modules.common.model import Model
from app import db


class User(Model):
    """
    Define the model
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)

    firstname = db.Column(db.String)
    lastname = db.Column(db.String)

    email = db.Column(db.String)  # (255), unique=True)
    password_hash = db.Column(db.String)  # (128), default='')
    admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)