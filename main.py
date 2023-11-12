from typing import Union

from fastapi import FastAPI

from dht20_sensor.sensor import DHT20Sensor

app = FastAPI()
sensor = DHT20Sensor()


@app.get("/")
def read_root():
    temperature, humidity = sensor.read()
    return {"temperature": temperature, "humidity": humidity}
