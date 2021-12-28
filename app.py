import os
import flask
from nasa import nasa

app = flask.Flask(__name__)
app.secret_key = os.getenv("appSecret")


@app.route("/", methods=["POST", "GET"])
def main():
    astro_pic = nasa().astro_pic()
    return flask.render_template(
        "index.html",
        pic_url=astro_pic["pic_url"],
        pic_title=astro_pic["title"],
        pic_expl=astro_pic["expl"],
        pic_copy=astro_pic["copy"],
        pic_media=astro_pic["media"],
    )


@app.route("/asteroids", methods=["POST", "GET"])
def astr():
    astr_num, astr_prop = nasa().astr()
    return flask.render_template(
        "asteroids.html",
        astr_num=astr_num,
        astr_name=astr_prop["name_astr"],
        astr_prop_len=len(astr_prop["name_astr"]),
        astr_hazard=astr_prop["hazard"],
        astr_diam_min=astr_prop["diam_min"],
        astr_diam_max=astr_prop["diam_max"],
        astr_rel_vel=astr_prop["rel_vel"],
    )


@app.route("/space_weather", methods=["POST", "GET"])
def space():
    cme = nasa().space_cme()
    flare = nasa().space_flare()

    return flask.render_template(
        "space_weather.html",
        cme_time=cme["time"],
        cme_len=len(cme["time"]),
        cme_speed=cme["speed"],
        cme_link=cme["link"],
        flare_time=flare["begin_time"],
        flare_len=len(flare["begin_time"]),
        flare_class=flare["class_type"],
        flare_link=flare["link"],
    )


@app.route("/mars", methods=["POST", "GET"])
def mars():
    weather = nasa().mars_weather()
    rover = nasa().mars_rover()

    if weather["last_time"] == []:
        flask.flash("No weather data is currently available from NASA.")

    return flask.render_template(
        "mars.html",
        mars_weather_time=weather["last_time"],
        mars_weather_len=len(weather["last_time"]),
        mars_high_atm_temp=weather["high_atm_temp"],
        mars_low_atm_temp=weather["low_atm_temp"],
        mars_wind_speed=weather["wind_speed"],
        mars_atm_press=weather["atm_press"],
        mars_season=weather["season"],
        mars_r_img=rover["img"],
        mars_r_len=len(rover["img"]),
        mars_r_date=rover["earth_date"],
        mars_r_sol=rover["sol"],
        mars_r_name=rover["rover_name"],
    )


if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "0.0.0.0"),
        port=os.getenv("PORT", "8088"),
    )
