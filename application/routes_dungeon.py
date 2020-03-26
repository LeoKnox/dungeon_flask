from application import app
from flask import render_template

room_list = [
        {"room_name":"Entry", "room_floor":"stone1","length":5,"width":5},
        {"room_name":"Throne", "room_floor":"Royal","length":6,"width":9}
]

@app.route('/rooms')
def rooms():
    return render_template("rooms.html", rooms="active", room_list=room_list)

@app.route('/levels')
def levels():
    return render_template("levels.html", levels="active")