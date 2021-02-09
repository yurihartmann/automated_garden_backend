from fastapi import APIRouter

from app.routes.v1.sensors.sensors_router import sensors_router

v1_router = APIRouter()

v1_router.include_router(
    sensors_router,
    prefix='/sensors'
)
