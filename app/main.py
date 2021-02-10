from fastapi import FastAPI
from starlette.responses import RedirectResponse, HTMLResponse
from starlette.status import HTTP_303_SEE_OTHER
from tortoise import Tortoise

from app.routes.mode_router import mode_router
from app.routes.sensors_router import sensors_router
from app.routes.weather_router import weather_router
from app.utils.config_connection_tortoise import config_connection_tortoise

app = FastAPI(title="Automated Garden", version="0.1.0")
AUTOMATED_GARDEN_MODE = ""


@app.on_event('startup')
async def on_startup_fast_api():
    await Tortoise.init(
        config=config_connection_tortoise()
    )
    await Tortoise.generate_schemas()


@app.on_event("shutdown")
async def on_shutdown():
    await Tortoise.close_connections()


app.include_router(
    sensors_router,
    prefix='/sensors'
)

app.include_router(
    mode_router,
    prefix='/mode'
)

app.include_router(
    weather_router,
    prefix='/weather'
)


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/mode/sync");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.get('/hc')
def health_check():
    return {"status": "OK"}
