from database import *
from pydantic import BaseModel

class ChungNhan(BaseModel):
    MaNV: str
    MaMB: int
    def __init__(self, MaNV, MaMB):
        self.MaNV = MaNV
        self.MaMB = MaMB
    
def get_chungnhan(MaNV):
    try:
        if MaNV == "":
            cursor.execute("""
                           SELECT * FROM CHUNGNHAN
                           """)
        else: 
            cursor.execute(f"""
                           SELECT * FROM CHUNGNHAN WHERE MaNV = '{MaNV}'
                           """)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"Error: {e}")
        
def create_chungnhan_data(item: ChungNhan):
    try:
        cursor.execute(f"""
                       INSERT INTO CHUNGNHAN(MaNV, MaMB)
                       VALUES ('{item.MaNV}', '{item.MaMB}')
                       """)
        conn.commit()
        return {"message": "Data created successfully"}
    except Exception as e:
        print(f"Error: {e}")
        
def put_chungnhan_data(MaNV, item: ChungNhan):
    try:
        cursor.execute(f"""
                    UPDATE CHUNGNHAN
                    SET MaMB = '{item.MaMB}'
                    WHERE MaNV = '{MaNV}'
                    """)
        conn.commit()
        return {"message": "Data updated successfully"}
    except Exception as e:
        print(f"Error: {e}")
        
def delete_chungnhan_data(MaNV):
    try:
        cursor.execute(f"""
                       DELETE FROM CHUNGNHAN
                       WHERE MaNV = '{MaNV}'
                       """)
        conn.commit()
        return {"message": "Data deleted successfully"}
    except Exception as e:
        print(f"Error: {e}")