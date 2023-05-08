from flask import Blueprint, render_template, redirect, url_for, request, flash
from init import db
from models import User
import read_src
import folium

dev = Blueprint('dev', __name__)

@dev.route("/dev/level/<lvl>")
def dev_level_screen(lvl):
    """Display the map
    """
    data = read_src.read_lvl_data(lvl)
    m = folium.Map(location=data["start_loc"], zoom_start=data["zoom"])
    nw = (data["start_loc"][0] + data["random_box_size_lat"], data["start_loc"][1] - data["random_box_size_lon"])
    ne = (data["start_loc"][0] + data["random_box_size_lat"], data["start_loc"][1] + data["random_box_size_lon"])
    sw = (data["start_loc"][0] - data["random_box_size_lat"], data["start_loc"][1] - data["random_box_size_lon"])
    se = (data["start_loc"][0] - data["random_box_size_lat"], data["start_loc"][1] + data["random_box_size_lon"])
    trail_coordinates = [nw, ne, se, sw, nw]
    folium.PolyLine(trail_coordinates, tooltip="Random box").add_to(m)
    return m.get_root().render()

@dev.route('/dev/view-users')
def view_users():
    users = {}
    _id = 1
    while User.query.filter_by(id=_id).first():
        user = User.query.filter_by(id=_id).first()
        user = user.__repr__().split(", ")
        users[_id] = user[1:]
        _id += 1
    print(users)
    return render_template("view_db.html", table_dict=users)

@dev.route('/dev/view-users/<int:id>')
def view_users_by_id(id):
    user = db.get_or_404(User, id)
    return render_template("view_data.html", key=f"User {id}", value=user)