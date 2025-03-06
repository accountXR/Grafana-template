import flask
import pandas as pd
import numpy as np

app = flask.Flask(__name__)

@app.route("/draw_histogram.csv")
def show_csv():
    data = pd.read_csv('draw_histogram.csv', index_col=0, sep = ' ')
    # 去除freq为0的行
    time_start_zero = data[data['freq'] == 0].index
    data.drop(time_start_zero, inplace=True)
    csv_data = pd.DataFrame.to_csv(data, sep = ' ', doublequote = False)
    return csv_data

app.run(host="0.0.0.0", port=9997, debug=True)
