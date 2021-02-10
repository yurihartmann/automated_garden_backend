import json

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.utils.connection_manager import ConnectionManager
from app.utils.mode_manager import ModeManager, AUTO, MANUAL

mode_router = APIRouter()
mode_manager = ModeManager()
connection_manager = ConnectionManager()


@mode_router.websocket("/sync")
async def websocket_mode(websocket: WebSocket):
    await connection_manager.connect(websocket)
    await connection_manager.send_personal_message_text(f"MODE:{mode_manager.get_mode()}", websocket)
    try:
        while True:
            data = await websocket.receive_text()  # expected: "MODE:AUTO" or "MODE:MANUAL"
            data = data.split(":")[1]

            if data.upper() == AUTO:
                mode_manager.set_mode(AUTO)
            elif data.upper() == MANUAL:
                mode_manager.set_mode(MANUAL)

            # await mode_manager.broadcast({"mode": mode_manager.get_mode()})

    except (WebSocketDisconnect, Exception):
        connection_manager.disconnect(websocket)
