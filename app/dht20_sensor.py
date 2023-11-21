from datetime import datetime

from dht20_sensor.sensor import DHT20Sensor
from .config import settings


def get_sensor():
    if settings.use_dummy_sensor:
        return DummySensor()
    else:
        return DHT20Sensor()


class DummySensor:
    def read(self):
        timestamp = datetime.utcnow().timestamp()
        temperature = {
            "value": "23.2",
            "timestamp": timestamp,
            "units": "C",
        }
        humidity = {
            "value": "77.5",
            "timestamp": timestamp,
            "units": "%",
        }
        return (temperature, humidity)
