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

    def __init__(self, MaCB, GaDi, GaDen, DoDai, GioDi, GioDen, ChiPhi):
        self.MaCB = MaCB
        self.GaDi = GaDi
        self.GaDen = GaDen
        self.DoDai = DoDai
        self.GioDi = GioDi
        self.GioDen = GioDen
        self.ChiPhi = ChiPhi


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
        add_chuyenbay = """INSERT INTO CHUYENBAY VALUES ('{item.MaCB}', '{item.GaDi}', '{item.GaDen}', {item.DoDai}, '{item.GioDi}', '{item.GioDen}', {item.ChiPhi})"""
        cursor.execute(add_chuyenbay, item.model_dump())
        conn.commit()
        return {"message": "Data created successfully"}
    except Exception as e:
        print(f"Error: {e}")


def put_chuyenbay_data(MaCB, item: ChuyenBay):
    cursor.execute(
        f"""UPDATE CHUYENBAY SET GaDi = '{item.GaDi}', GaDen = '{item.GaDen}', DoDai = {item.DoDai}, GioDi = '{item.GioDi}', GioDen = '{item.GioDen}', ChiPhi = {item.ChiPhi} WHERE MaCB = '{MaCB}'"""
    )
    conn.commit()
    return {"message": "Data updated successfully"}


def delete_chuyenbay_data(MaCB):
    cursor.execute(f"""DELETE FROM CHUYENBAY WHERE MaCB = '{MaCB}'""")
    conn.commit()
    return {"message": "Data deleted successfully"}
