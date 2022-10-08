import time
import board
import busio as io
import pyrebase
import busio
import adafruit_sgp30


i2c_bus = busio.I2C(board.SCL, board.SDA, frequency=100000)
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c_bus)
eCO2, TVOC = sgp30.iaq_measure()


config = {
  "apiKey": "cUWlp6gRopkybw3307qYkpv4YtB8s6xQBseq1Nwn",
  "authDomain": "robotcat-65f88.firebaseapp.com",
  "databaseURL": "https://robotcat-65f88-default-rtdb.firebaseio.com",
  "storageBucket": "robotcat-65f88.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

print("YA ESAMOS EN LINEA LUIS")
print("—————————————————————————")
print()

while True:

  ambientCelsius = float(sgp30.eCO2)
  objectCelsius = float(sgp30.TVOC)


  data = {
    "ambient": ambientCelsius,
    "object": objectCelsius,
  }
  db.child("Robot").child("1-set").set(data)
  db.child("Robot").child("2-push").push(data)

  time.sleep(2)
