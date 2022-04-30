from app.modules.common.model import Model
from app import db


class User(Model):
    """
    Define the model
    """
    __tablename__ = 'phone_address'
    id = db.Column(db.Integer, primary_key=True)

    address = db.Column(db.String)
    phone = db.Column(db.String)
