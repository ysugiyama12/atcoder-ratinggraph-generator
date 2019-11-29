from flask import Flask, render_template, request
from functions import *
import json

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    inputs = {}
    if request.method == "POST":
        print(request.form)
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
    return render_template("index.html", username=username, rating_json=rating_json, rating_json_dump=rating_json_dump)

if __name__ == "__main__":
    app.run(debug=True, port=5050)