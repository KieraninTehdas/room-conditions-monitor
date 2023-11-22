from typing import Union

from fastapi import FastAPI, Depends
from typing_extensions import Annotated

from src.sensor import get_sensor, Sensor
import src.schemas as schemas

app = FastAPI()


@app.get("/current-conditions")
def current_conditions(
    sensor: Annotated[Sensor, Depends(get_sensor)]
) -> schemas.Conditions:
    temperature, humidity = sensor.read()
    return {"temperature": temperature, "humidity": humidity}
