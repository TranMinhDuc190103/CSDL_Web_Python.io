from database import *
from pydantic import BaseModel

class NhanVien(BaseModel):
    MaNV: str
    Ten: str
    Luong: int
    # def __init(self, MaNV, Ten, Luong):
    #     self.MaNV = MaNV
    #     self.Ten = Ten
    #     self.Luong = Luong
    
def get_nhanvien(MaNV):
    try:
        if MaNV == "":
            cursor.execute("""  
                           SELECT * FROM NHANVIEN
                           """)
        else:
            cursor.execute(f"""
                           SELECT * FROM NHANVIEN WHERE MaNV = '{MaNV}'
                           """)
        result = cursor.fetchall()
        return result   
    except Exception as e:
        print(f"Error: {e}")
        
def create_nhanvien_data(item: NhanVien):
    try:
        value = (item.MaNV, item.Ten, item.Luong)
        cursor.execute(f"""
                       INSERT INTO NHANVIEN(MaNV, Ten, Luong)
                       VALUES (%s, %s, %s)
                       """, value)
        conn.commit()
        return {"message": "Data created successfully"}
    except Exception as e:
        print(f"Error: {e}")
        
def put_nhanvien_data(MaNV, item: NhanVien):
    try:
        value = (item.Ten, item.Luong, MaNV)
        cursor.execute(f"""
                       UPDATE NHANVIEN
                       SET Ten = %s, Luong = %s
                       WHERE MaNV = %s
                       """, value)
        conn.commit()
        return {"message": "Data updated successfully"}
    except Exception as e:
        print(f"Error: {e}")
        
def delete_nhanvien_data(MaNV):
    try:
        cursor.execute(f"""
                       DELETE FROM NHANVIEN
                       WHERE MaNV = '{MaNV}'
                       """)
        conn.commit()
        return {"message": "Data deleted successfully"}
    except Exception as e:
        print(f"Error: {e}")