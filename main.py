from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict

app = FastAPI()


@app.get("/")
async def home():
    return {"data": "Hello world"}


class STaskAdd(BaseModel):
    name: str
    description: str


@app.post("/")
async def add_task(task: STaskAdd):
    return {"data": task}


class STask(STaskAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)
