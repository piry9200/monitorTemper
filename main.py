from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
from flask_cors import CORS
from dictOfFunction import dataToDB
from dictOfFunction import dataFromDB 
import json

secretKeyJson = "./tempcontrol-fd850-firebase-adminsdk-f43jn-fe3be151b4.json"

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return render_template("hello.html")

@app.route("/post", methods=["POST"])
def sendDataToDB():
    param = json.loads(request.json)
    #print(param)
    date = param["date"]
    temperature = param["temperature"]
    humidity = param["humidity"]
    dataToDB.dateToDB(secretKeyJson, date, temperature, humidity)
    return ('200')

@app.route("/get", methods=["GET"])
def demandDataFromDB():
    data = dataFromDB.dataFromDB(secretKeyJson)
    return jsonify(data)