from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database import *
from database_model import *

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse("request.html", {"request": request})

@app.post("/query", response_class=HTMLResponse)
async def get_query(request: Request):
    query = await request.form()
    cursor.execute(query)
    result = cursor.fetchall()
    # column_dict = {
    #     "NHANVIEN": NHANVIEN_COLUMNS,
    #     "CONGVIEC": CONGVIEC_COLUMNS,
    #     "PHONGBAN": PHONGBAN_COLUMNS,
    #     "PHANCONG": PHANCONG_COLUMNS,
    #     "DEAN": DEAN_COLUMNS,
    #     "THANNHAN": THANNHAN_COLUMNS,
    #     "DIADIEM_PHG": DIADIEMPHG_COLUMNS
    # }
    if "NHANVIEN" in query:
        columns = NHANVIEN_COLUMNS
    elif "CONGVIEC" in query:
        columns = CONGVIEC_COLUMNS
    elif "PHONGBAN" in query:
        columns = PHONGBAN_COLUMNS
    elif "PHANCONG" in query:
        columns = PHANCONG_COLUMNS
    elif "DEAN" in query:
        columns = DEAN_COLUMNS
    elif "THANNHAN" in query:
        columns = THANNHAN_COLUMNS
    elif "DIADIEM_PHG" in query:
        columns = DIADIEMPHG_COLUMNS
    return templates.TemplateResponse("result.html", {"request": request, "result": result, "columns": columns})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=3306)