import io
import os
import time

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import StreamingResponse

from controller import Controller

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/src", StaticFiles(directory="src"), name="src")


@app.get('/favicon.ico')
async def favicon():
    file_name = "favicon.ico"
    file_path = os.path.join("static", file_name)
    return FileResponse(path=file_path, headers={"Content-Disposition": "attachment; filename=" + file_name})


@app.get('/src/output/code.svg')
async def preview():
    file_name = "/src/output/code.svg"
    file_path = os.path.join("src", file_name)
    return FileResponse(path=file_path, headers={"Content-Disposition": "attachment; filename=" + file_name,
                                                 "Cache-control": "no-store"})


@app.get("/")
def root(user_name=None, theme=None):
    if user_name:
        return user_names(user_name, theme)
    return FileResponse("static/templates/index.html")


def user_names(user_name, theme: str):
    time.sleep(0)
    user = Controller(user_name)
    return StreamingResponse(user.paint_svg(theme), media_type="image/svg+xml")
