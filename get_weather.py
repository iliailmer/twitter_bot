import pyowm
from numpy import random
from pyowm.tiles.enums import MapLayerEnum
from pyowm.commons.tile import Tile
from pyowm.utils.geo import Point


def get_observation():
    lat, lon = random.uniform(-90., 90.), random.uniform(-180., 180.)

    owm = pyowm.OWM('03a2f49a1242c4094d3593b314fff7f0')

    observation = owm.weather_at_coords(lat, lon).get_weather()
    return observation
