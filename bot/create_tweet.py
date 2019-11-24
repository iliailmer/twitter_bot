from get_weather import get_observation
from create_api import create_api

import time
if __name__ == "__main__":
    while True:
        obs = get_observation()
        w = obs.get_weather()
        temperature = f"It's " \
            + f"{w.get_temperature(unit='celsius')['temp']}"\
            + " degrees Celsius" +\
            f" with {w.get_detailed_status().lower()}"
        if len(obs.get_location().get_name()) > 0:
            location = f" at {obs.get_location().get_name()}, " +\
                f"{obs.get_location().get_lat()}, {obs.get_location().get_lon()}"
        else:
            location = f" at {obs.get_location().get_lat()},"\
                + f"{obs.get_location().get_lon()}."
        tweet = temperature + location
        api = create_api()
        # print(tweet)
        api.update_status(tweet)
        time.sleep(60*60*24)
