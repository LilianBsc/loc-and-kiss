import geopy
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

def get_location(coordinates):
    """
    Renvoie l'objet location correspondant aux coordonnées données.
    Si les coordonnées se trouvent en dehors de toutes les frontières terrestres,
    renvoie "Mer".
    """
    lat, lon = coordinates[0], coordinates[1]
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = None
    try:
        location = geolocator.reverse(f"{lat}, {lon}")
    except GeocoderTimedOut:
        return "Erreur: GeocoderTimedOut"
    if location is not None:
        return location
    return "Sea"

def get_country(coordinates):
    location = get_location(coordinates)
    if location == "Sea":
        return "Sea"
    return location.raw["address"].get("country")

