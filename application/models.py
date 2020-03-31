import flask
from application import db

class Room(db.Document):
    room_name   =   db.StringField( unique=True )
    room_floor  =   db.StringField( max_length=50 )
    length      =   db.IntField()
    width       =   db.IntField()