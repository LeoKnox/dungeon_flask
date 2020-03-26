from application import app
from flask import render_template

room = {"room_name":"Entry", "room_floor":"stone1","length":5,"width":5}

@app.route('/rooms')
def rooms():
    print (room)
    return render_template("rooms.html", rooms="active")

@app.route('/levels')
def levels():
    return render_template("levels.html", levels="active")