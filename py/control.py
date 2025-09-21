import random
import time

class Pelayan:
    def __init__(self,nama:str,umur:int,gaji:float) -> None:
        self.nama: str = nama
        self.umur: int = umur
        self.gaji: float = gaji
        self.pesanan_diantar: list[str] = []

    def ambil_pesanan(self,pesanan:str) -> None:
        print(f"{self.nama} mengambil pesanan pelanggan,info pesanan: {pesanan}")
        
    def antar_makanan(self,pesanan:str) -> None:
        self.pesanan_diantar.append(pesanan)
        print(f"{self.nama} mengantar {pesanan} ke meja pelanggan")
        self.cek_status()
    
    def cek_status(self) -> None:
        if len(self.pesanan_diantar) >= 5:
            self.status = "capek"
        else:
            self.status = "siap"
        print(f"status pelayan {self.nama}:{self.status}")

class Terminal:
    def __init__(self,pesawat:str,no_pesawat:int) -> None:
        self.kapal: str = pesawat
        self.no_kapal: int = no_pesawat
        
    def kedatangan_pesawat(self,waktu_tiba:int,tujuan:str,asal:str) -> None:
        print(f"Pesawat masuk pada pukul {waktu_tiba} / {self.check_status(waktu_tiba)}")
        print(f"asal {asal} ke {tujuan}")

    def check_status(self,waktu_tiba:int) -> str:
        if waktu_tiba < 9:
            print(f"red")
        else:
            print(f"green")
        