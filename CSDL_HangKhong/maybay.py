from database import *
from pydantic import BaseModel

class MayBay(BaseModel):
    MaMB: int
    Hieu: str
    TamBay: int
    def __init__(self, MaMB, Hieu, TamBay):
        self.MaMB = MaMB
        self.Hieu = Hieu
        self.TamBay = TamBay
    
def get_maybay(MaMB):
    try:
        if MaMB == None:
            cursor.execute("""  
                           SELECT * FROM MAYBAY
                           """)
        else:
            cursor.execute(f"""
                           SELECT * FROM MAYBAY WHERE MaMB = '{MaMB}'
                           """)
        result = cursor.fetchall()
        return result   
    except Exception as e:
        print(f"Error: {e}")
        
def create_maybay_data(item: MayBay):
    try:
        cursor.execute(f"""
            INSERT INTO MAYBAY(MaMB, Hieu, TamBay)
            VALUES ('{item.MaMB}', '{item.Hieu}', {item.TamBay})
            """)    
        conn.commit()
        return {"message": "Data created successfully"}
    except Exception as e:
        print(f"Error: {e}")
        
def put_maybay_data(MaMB, item: MayBay):
    try:
        cursor.execute(f"""
            UPDATE MAYBAY
            SET Hieu = '{item.Hieu}', TamBay = '{item.TamBay}'
            WHERE MaMB = '{MaMB}'
            """)
        conn.commit()
        return {"message": "Data updated successfully"}
    except Exception as e:
        print(f"Error: {e}")

def delete_maybay_data(MaMB):
    try:
        cursor.execute(f"""
                       DELETE FROM MAYBAY
                       WHERE MaMB = '{MaMB}'
                       """)
        conn.commit()
        return {"message": "Data deleted successfully"}
    except Exception as e:
        print(f"Error: {e}")