from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database import *
from database_model import *

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_nhanvien(request: Request):
    cursor.execute(f"SELECT * FROM nhanvien")
    data = cursor.fetchall()
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/process", response_class=HTMLResponse)
async def post_func(request: Request):
    choice_data = await request.form()
    choice = choice_data.get("choice")
    result = ""
    match choice:
        case GET:
            cursor.execute(f"SELECT * FROM NHANVIEN")
        case POST:
            
        case UPDATE:
            
        case DELETE:
            
        case _:
            pass
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=3306)