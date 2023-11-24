from datetime import datetime
from typing import List

from pydantic import BaseModel


class Reading(BaseModel):
    value: float
    timestamp: datetime

    class Config:
        from_attribues = True


class Condition(Reading):
    units: str


class Conditions(BaseModel):
    temperature: Condition
    humidity: Condition


class VariableReadings(BaseModel):
    units: str
    readings: List[Reading]


class Readings(BaseModel):
    temperature: VariableReadings
    humidity: VariableReadings
