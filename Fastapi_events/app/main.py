from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routers import events, subscriptions, users
from app.db.init_db import init_db
from app.db.session import engine


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncIterator[None]:
    await init_db()
    yield
    await engine.dispose()


app = FastAPI(title="Events API", lifespan=lifespan)
app.include_router(users.router)
app.include_router(events.router)
app.include_router(subscriptions.router)
