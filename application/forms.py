from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError

class CreateRoomForm(FlaskForm):
    room_name   =   StringField("Room Name", validators=[DataRequired()])
    room_floor  =   StringField("Room Floor", validators=[DataRequired()])
    length      =   IntegerField("Length", validators=[DataRequired()])
    width       =   StringField("Width", validators=[DataRequired()])
    submit      =   SubmitField("Submit Room")

class DoorForm(FlaskForm):
    room_name   =   StringField("Room Name")
    room_wall   =   IntegerField("Wall")
    wall_pos    =   IntegerField("Wall Position")
    door_type   =   StringField("Door Type")
    submit      =   SubmitField("Submit Door")