from application import app, db, routes_dungeon
from flask import render_template

@app.route("/")
@app.route("/index")
@app.route("/title")
def index():
    return render_template("index.html", title="active")
