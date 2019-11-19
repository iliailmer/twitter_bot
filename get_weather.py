import pyowm
import numpy as np
from pyowm.tiles.enums import MapLayerEnum
from pyowm.commons.tile import Tile
from pyowm.utils.geo import Point


def get_observation():
    lat, lon = np.random.uniform(-90., 90.), np.random.uniform(-180., 180.)

    owm = pyowm.OWM('03a2f49a1242c4094d3593b314fff7f0')

    observation = owm.weather_at_coords(lat, lon)
    return observation
