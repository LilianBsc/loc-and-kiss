""" flask_example.py

    Required packages:
    - flask
    - folium

    Usage:

    Start the flask server by running:

        $ python flask_example.py

    And then head to http://127.0.0.1:5000/ in your browser to see the map displayed

"""
from flask import Blueprint, render_template
import folium
import read_map, read_src, services
from init import db
from flask_login import login_required, current_user
from models import Loc

game = Blueprint('game', __name__)

@game.route("/")
def welcome_screen():
    """Display the map
    """
    return render_template("welcome.html")

@game.route("/level")
@login_required
def select_level_screen():
    """Display the map
    """
    return render_template("select_level.html")

@game.route('/level/<lvl>')
@login_required
def level_screen(lvl):
    data = read_src.read_lvl_data(lvl)
    rand_mark_loc = services.compute_rand_loc(data)

    # Fill database
    new_loc = Loc(lattitude=rand_mark_loc[0], longitude=rand_mark_loc[1], user=current_user)
    db.session.add(new_loc)
    db.session.commit()
    
    m = folium.Map(location=data["start_loc"], zoom_start=data["zoom"])
    folium.Marker(
    rand_mark_loc, 
    popup=f"<i>{round(rand_mark_loc[0], 4)}N, {round(rand_mark_loc[1], 4)}E</i>", 
    tooltip="Kiss here!",
    icon=folium.Icon(color="pink", prefix="fa", icon="face-kiss-wink-heart")
    ).add_to(m)
    return m.get_root().render()

