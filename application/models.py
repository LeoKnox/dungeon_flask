import flask
from application import db

class Room(db.Document):
    room_name   =   db.StringField( unique=True )
    room_floor  =   db.StringField( max_length=50 )
    length      =   db.IntField()
    width       =   db.IntField()

class Door(db.Document):
    room_name   =   db.StringField()
    room_wall   =   db.IntField()
    wall_pos    =   db.IntField()
    door_type   =   db.StringField()