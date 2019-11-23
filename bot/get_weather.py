import pyowm
import numpy as np
from pyowm.tiles.enums import MapLayerEnum
from pyowm.commons.tile import Tile
from pyowm.utils.geo import Point
import pandas as pd


def get_observation():
    entry = pd.read_csv("cities.csv").sample()
    city = entry["City"].values[0]
    state = entry["State short"].values[0]
    owm = pyowm.OWM('03a2f49a1242c4094d3593b314fff7f0')
    # reg = owm.city_id_registry()
    # ids = reg.ids_for(f'Cambridge', 'US')
    # owm.weather_at_coords(lat, lon)
    observation = owm.weather_at_place(f"{city},us")
    return observation
