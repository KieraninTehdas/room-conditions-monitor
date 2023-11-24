from typing import Union, List
from typing_extensions import Annotated
from datetime import datetime

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from src.sensor import get_sensor, Sensor
from src.database import get_db, engine
from src import reading_repository
import src.schemas as schemas
import src.models as models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/current-conditions")
def current_conditions(
    sensor: Annotated[Sensor, Depends(get_sensor)]
) -> schemas.Conditions:
    temperature, humidity = sensor.read()
    return schemas.Conditions.model_validate(
        {"temperature": temperature, "humidity": humidity}
    )


@app.get("/temperature-readings", response_model=List[schemas.Reading])
def temperature_readings(
    from_timestamp: datetime, to_timestamp: datetime, db: Session = Depends(get_db)
):
    return reading_repository.get_temperatures(
        db, from_timestamp.timestamp(), to_timestamp.timestamp()
    )
