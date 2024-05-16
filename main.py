from __future__ import annotations
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict
from fastapi import Depends
from contextlib import asynccontextmanager
from database import create_tables, delete_tables

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("База готова")
    yield
    await delete_tables()
    print("База очищена")


app = FastAPI(lifespan=lifespan)


class STaskAdd(BaseModel):
    name: str
    description: str


class STask(STaskAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)


@app.get("/")
async def home():
    return {"data": "Hello world"}


@app.post("/")
async def add_task(task: STaskAdd = Depends()):
    return {"data": task}



