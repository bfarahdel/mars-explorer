import os
import flask
from nasa import nasa

app = flask.Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def main():

    return flask.render_template("index.html")


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

    return flask.render_template(
        "space_weather.html",
        cme_time=cme["time"],
        cme_len=len(cme["time"]),
        cme_speed=cme["speed"],
        cme_link=cme["link"],
    )


if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "0.0.0.0"),
        port=os.getenv("PORT", "8088"),
    )
