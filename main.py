import time
from datetime import timedelta, datetime

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import Response

from controller import Controller

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root(user_name=None, theme=None):
    if user_name:
        return user_names(user_name, theme)
    return FileResponse("static/templates/index.html")


def user_names(user_name, theme: str):
    time.sleep(0)
    user = Controller(user_name)
    modified_past = datetime.now() + timedelta(minutes=180)
    max_age = 3 * 60 * 60
    modified_per = datetime.now()
    modif_past = modified_past.strftime('%a, %d %b %Y %H:%M:%S GMT')
    modif_per = modified_per.strftime('%a, %d %b %Y %H:%M:%S GMT')
    repl = user.paint_svg(theme).replace('"', "'")
    print(repl)
    return Response(repl, media_type="image/svg+xml",
                    headers={"Expires": f"{modif_past}", "Last-Modified": f"{modif_per}",
                             "Cache-control": f"max-age={max_age}"}
                    )
