import os
import time

from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from controller import Controller

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/src", StaticFiles(directory="src"), name="output")


@app.get('/favicon.ico')
async def favicon():
    file_name = "favicon.ico"
    file_path = os.path.join("static", file_name)
    return FileResponse(path=file_path, headers={"Content-Disposition": "attachment; filename=" + file_name})


@app.get('/src/output/canvas.png')
async def preview():
    file_name = "/src/output/canvas.png"
    file_path = os.path.join("output", file_name)
    return FileResponse(path=file_path, headers={"Content-Disposition": "attachment; filename=" + file_name})


# @app.post("/postdata/")
# def postdata(user_name=Form()):
#     return RedirectResponse(f"/name/{user_name}/", status_code=302)


# @app.get("/users")
# def get_model(name, age):
#     return {"user_name": name, "user_age": age}


@app.get("/")
def root(user_name=None, color=None):
    if user_name:
        return user_names(user_name, color)
    return FileResponse("static/templates/index.html")


def user_names(user_name: str, color):
    time.sleep(2)
    user = Controller(user_name)
    user.items(color)
    user.paint()
    return FileResponse('./src/output/canvas.png')
