
from main import app


@app.post("/")
async def add_task(task: STaskAdd):
    return {"data": task}

