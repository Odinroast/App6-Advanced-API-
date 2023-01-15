import flask
import pandas as pd


app = flask.Flask(__name__)
stations = pd.read_csv("test(jupyter)/data_small/stations.txt", skiprows=17)

@app.route("/")
def home():
    return flask.render_template("home.html", data=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def api(station, date):
    filename = 'test(jupyter)/data_small/TG_STAID' + station.zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temp = df.loc[df['    DATE'] == date]['   TG'].squeeze()/10
    return{"station": station,
           "date": date,
           "temperature": temp}


if __name__ == '__main__':
    app.run(debug=True)
