from database import *
from pydantic import BaseModel
from datetime import time


class ChuyenBay(BaseModel):
    MaCB: str
    GaDi: str
    GaDen: str
    DoDai: int
    GioDi: str
    GioDen: str
    ChiPhi: int

    # def __init__(self, MaCB, GaDi, GaDen, DoDai, GioDi, GioDen, ChiPhi):
    #     self.MaCB = MaCB
    #     self.GaDi = GaDi
    #     self.GaDen = GaDen
    #     self.DoDai = DoDai
    #     self.GioDi = GioDi
    #     self.GioDen = GioDen
    #     self.ChiPhi = ChiPhi


def get_chuyenbay(MaCB):
    try:
        if MaCB == "":
            cursor.execute(
                """
                SELECT * FROM CHUYENBAY
                """
            )
        else:
            cursor.execute(
                f"""
                SELECT * FROM CHUYENBAY WHERE MaCB = '{MaCB}'
                """
            )
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"Error: {e}")


def create_chuyenbay_data(item: ChuyenBay):
    try:
        value = (item.MaCB, item.GaDi, item.GaDen, item.DoDai, item.GioDi, item.GioDen, item.ChiPhi)
        cursor.execute("""INSERT INTO CHUYENBAY VALUES (%s, %s, %s, %s, %s, %s, %s)""",value)
        conn.commit()
        return {"message": "Data created successfully"}
    except Exception as e:
        print(f"Error: {e}")


def put_chuyenbay_data(MaCB, item: ChuyenBay):
    try:
        value = (item.GaDi, item.GaDen, item.DoDai, item.GioDi, item.GioDen, item.ChiPhi, MaCB)
        cursor.execute(
            """UPDATE CHUYENBAY SET GaDi = %s, GaDen = %s, DoDai = %s, GioDi = %s, GioDen = %s, ChiPhi = %s WHERE MaCB = %s""", value
        )
        conn.commit()
        return {"message": "Data updated successfully"}
    except Exception as e:
        print(f"Error: {e}")

def delete_chuyenbay_data(MaCB):
    try:
        cursor.execute(f"""DELETE FROM CHUYENBAY WHERE MaCB = '{MaCB}'""")
        conn.commit()
        return {"message": "Data deleted successfully"}
    except Exception as e:
        print(f"Error: {e}")