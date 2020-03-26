from application import app
from flask import render_template

@app.route('/rooms')
def rooms():
    return "<h1>Rooms</h1>"