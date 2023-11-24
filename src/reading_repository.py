from datetime import datetime

from sqlalchemy.orm import Session
from typing import Union

import src.schemas as schemas
import src.models as models


def get_temperatures(db: Session, from_timestamp: float, to_timestamp: float):
    return get_readings(db, models.TemperatureReading, from_timestamp, to_timestamp)


def get_humidities(db: Session, from_timestamp: float, to_timestamp: float):
    return get_readings(db, models.HumidityReading, from_timestamp, to_timestamp)


def get_readings(
    db: Session,
    reading_model: Union[models.TemperatureReading, models.HumidityReading],
    from_timestamp: float,
    to_timestamp: float,
):
    return db.query(reading_model).filter(
        models.TemperatureReading.timestamp.between(from_timestamp, to_timestamp)
    )


def save_temperature(db: Session, temperature: schemas.Reading):
    return save_reading(db, models.TemperatureReading, temperature)


def save_humidity(db: Session, humidity: schemas.Reading):
    return save_reading(db, models.HumidityReading, humidity)


def save_reading(
    db: Session,
    reading_model: Union[models.TemperatureReading, models.HumidityReading],
    reading: schemas.Reading,
):
    db_reading = reading_model(**reading.dict)
    db.add(db_reading)
    db.commit()
    db.refresh(db_reading)
    return db_reading
