
from flask_login import UserMixin
from . import db

class user(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))

    def __init__(self,username,password):
        self.username = username
        self.password = password

class worker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    surname = db.Column(db.String(20))
    adres = db.Column(db.String(50))

    def __init__(self, name, surname, adres):
        self.name = name
        self.surname = surname
        self.adres = adres
