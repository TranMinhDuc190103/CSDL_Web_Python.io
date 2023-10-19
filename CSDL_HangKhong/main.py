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
async def create_chuyenbay(MaCB: str,GaDi: str,GaDen: str,DoDai: int,GioDi: str,GioDen: str,ChiPhi: int):
    return create_chuyenbay_data(ChuyenBay(MaCB,GaDi,GaDen,DoDai,GioDi,GioDen,ChiPhi))

@app.put("/chuyenbay/{MaCB}")
async def put_chuyenbay(MaCB: str,GaDi: str,GaDen: str,DoDai: int,GioDi: str,GioDen: str,ChiPhi: int):
    return put_chuyenbay_data(MaCB,ChuyenBay(MaCB, GaDi,GaDen,GioDi,DoDai,GioDen,ChiPhi))

@app.delete("/chuyenbay/{MaCB}")
async def delete_chuyenbay(MaCB: str):
    return delete_chuyenbay_data(MaCB)

#API May bay
@app.get("/maybay/{MaMB}")
async def maybay(MaMB):
    return get_maybay(MaMB)

@app.post("/maybay/input")
async def create_maybay(MaMB: int,Loai: str,TamBay: int):
    return create_maybay_data(MayBay(MaMB,Loai,TamBay))

@app.put("/maybay/{MaMB}")
async def put_maybay(MaMB: int,Loai: str,TamBay: int):
    return put_maybay_data(MaMB,MayBay(MaMB,Loai,TamBay))

@app.delete("/maybay/{MaMB}")
async def delete_maybay(MaMB):
    return delete_maybay_data(MaMB)

#API Nhan vien
@app.get("/nhanvien/{MaNV}")
async def nhanvien(MaNV):
    return get_nhanvien(MaNV)

@app.post("/nhanvien/input")
async def create_nhanvien(MaNV: str,Ten: str,Luong: int):
    return create_nhanvien_data(NhanVien(MaNV,Ten,Luong))

@app.put("/nhanvien/{MaNV}")
async def put_nhanvien(MaNV: str,Ten: str,Luong: int):
    return put_nhanvien_data(MaNV,NhanVien(MaNV, Ten,Luong))

@app.delete("/nhanvien/{MaNV}")
async def delete_nhanvien(MaNV):
    return delete_nhanvien_data(MaNV)

@app.get("/chungnhan/{MaNV}")
async def chungnhan(MaNV):
    return get_chungnhan(MaNV)

@app.post("/chungnhan/input")
async def create_chungnhan(MaNV: str,MaMB: int):
    return create_chungnhan_data(ChungNhan(MaNV,MaMB))

@app.put("/chungnhan/{MaNV}")
async def put_chungnhan(MaNV: str,MaMB: int):
    return put_chungnhan_data(MaNV,ChungNhan(MaNV, MaMB))

@app.delete("/chungnhan/{MaNV}")
async def delete_chungnhan(MaNV):
    return delete_chungnhan_data(MaNV)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=3306)
    # generate_data()