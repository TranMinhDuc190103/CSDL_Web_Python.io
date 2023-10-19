from chuyenbay import *
from maybay import *
from nhanvien import *
from chungnhan import *
from database import *
from fastapi import FastAPI
from data_generator import *

app = FastAPI()

try:
    cursor.execute ("""
            CREATE TABLE IF NOT EXISTS CHUYENBAY (
                MaCB CHAR(5) PRIMARY KEY,
                GaDi VARCHAR(50),
                GaDen VARCHAR(50),
                DoDai INT,
                GioDi TIME,
                GioDen TIME,
                ChiPhi INT
            )
        """)

    cursor.execute ("""
            CREATE TABLE IF NOT EXISTS MAYBAY (
                MaMB INT PRIMARY KEY,
                Hieu VARCHAR(50),
                TamBay INT
            )
        """)

    cursor.execute ("""
            CREATE TABLE IF NOT EXISTS NHANVIEN (
                MaNV CHAR(9) PRIMARY KEY,
                Ten VARCHAR(50),
                Luong INT
            )
        """)

    cursor.execute ("""
            CREATE TABLE IF NOT EXISTS CHUNGNHAN (
                MaNV CHAR(9),
                MaMB INT,
                FOREIGN KEY (MaNV) REFERENCES NHANVIEN (MaNV),
                FOREIGN KEY (MaMB) REFERENCES MAYBAY (MaMB)
            )
        """)
except Exception as e:
    print(f"Error: {e}")

@app.get("/")
async def root():
    return {"message": "Hello World"}

#API Chuyen bay
@app.get("/chuyenbay/{MaCB}")
async def chuyenbay(MaCB):
    return get_chuyenbay(MaCB)

@app.post("/chuyenbay/input")
async def create_chuyenbay(item: ChuyenBay):
    return create_chuyenbay_data(item)

@app.put("/chuyenbay/{MaCB}")
async def put_chuyenbay(MaCB, item: ChuyenBay):
    return put_chuyenbay_data(MaCB, item)

@app.delete("/chuyenbay/{MaCB}")
async def delete_chuyenbay(MaCB):
    return delete_chuyenbay_data(MaCB)

#API May bay
@app.get("/maybay/{MaMB}")
async def maybay(MaMB):
    return get_maybay(MaMB)

@app.post("/maybay/input")
async def create_maybay(item: MayBay):
    return create_maybay_data(item)

@app.put("/maybay/{MaMB}")
async def put_maybay(MaMB, item: MayBay):
    return put_maybay_data(MaMB, item)

@app.delete("/maybay/{MaMB}")
async def delete_maybay(MaMB):
    return delete_maybay_data(MaMB)

#API Nhan vien
@app.get("/nhanvien/{MaNV}")
async def nhanvien(MaNV):
    return get_nhanvien(MaNV)

@app.post("/nhanvien/input")
async def create_nhanvien(item: NhanVien):
    return create_nhanvien_data(item)

@app.put("/nhanvien/{MaNV}")
async def put_nhanvien(MaNV, item: NhanVien):
    return put_nhanvien_data(MaNV, item)

@app.delete("/nhanvien/{MaNV}")
async def delete_nhanvien(MaNV):
    return delete_nhanvien_data(MaNV)

@app.get("/chungnhan/{MaNV}")
async def chungnhan(MaNV):
    return get_chungnhan(MaNV)

@app.post("/chungnhan/input")
async def create_chungnhan(item: ChungNhan):
    return create_chungnhan_data(item)

@app.put("/chungnhan/{MaNV}")
async def put_chungnhan(MaNV, item: ChungNhan):
    return put_chungnhan_data(MaNV, item)

@app.delete("/chungnhan/{MaNV}")
async def delete_chungnhan(MaNV):
    return delete_chungnhan_data(MaNV)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=3306)