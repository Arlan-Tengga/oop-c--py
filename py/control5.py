# class method
from typing import Final,Type
from datetime import datetime

class Karyawan:
    # class attribute
    perusahaan: Final[str] = "WargaSlowlyTech"
    tingkat_inflasi: Final[float] = 0.05
    # list untuk semua objek yang sudah dibuat
    semua_karyawan: list["Karyawan"] = []

    # konsuktor 
    # instance method
    # instance method menggunakan self
    def __init__(self,nama:str,posisi:str,gaji_bulanan:float,tahun_masuk:int) -> None:
        self.nama: str = nama
        self.posisi: str = posisi
        self.gaji_bulanan: float = gaji_bulanan
        self.tahun_masuk: int = tahun_masuk

        Karyawan.semua_karyawan.append(self)    
    
    # alternative constructor
    @classmethod
    def dari_gaji_tahunan(cls:Type["Karyawan"],nama:str,posisi:str,gaji_tahunan:float,tahun_masuk:int) -> "Karyawan":
        gaji_bulanan = gaji_tahunan /12
        return cls(nama,posisi,gaji_bulanan,tahun_masuk)
    
    @classmethod
    def hitung_rata_rata_gaji(cls: Type["Karyawan"]) -> float:
        if not cls.semua_karyawan:
            return 0.0
        total = sum(k.gaji_bulanan for k in cls.semua_karyawan)
        return total / len(cls.semua_karyawan)
    
    @classmethod
    def hitung_gaji_5_tahun(cls: Type["Karyawan"]) -> float:
        if not cls.semua_karyawan:
            return 0.0
        # total = k.gaji_bulanan for k in cls.semua_karyawan


    def ingpo_karyawan(self) -> None:
        lama_kerja = datetime.now().year - self.tahun_masuk
        print(f"nama : {self.nama}")
        print(f"posisi : {self.posisi}")
        print(f"gaji : {self.gaji_bulanan:.0f} / bulan")
        print(f"lama kerja: {lama_kerja} tahun")
        print(f"perusahaan: {Karyawan.perusahaan}")
    