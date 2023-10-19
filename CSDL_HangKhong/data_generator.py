from random import randint
from chuyenbay import *
from maybay import *
from chungnhan import *
from nhanvien import *
from datetime import time


def generate_data():
    for i in range(0, 10):
        MaCB = str(randint(1, 20))
        Ga = ["HaNoi", "Vinh", "HCM", "BangKok", "DaNang", "Paris"]
        GaDi = str(Ga[randint(0, 5)])
        GaDen = str(Ga[randint(0, 5)])
        while GaDi == GaDen:
            GaDen = str(Ga[randint(0, 5)])
        DoDai = str(randint(100, 1000))
        GioDi = str(randint(0, 23)) + ":" + str(randint(0, 59)) + ":" + str(randint(0, 59))
        GioDen = str(randint(0, 23)) + ":" + str(randint(0, 59)) + ":" + str(randint(0, 59))
        ChiPhi = str(randint(100000, 1000000))
        create_chuyenbay_data(MaCB, GaDi, GaDen, DoDai, GioDi, GioDen, ChiPhi)

    for i in range(0, 100):
        MaMB = str(randint(1, 20))
        loai = ["Boeing", "Airbus", "Atr"]
        Tambay = str(randint(1, 20))
        Manv = str(randint(1, 20))
        tennv = [
            "Nguyen Van A",
            "Nguyen Van B",
            "Nguyen Van C",
            "Nguyen Van D",
            "Nguyen Van E",
            "Nguyen Van F",
            "Nguyen Van G",
            "Nguyen Van H",
            "Nguyen Van I",
            "Nguyen Van K",
        ] 
        Luong = str(randint(1000000, 10000000))
        create_maybay_data(MaMB, loai[randint(0, 2)], Tambay)
        create_chungnhan_data(Manv, MaMB)
        create_nhanvien_data(Manv, tennv[randint(0, 9)], Luong)
