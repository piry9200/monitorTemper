from flask import Flask
from flask import request
from flask import render_template
import json
import dataToDB

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("hello.html")

@app.route("/post", methods=["POST"])
def sendDataToDB():
    param = json.loads(request.json)
    print(param)
    date = param["date"]
    temperature = param["temperature"]
    humidity = param["humidity"]
    dataToDB(date, temperature, humidity)
    return ('200')

