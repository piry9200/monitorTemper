from urllib import response
import RPi.GPIO as GPIO
import requests
from DHT11 import dht11
import datetime
import json

url = "http://127.0.0.1:5000/post"
now = datetime.datetime.now()

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin=14)

try:
	result = instance.read()
	if result.is_valid():#DHT11から正しくデータを取得できたら
		date = now.strftime("%Y.%m.%d.%H:%M")
		temperature = result.temperature
		humidity = result.humidity
		datas = {   "date" : date,
			"temperature" : temperature,
			"humidity" : humidity
		}
	response = requests.post(url, json = json.dumps(datas))

except KeyboardInterrupt:
	print("Cleanup")
	GPIO.cleanup()