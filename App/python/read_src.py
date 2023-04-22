import json

path = "../../src/levels-limits"

def read_lvl_data(lvl):
    """The data is stored in the .txt file as followed: lat, lon, size
    where lat and long is the starting loc 

    Args:
        lvl (int): the level you want to retrieve the data for

    Returns:
        list: [lat, lon, size]
    """
    with open(path+f"/lvl{lvl}.json") as file:
        data = json.load(file)
    return data