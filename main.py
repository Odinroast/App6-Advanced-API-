import flask

app = flask.Flask(__name__)


@app.route("/home")
def home():
    return flask.render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def api(station, date):
    temperature = 23
    return {"station" : station,
            "date": date,
            "temperature": temperature}


if __name__ == '__main__':
    app.run(debug=True)
