
from main import app, STaskAdd


@app.post("/")
async def add_task(task: STaskAdd):
    return {"data": task}

