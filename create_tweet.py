from get_weather import get_observation
from create_api import create_api

obs = get_observation()
tweet = f"Temperature {obs.get_weather().get_temperature(unit='celsius')} F." \
    + f" at {obs.get_location().get_name()}"

api = create_api()
