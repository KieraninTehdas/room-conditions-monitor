from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    use_dummy_sensor: bool = False


settings = Settings()
