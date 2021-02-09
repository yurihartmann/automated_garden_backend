from tortoise.fields import *
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator


class Sensor(Model):
    id = IntField(pk=True)
    identification_number = IntField()
    name = TextField()


SensorSchema = pydantic_model_creator(Sensor, name='SensorSchema')
NewSensorSchema = pydantic_model_creator(Sensor, name='NewSensorSchema', exclude_readonly=True)
