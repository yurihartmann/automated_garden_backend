import os

from utils.singleton import SingletonMeta


class Settings(metaclass=SingletonMeta):

    DATABASE_URL = os.getenv("DATABASE_URL")

    def __init__(self):
        self.validate_database_url()

    def validate_database_url(self):
        if self.DATABASE_URL is None:
            raise ValueError("DATABASE_URL should be not empty")
