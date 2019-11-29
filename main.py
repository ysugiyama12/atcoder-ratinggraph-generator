from flask import Flask, render_template, request
from functions import *

app = Flask(__name__)

@app.route('/')
def index():
    username = request.args.get("username")
    rating_json = ""
    if username is None:
        username = ""
    else:
        rating_json = getJsonData(username)
    return render_template("index.html", username=username, rating_json=rating_json)

if __name__ == "__main__":
    app.run(debug=True, port=5050)