from typing import Final,Type

class particel:
    # class atribute
    konstanta_gtavitasi:Final[int] = 9.8
    dimensi_ruang:Final[int] = 3
    konstanta_gtavitasi_universal:Final[int] = 6.67* 10**(-11)
    # instance attribute
    def __init__(self,massa:int,kecepatan:int):
        self.massa: int = massa
        self.kecepatan: int = kecepatan

    # instance method
    def energi_kinetik(self) -> float:
        ek = (1/2)*self.massa*self.kecepatan**2
        return ek
    
    def energi_potensial_benda(self,ketinggian:float) -> float:
        ep = self.massa*particel.konstanta_gtavitasi*ketinggian
        return ep
    
    @classmethod
    def ubah_dimensi(cls:Type["particel"],dimensi_baru:int) -> None:
        cls.dimensi_ruang = dimensi_baru
    
    def work_particel(self) -> None:
        print(f"partikel ini bekerja pada dimensi {particel.dimensi_ruang}")

    @staticmethod
    def energi_potensial(massa_1:int,massa_2:int,jarak:int) -> float:
        k = massa_1*massa_2/jarak
        hasil = -particel.konstanta_gtavitasi_universal*k
        return hasil
    
        

     



