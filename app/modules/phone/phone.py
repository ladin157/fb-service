from app.modules.common.model import Model
from app import db


class Phone(Model):
    """
    Define the model
    """
    __tablename__ = 'phone'
    id = db.Column(db.Integer, primary_key=True)

    address = db.Column(db.String)
    phone = db.Column(db.String)
