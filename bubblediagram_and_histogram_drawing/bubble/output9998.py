import flask
import pandas as pd
import numpy as np

app = flask.Flask(__name__)

@app.route("/bubble.csv")
def show_csv():
    data = pd.read_csv('groups_statistic.csv', index_col=0)
    csv_data = pd.DataFrame.to_csv(data)
    return csv_data

app.run(host="0.0.0.0", port=9998, debug=True)
