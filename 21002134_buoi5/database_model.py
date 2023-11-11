from pydantic import BaseModel
from datetime import datetime

NHANVIEN_COLUMNS = ("Họ nhân viên", "Tên Lót", "Tên nhân viên", "Mã NV", "Ngày sinh", "Địa chỉ", "Giới tính", "Lương", "Mã NQL", "Phòng")
CONGVIEC_COLUMNS = ("Mã đề án", "Số thứ tự", "Tên công việc")
DEAN_COLUMNS = ("Tên đề án", "Mã đề án", "Địa điểm đề án", "Phòng")
DIADIEMPHG_COLUMNS = ("Mã phòng", "Địa điểm")
PHANCONG_COLUMNS = ("Mã nhân viên", "Mã đề án", "Số thứ tự", "Thời gian")
PHONGBAN_COLUMNS = ("Tên phòng", "Mã phòng", "Trưởng phòng", "Ngày nhận chức")
THANNHAN_COLUMNS = ("Mã nhân viên", "Tên thân nhân", "Ngày sinh", "Phái", "Quan hệ")

class nhanvien(BaseModel):
    HoNV: str
    TenLot: str
    TenNV: str
    MaNV: str
    NgSinh: datetime
    DChi: str
    Phai: str
    Luong: int
    MaNQL: int
    Phg: int
    
class congviec(BaseModel):
    MaDA: int
    Stt: int
    TenCongViec: str

class dean(BaseModel):
    TenDA: str
    MaDA: int
    DDiemDA: str
    Phong: int
    
class diadiemphg(BaseModel):
    MaPhg: int
    DiaDiem: str

class phancong(BaseModel):
    MaNV: str
    MaDA: int
    Stt: int
    ThoiGian: float
    
class phongban(BaseModel):
    TenPhg: int
    MaPhg: int
    TrPhg: str
    NgNhanChuc: datetime
    
class thannhan(BaseModel):
    MaNV: str
    TenTN: str
    NgSinh: datetime
    Phai: str
    Quanhe: str