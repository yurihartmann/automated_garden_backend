from fastapi import APIRouter

from app.models.sensor import NewSensorSchema, Sensor, SensorSchema

sensors_router = APIRouter()


@sensors_router.post('/sensors')
async def add_sensor(new_sensor: NewSensorSchema):
    sensor_obj = await Sensor.create(**new_sensor.dict(exclude_unset=True))
    return await SensorSchema.from_tortoise_orm(sensor_obj)
