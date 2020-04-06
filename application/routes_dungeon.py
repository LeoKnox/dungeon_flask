from application import app, db
from application.forms import CreateRoomForm, DoorForm
from application.models import Room, Door
from flask import render_template, redirect, url_for

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

@app.route('/edit_room/<room_name>', methods=['GET', 'POST'])
def edit_room(room_name):
    form = CreateRoomForm()
    door_form = DoorForm()
    single_room = Room.objects(room_name=room_name).first()
    doors = list( Room.objects.aggregate(*[
        {
            '$lookup': {
                'from': 'Door', 
                'localField': 'room_name', 
                'foreignField': 'room_name', 
                'as': 'r1'
            }
        }, {
            '$match': {
                'room_name': room_name
            }
        }
    ]))

    if form.validate_on_submit():
        room = {
            "room_name":form.room_name.data,
            "room_floor":form.room_floor.data,
            "length":form.length.data,
            "width":form.width.data
        }
        single_room.update(**room)
        return redirect(url_for('edit_room', room_name=room_name))
    return render_template("edit_room.html", single_room = doors[0], form=form, door_form=door_form)

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
    
@app.route('/add_door', methods=["GET", "POST"])
def add_door():
    if form.validate_on_submit():
        room_name   =   form.room_name.data
        room_wall   =   form.room_wall.data
        wall_pos    =   form.wall_pos.data
        door_type   =   form.door_type.data
        
        door = Door(room_name=room_name, room_wall=room_wall, wall_pos=wall_pos, door_type=door_type)
        door.save()
    return redirect(url_for('edit_room', room_name=room_name))