from pydantic import BaseModel

from main import app


class STaskAdd(BaseModel):
    name: str
    description: str


@app.post("/")
async def add_task(task: STaskAdd):
    return {"data": task}


class STask(STaskAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)
