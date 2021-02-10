from tortoise.fields import *
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator

from app.models.timestamp_mixin import TimestampMixin


class HistoryReadingWeatherSensor(Model, TimestampMixin):
    id = UUIDField(pk=True)
    temperature = FloatField()
    humidity = IntField()


HistoryReadingWeatherSensorSchema = pydantic_model_creator(cls=HistoryReadingWeatherSensor,
                                                           name='HistoryReadingWeatherSensorSchema')
NewHistoryReadingWeatherSensorSchema = pydantic_model_creator(cls=HistoryReadingWeatherSensor,
                                                              name='NewHistoryReadingWeatherSensorSchema',
                                                              exclude_readonly=True)
