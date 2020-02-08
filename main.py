from flask import Flask, render_template, request
from functions import *
import json

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    inputs = {}
    if request.method == "POST":
        inputs = dict(request.form)
        # for k,v in request.form.items():
        #     print(k,v)
    username = request.args.get("username")
    rating_json = []
    if username is None:
        username = ""
    else:
        rating_json = getJsonData(username, inputs)
    rating_json_dump = json.dumps(rating_json)
    color_array = [
            [0, "#808080"],
            [400, "#804000"],
            [800, "#008000"],
            [1200, "#00C0C0"],
            [1600, "#0000FF"],
            [2000, "#C0C000"],
            [2400, "#FF8000"],
            [2800, "#FF0000"],
            [3200, "#FF0000"],
            [3600, "#FF0000"],
            [4000, "#FF0000"]
    ]

    for i, c in enumerate(color_array):
        color_array[i].append("color" + str(i))
        if "color" + str(i) + "-num" in request.form:
            color_array[i][0] = request.form["color" + str(i) + "-num"]
        if "color" + str(i) + "-col" in request.form:
            color_array[i][1] = request.form["color" + str(i) + "-col"]
    color_json_dump = json.dumps(color_array)
        
    return render_template("index.html", username=username, rating_json=rating_json, rating_json_dump=rating_json_dump, color_array=color_array, color_json_dump=color_json_dump)

if __name__ == "__main__":
    app.run(debug=True)