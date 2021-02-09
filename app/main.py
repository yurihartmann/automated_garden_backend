from fastapi import FastAPI
from starlette.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER
from tortoise import Tortoise

from app.routes.v1.v1_router import v1_router
from utils.config_connection_tortoise import config_connection_tortoise

app = FastAPI(title="Automated Garden", version="0.1.0")


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
    v1_router,
    prefix='/v1'
)


@app.get('/')
def home():
    return RedirectResponse(url="/docs", status_code=HTTP_303_SEE_OTHER)


@app.get('/hc')
def health_check():
    return {"status": "OK"}
