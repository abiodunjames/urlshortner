from fastapi import FastAPI

from app.api.db import database, engine, metadata
from app.api.routes import route

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup() -> None:
    await database.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    await database.disconnect()


app.include_router(route)