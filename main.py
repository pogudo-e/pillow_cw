from CodeWars import CodeWars

from fastapi import FastAPI
from fastapi.responses import FileResponse

# TODO: исправить ошибки рисования


app = FastAPI()


@app.get("/{user_name}")
def root(user_name: str):
    test = CodeWars(f'{user_name}')
    test.parse()
    print(test)
    test.draw()
    return FileResponse('./src/output/canvas.png')
