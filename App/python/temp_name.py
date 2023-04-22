import folium
from folium import plugins
import random
import read_map

def compute_rand_loc(data):
    loc = data["start_loc"]
    random_lat, random_lon = data["random_box_size_lat"], data["random_box_size_lon"]
    rand_loc =  [loc[0] + random.uniform(-random_lat, random_lat), loc[1] + random.uniform(-random_lon, random_lon)]
    if data["is_country"]:
        country = data["name"]
        while read_map.get_country(rand_loc) != country:
            rand_loc =  [loc[0] + random.uniform(-random_lat, random_lat), loc[1] + random.uniform(-random_lon, random_lon)]
    return rand_loc

def get_map_size(zoom):
    return zoom + 0.2

# start_loc = [48.864716, 2.349014]
# rand_loc = compute_rand_loc(start_loc)
# print(rand_loc)

# m = folium.Map(location=start_loc, zoom_start=12)
# folium.Marker(
#     rand_loc,
#     popup="<i>address?</i>", 
#     tooltip="Kiss here!",
#     icon=folium.Icon(color="pink", icon="heart")
# ).add_to(m)

# m.save("../../src/map/index.html")