from fastapi.testclient import TestClient

from datetime import datetime
from typing import Tuple

from src.main import app
from src.sensor import get_sensor, DummySensor

client = TestClient(app)

now = datetime.utcnow()
temperature = 23.4
humidity = 76.8


class ConstantDataGenerator:
    def __init__(self, temperature: float, humidity: float):
        self.temperature = temperature
        self.humidity = humidity

    def next_readings(self) -> Tuple[float, float]:
        return (self.temperature, self.humidity)


def constant_sensor():
    return DummySensor(ConstantDataGenerator(temperature, humidity), now)


app.dependency_overrides[get_sensor] = constant_sensor


def test_current_conditions():
    response = client.get("/current-conditions")

    assert response.status_code == 200
    assert response.json() == {
        "temperature": {
            "value": temperature,
            "timestamp": now.timestamp(),
            "units": "C",
        },
        "humidity": {"value": humidity, "timestamp": now.timestamp(), "units": "%"},
    }
