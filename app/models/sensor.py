from tortoise.fields import *
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator

from app.models.timestamp_mixin import TimestampMixin


class Sensor(Model, TimestampMixin):
    id = UUIDField(pk=True)
    identification_number = IntField(unique=True)
    name = TextField()


SensorSchema = pydantic_model_creator(Sensor, name='SensorSchema')
NewSensorSchema = pydantic_model_creator(Sensor, name='NewSensorSchema', exclude_readonly=True)
