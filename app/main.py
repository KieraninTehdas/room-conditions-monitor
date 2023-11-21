from typing import Union

from fastapi import FastAPI

from .dht20_sensor import get_sensor

app = FastAPI()
sensor = get_sensor()


@app.get("/")
def read_root():
    temperature, humidity = sensor.read()
    return {"temperature": temperature, "humidity": humidity}
