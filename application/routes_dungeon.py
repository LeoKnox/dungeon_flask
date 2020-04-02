from application import app, db
from application.forms import CreateRoomForm
from flask import render_template, redirect, url_for

single_room = {"room_name":"Throne", "room_floor":"Royal","length":6,"width":9}

class Room(db.Document):
    room_name   =   db.StringField( unique=True, max_length=30)
    room_floor  =   db.StringField( unique=True, max_length=30)
    length      =   db.IntField()
    width       =   db.IntField()

@app.route('/rooms', methods=["GET", "POST"])
def rooms():
    form = CreateRoomForm()

    if form.validate_on_submit():
        room_name   =   form.room_name.data
        room_floor  =   form.room_floor.data
        length      =   form.length.data
        width       =   form.width.data

        room = Room(room_name=room_name, room_floor=room_floor, length=length, width=width)
        room.save()

    room_list = Room.objects.all()

    return render_template("rooms.html", rooms="active", room_list=room_list, form=form)

@app.route('/levels')
def levels():
    return render_template("levels.html", levels="active")

@app.route('/edit_room', methods=['GET', 'POST'])
def edit_room():
    #single_room = Room.objects.(room_name=room_name).first()
    return render_template("edit_room.html", single_room = single_room)

@app.route('/create_room', methods=["GET", "POST"])
def create_room():
    if form.validate_on_submit():
        room_name   =   form.room_name.data
        room_floor  =   form.room_floor.data
        length      =   form.length.data
        width       =   form.width.data

        room = Room(room_name=room_name, room_floor=room_floor, length=length, width=width)
        room.save()
    return redirect(url_for('rooms'))
    