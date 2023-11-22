from datetime import datetime
from typing import Tuple
import random

from dht20_sensor.sensor import DHT20Sensor
from .config import get_settings


def get_sensor():
    if get_settings().use_dummy_sensor:
        return DummySensor(RandomDataGenerator(23.0, 65.0))
    else:
        return DHT20Sensor()


class DummySensor:
    def __init__(self, data_generator):
        self.data_generator = data_generator

    def read(self):
        timestamp = datetime.utcnow().timestamp()
        temperature, humidity = self.data_generator.next_readings()

        temperature = {
            "value": temperature,
            "timestamp": timestamp,
            "units": "C",
        }
        humidity = {
            "value": humidity,
            "timestamp": timestamp,
            "units": "%",
        }
        return (temperature, humidity)


class RandomDataGenerator:
    def __init__(self, initial_temperature: float, initial_humidity: float):
        self.current_temperature = initial_temperature
        self.current_humidity = initial_humidity

    def update_reading(self, reading) -> float:
        delta_direction = random.randint(-1, 1)
        delta = random.randint(1, 5) / 10

        return round(reading + (delta_direction * delta), 1)

    def next_readings(self) -> Tuple[float, float]:
        self.current_temperature = self.update_reading(self.current_temperature)
        self.current_humidity = self.update_reading(self.current_humidity)

        return (self.current_temperature, self.current_humidity)
