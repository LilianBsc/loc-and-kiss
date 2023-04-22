""" flask_example.py

    Required packages:
    - flask
    - folium

    Usage:

    Start the flask server by running:

        $ python flask_example.py

    And then head to http://127.0.0.1:5000/ in your browser to see the map displayed

"""

from flask import Flask, render_template_string
import temp_name as tn
import folium
import read_src

app = Flask(__name__)

@app.route("/")
def welcomescreen():
    """Display the map
    """
    m = folium.Map(location=[0, 0], zoom_start=12)
    folium.Marker(
    [0, 0], 
    popup="<i>Point Némo</i>", 
    tooltip="Click here !",
    icon=folium.Icon(color="blue", prefix="fa", icon="anchor")
    ).add_to(m)
    return m.get_root().render()

@app.route("/dev/level/<lvl>")
def devlvlscreen(lvl):
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

@app.route('/level/<lvl>')
def lvl_screen(lvl):
    data = read_src.read_lvl_data(lvl)
    rand_mark_loc = tn.compute_rand_loc(data)
    m = folium.Map(location=data["start_loc"], zoom_start=data["zoom"])
    folium.Marker(
    rand_mark_loc, 
    popup=f"<i>{round(rand_mark_loc[0], 4)}N, {round(rand_mark_loc[1], 4)}E</i>", 
    tooltip="Kiss here!",
    icon=folium.Icon(color="pink", prefix="fa", icon="face-kiss-wink-heart")
    ).add_to(m)

    return m.get_root().render()

if __name__ == "__main__":
    app.run(debug=True)