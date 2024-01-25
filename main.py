import os
import time

from CodeWars import CodeWars

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

# TODO: исправить ошибки рисования


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
    test = CodeWars(f'{user_name}')
    test.parse()
    print(test)
    test.draw()
    del test
    return FileResponse('./src/output/canvas.png')
