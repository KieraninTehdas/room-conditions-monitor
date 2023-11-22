from typing import Union

from fastapi import FastAPI, Depends
from typing_extensions import Annotated

from src.sensor import get_sensor, Sensor

app = FastAPI()


@app.get("/current-conditions")
def read_root(sensor: Annotated[Sensor, Depends(get_sensor)]):
    temperature, humidity = sensor.read()
    return {"temperature": temperature, "humidity": humidity}
