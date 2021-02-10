import json

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.models.history_reading_weather_sensor import HistoryReadingWeatherSensor, NewHistoryReadingWeatherSensorSchema
from app.utils.connection_manager import ConnectionManager

weather_router = APIRouter()
connection_manager = ConnectionManager()


@weather_router.websocket('/sync')
async def websocket_mode(websocket: WebSocket):
    await connection_manager.connect(websocket)
    await connection_manager.send_personal_message({"humidity": 1,
                                                    "temperature": 1}, websocket)
    try:
        while True:
            data = await websocket.receive_text()  # expected: "HUMIDITY:70|TEMPERATURE:24"
            data = data.lower().split("|")
            print(data)
            readings = {}
            for var in data:
                var = var.split(":")
                readings[var[0]] = var[1]
            try:
                new_history = NewHistoryReadingWeatherSensorSchema(temperature=readings.get('temperature'),
                                                                   humidity=readings.get('humidity'))
                await HistoryReadingWeatherSensor.create(**new_history.dict(exclude_unset=True))

                await connection_manager.broadcast({"humidity": new_history.humidity,
                                                    "temperature": new_history.temperature})
            except:
                pass

    except (WebSocketDisconnect, Exception):
        connection_manager.disconnect(websocket)
