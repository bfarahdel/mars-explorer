from dotenv import find_dotenv, load_dotenv
from datetime import datetime
import os
import requests
import random

load_dotenv(find_dotenv())


class nasa:
    def __init__(self):
        self.nasa_key = os.getenv("nasa_key")

    def astro_pic(self):
        url = f"https://api.nasa.gov/planetary/apod?api_key={self.nasa_key}"
        response = requests.get(url=url)
        if response.ok is True:
            response_json = response.json()
        else:
            return "Data not available"

        pic_url = (
            response_json["url"]
            if "url" in response_json
            else "No image information provided from NASA"
        )
        title = (
            response_json["title"]
            if "title" in response_json
            else "No title information provided from NASA"
        )
        expl = (
            response_json["explanation"]
            if "explanation" in response_json
            else "No explanation information provided from NASA"
        )
        copy = (
            response_json["copyright"]
            if "copyright" in response_json
            else "No copyright information provided from NASA"
        )
        media = (
            response_json["media_type"]
            if "media_type" in response_json
            else "No media information provided from NASA"
        )

        pic = {
            "pic_url": pic_url,
            "title": title,
            "expl": expl,
            "copy": copy,
            "media": media,
        }

        return pic

    def astr(self):
        date = datetime.now()
        today = f"{date.year}-{date.month}-{date.day}"
        url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={today}&end_date={today}&api_key={self.nasa_key}"
        response = requests.get(url=url)
        if response.ok is True:
            response_json = response.json()
        else:
            return "Data not available"

        num_astr = (
            response_json["element_count"]
            if "element_count" in response_json
            else "No asteroid information provided from NASA"
        )

        if "near_earth_objects" in response_json:
            earth_obj = response_json["near_earth_objects"][today]
        else:
            num_astr = "No asteroid information provided from NASA"
            astr_prop = {
                "name_astr": ["No asteroid information provided from NASA"],
                "hazard": ["No asteroid information provided from NASA"],
                "diam_min": ["No asteroid information provided from NASA"],
                "diam_max": ["No asteroid information provided from NASA"],
                "rel_vel": ["No asteroid information provided from NASA"],
            }
            return num_astr, astr_prop

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
            time.append(
                event["time21_5"][0:10]
            ) if "time21_5" in event else time.append(
                "Time info not available from NASA"
            )
            speed.append(event["speed"]) if "speed" in event else speed.append(
                "Speed info not available from NASA"
            )
            link.append(event["link"]) if "link" in event else link.append(
                "Link info not available from NASA"
            )

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
            begin_time.append(
                event["beginTime"][0:10]
            ) if "beginTime" in event else link.append(
                "Link info not available from NASA"
            )
            class_type.append(
                event["classType"]
            ) if "classType" in event else link.append(
                "Class info not available from NASA"
            )
            link.append(event["link"]) if "link" in event else link.append(
                "Link info not available from NASA"
            )

        flare = {"begin_time": begin_time, "class_type": class_type, "link": link}

        return flare

    def mars_weather(self):
        url = f"https://api.nasa.gov/insight_weather/?api_key={self.nasa_key}&feedtype=json&ver=1.0"
        response = requests.get(url=url)
        if response.ok is True:
            response_json = response.json()
        else:
            return "Data not available"

        last_time = []
        high_atm_temp = []
        low_atm_temp = []
        wind_speed = []
        atm_press = []
        season = []
        keys = list(response_json.keys())
        for event_id in list(response_json.keys())[:-2]:
            event = response_json[event_id]
            last_time.append(
                event["Last_UTC"]
            ) if "Last_UTC" in event else last_time.append(
                "Last time info not available from NASA"
            )
            high_atm_temp.append(
                round(event["AT"]["mx"], 3)
            ) if "AT" in event else high_atm_temp.append(
                "Atmospheric temperature info not available from NASA"
            )
            low_atm_temp.append(
                round(event["AT"]["mn"], 3)
            ) if "AT" in event else low_atm_temp.append(
                "Atmospheric temperature info not available from NASA"
            )
            wind_speed.append(
                round(event["HWS"]["av"], 3)
            ) if "HWS" in event else wind_speed.append(
                "Wind speed info not available from NASA"
            )
            atm_press.append(
                round(event["PRE"]["av"], 3)
            ) if "PRE" in event else atm_press.append(
                "Link info not available from NASA"
            )
            season.append(event["Season"]) if "Season" in event else season.append(
                "Season info not available from NASA"
            )

        weather = {
            "last_time": last_time,
            "high_atm_temp": high_atm_temp,
            "low_atm_temp": low_atm_temp,
            "wind_speed": wind_speed,
            "atm_press": atm_press,
            "season": season,
        }

        return weather

    def mars_rover(self):
        url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?api_key={self.nasa_key}"
        response = requests.get(url=url)
        if response.ok is True:
            response_json = response.json()
        else:
            return "Data not available"

        img = []
        earth_date = []
        sol = []
        rover_name = []
        if "latest_photos" not in response_json:
            rover_data = {
                "img": "Image not available from NASA",
                "earth_date": "Earth date not available from NASA",
                "sol": "Sol not available from NASA",
                "rover_name": "Rover name not available from NASA",
            }
            return rover_data

        photos = response_json["latest_photos"]

        photos_list = list(range(0, len(photos)))
        photo_ind = random.sample(photos_list, 3)

        for i in photo_ind:
            img.append(photos[i]["img_src"])
            earth_date.append(photos[i]["earth_date"])
            sol.append(photos[i]["sol"])
            rover_name.append(photos[i]["rover"]["name"])

        rover_data = {
            "img": img,
            "earth_date": earth_date,
            "sol": sol,
            "rover_name": rover_name,
        }

        return rover_data
