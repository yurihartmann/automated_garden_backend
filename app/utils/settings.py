import os

from app.utils.singleton import SingletonMeta


class Settings(metaclass=SingletonMeta):

    ENVIRONMENT = os.getenv("ENVIRONMENT", "DEV")
    DATABASE_URL = os.getenv("DATABASE_URL")
    DATABASE_HOST = os.getenv("DATABASE_HOST")
    DATABASE_PORT = os.getenv("DATABASE_PORT")
    DATABASE_USER = os.getenv("DATABASE_USER")
    DATABASE_PASS = os.getenv("DATABASE_PASS")
    DATABASE_NAME = os.getenv("DATABASE_NAME")
    API_URL = os.getenv("API_URL")
    MODELS_TORTOISE = ["app.models.sensor", "app.models.history_reading_soil_moisture_sensor",
                       "app.models.history_reading_weather_sensor"]

    def __init__(self):
        self.validate_api_url()
        if self.ENVIRONMENT == "DEV":
            self.validate_database_url()
        else:
            self.validate_database_host()
            self.validate_database_port()
            self.validate_database_user()
            self.validate_database_pass()
            self.validate_database_name()

    def validate_database_url(self):
        if self.DATABASE_URL is None:
            raise ValueError("DATABASE_URL should be not empty")

    def validate_database_host(self):
        if self.DATABASE_HOST is None:
            raise ValueError("DATABASE_HOST should be not empty")

    def validate_database_port(self):
        if self.DATABASE_PORT is None:
            raise ValueError("DATABASE_PORT should be not empty")

    def validate_database_user(self):
        if self.DATABASE_USER is None:
            raise ValueError("DATABASE_USER should be not empty")

    def validate_database_pass(self):
        if self.DATABASE_PASS is None:
            raise ValueError("DATABASE_PASS should be not empty")

    def validate_database_name(self):
        if self.DATABASE_NAME is None:
            raise ValueError("DATABASE_NAME should be not empty")

    def validate_api_url(self):
        if self.API_URL is None:
            raise ValueError("API_URL should be not empty")
