from application import app, routes_dungeon
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")
