from flask import Flask
from flask import request
from flask import render_template
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("hello.html")

@app.route("/post", methods=["POST"])
def sendDataToDB():
    param = json.loads(request.json)
    print(param)
    dates = param["date"]
    temperature = param["temperature"]
    humidity = param["humidity"]
    return ('200')