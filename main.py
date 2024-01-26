import os
import time

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from controller import Controller

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/favicon.ico')
async def favicon():
    file_name = "favicon.ico"
    file_path = os.path.join("static", file_name)
    return FileResponse(path=file_path, headers={"Content-Disposition": "attachment; filename=" + file_name})


@app.get("/name/{user_name}")
def root(user_name: str):
    time.sleep(2)
    user = Controller(user_name)
    user.paint()
    return FileResponse('./src/output/canvas.png')
