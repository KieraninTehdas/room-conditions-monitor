from datetime import datetime

from pydantic import BaseModel


class Reading(BaseModel):
    value: float
    timestamp: datetime
    units: str


class Conditions(BaseModel):
    temperature: Reading
    humidity: Reading
