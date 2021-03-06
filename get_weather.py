"""Module for getting weather."""
import pyowm
import numpy as np
from pyowm.tiles.enums import MapLayerEnum
from pyowm.commons.tile import Tile
from pyowm.utils.geo import Point
import pandas as pd
from os import environ


def get_observation():
    """Get the weather for a random city from the cities.csv."""
    entry = pd.read_csv("./cities.csv").sample()
    city = entry["City"].values[0]
    state = entry["State short"].values[0]
    owm = pyowm.OWM(environ['OWM_KEY'])
    observation = owm.weather_at_place(f"{city},us")
    return observation
