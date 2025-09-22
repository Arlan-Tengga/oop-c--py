from typing import Final
# Case 1 (Fisika): Gravitasi Planet
# name,radius,mass
# *
# class attribute: G (konstanta Gravitasi)
# insatnca attribute: nama,mass,jari_jari
# Method : gravitasi_permukaa()
# Buat objek Bumi dan Mars, lalu bandingkan gravitasi permukaannya.
# 
# * #


# *
# case 2 Perustakaan
# class attribute: kategori_umum = "Literasi"
#                  (kategori besar, sama untuk semua buku).
# Instance attribute: judul, penulis, tahun
# Method: info_buku() → cetak detail buku.
# 
# Latihan: Buat 2 buku berbeda dan tampilkan informasinya
# *#


class planet:
    constant_gravitation:Final[int] = 6.67 * 10**-11
    mass_earth:Final[int] = 5.67 * 10**24
    mass_mars:Final[int] = 6.42 * 10**23
    def __init__(self,name:str,radius:int,mass:int) -> None:
        self.name: str = name
        self.radius: int = radius
        self.mass: int = mass

    def gravitasi_permukaan(self) -> int:
        self.gravitas = planet.constant_gravitation*self.mass / self.radius**2
        print(self.gravitas)
    
    def gaya_grafitasi(self,planet_name:str) -> int:
        if(planet_name == "earth"):
            self.gravitas_force = planet.constant_gravitation*planet.mass_earth*self.mass / self.radius**2
        elif(planet_name == "mars"):
            self.gravitas_force = planet.constant_gravitation*planet.mass_mars*self.mass / self.radius**2
        print(self.gravitas_force)
    
    def potensial_gravitasi(self) -> int:
        self.potetial_result = -planet.constant_gravitation*planet.mass_earth*self.mass / self.radius
        print(self.potetial_result)
    

class Perpustakaan:
    kategori_umum:Final[str] = "Perpustakaan RI"
    daftar_buku_perpus:Final[list[str]] = [
        "Matematical Pyhsics","Haliday Physics","Calculus","Mary L Boas"
    ]

    # Instance attribute: judul, penulis, tahun

    # mendefinisikan struktrur data
    def __init__(self,judul:str,penulis:str,tahun:int) -> None:
        self.judul: str = judul
        self.penulis: str = penulis
        self.tahun: int = tahun
        self.daftar_buku: list[int] = Perpustakaan.daftar_buku_perpus.copy()

    def info_perpustakaa(self) -> None:
        print(f"info perpustakaan")
        print(f"Perpustakaan : {Perpustakaan.kategori_umum}")
        print(f"daftar buku : {self.daftar_buku}")
        

