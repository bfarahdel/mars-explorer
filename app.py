import os
import flask

app = flask.Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def main():

    return flask.render_template("index.html")


if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "0.0.0.0"),
        port=os.getenv("PORT", "8088"),
    )
