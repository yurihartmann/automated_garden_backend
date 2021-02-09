from fastapi import FastAPI
from tortoise import Tortoise

from app.routes.v1.v1_router import v1_router
from app.settings.settings import Settings

app = FastAPI(title="Automated Garden", version="0.1.0")


@app.on_event('startup')
async def on_startup():
    await Tortoise.init(
        db_url=Settings().DATABASE_URL,
        modules={'models': ['app.models.sensor']},
    )
    await Tortoise.generate_schemas()


@app.on_event("shutdown")
async def on_shutdown():
    await Tortoise.close_connections()


app.include_router(
    v1_router,
    prefix='/v1'
)


@app.get('/hc')
def health_check():
    return {"status": "OK"}
