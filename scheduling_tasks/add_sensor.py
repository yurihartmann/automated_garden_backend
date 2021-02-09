import requests

from app.settings.settings import Settings
from utils.logger import logger


def add_sensor():
    settings = Settings()

    response = requests.post(f'{settings.API_URL}/v1/sensors/sensors', json={
        "identification_number": 0,
        "name": "string"
    })

    logger.info(f"{response.status_code} - {response.content}")
