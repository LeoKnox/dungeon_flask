from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError

class CreateRoomForm(FlaskForm):
    room_name   =   StringField("Room Name", validators=[DataRequired()])
    room_floor  =   StringField("Room Floor", validators=[DataRequired()])
    length      =   IntegerField("Length", validators=[DataRequired()])
    Width       =   StringField("Width", validators=[DataRequired()])
    submit      =   SubmitField("Create Room")