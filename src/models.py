from sqlalchemy import Column, Integer, Float, TIMESTAMP
from sqlalchemy.orm import relationship

from src.database import Base


class TemperatureReading(Base):
    __tablename__ = "temperature_readings"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(Float)
    timestamp = Column(TIMESTAMP, index=True)


class HumidityReading(Base):
    __tablename__ = "humidity_readings"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(Float)
    timestamp = Column(TIMESTAMP, index=True)
