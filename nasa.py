from dotenv import find_dotenv, load_dotenv
from datetime import datetime
import os
import requests
import urllib.request

from requests.models import Response

load_dotenv(find_dotenv())


class nasa:
    def __init__(self):
        self.nasa_key = os.getenv("nasa_key")

    def astr(self):
        date = datetime.now()
        today = f"{date.year}-{date.month}-{date.day}"
        url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={today}&end_date={today}&api_key={self.nasa_key}"
        response = requests.get(url=url)
        if response.ok is True:
            response_json = response.json()
        else:
            return "Data not available"

        num_astr = response_json["element_count"]
        earth_obj = response_json["near_earth_objects"][today]

        # get the properties of each asteroid
        name_astr = []
        hazard = []
        diam_min = []
        diam_max = []
        rel_vel = []

        for obj in earth_obj:
            name_astr.append(obj["name"])
            hazard.append(
                "yes" if obj["is_potentially_hazardous_asteroid"] == "true" else "no"
            )
            diam_min.append(
                round(
                    obj["estimated_diameter"]["kilometers"]["estimated_diameter_min"],
                    3,
                )
            )
            diam_max.append(
                round(
                    obj["estimated_diameter"]["kilometers"]["estimated_diameter_max"],
                    3,
                )
            )
            rel_vel.append(
                round(
                    float(
                        obj["close_approach_data"][0]["relative_velocity"][
                            "kilometers_per_second"
                        ]
                    ),
                    3,
                )
            )

        astr_prop = {
            "name_astr": name_astr,
            "hazard": hazard,
            "diam_min": diam_min,
            "diam_max": diam_max,
            "rel_vel": rel_vel,
        }

        return num_astr, astr_prop

    def space_cme(self):
        url = f"https://api.nasa.gov/DONKI/CMEAnalysis?&mostAccurateOnly=true&speed=500&halfAngle=30&catalog=ALL&api_key={self.nasa_key}"
        response = requests.get(url=url)
        if response.ok is True:
            response_json = response.json()
        else:
            return "Data not available"

        time = []
        speed = []
        link = []
        for event in response_json:
            time.append(event["time21_5"][0:10])
            speed.append(event["speed"])
            link.append(event["link"])

        cme = {"time": time, "speed": speed, "link": link}

        return cme

    def space_flare(self):
        url = f"https://api.nasa.gov/DONKI/FLR?&api_key={self.nasa_key}"
        response = requests.get(url=url)
        if response.ok is True:
            response_json = response.json()
        else:
            return "Data not available"

        begin_time = []
        class_type = []
        link = []
        for event in response_json:
            begin_time.append(event["beginTime"][0:10])
            class_type.append(event["classType"])
            link.append(event["link"])

        flare = {"begin_time": begin_time, "class_type": class_type, "link": link}

        return flare
