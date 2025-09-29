# inheritance
# kelas turunan dari variabel sebelumnya

# inheritance
class Kendaraan:
    def __init__(self,merek: str,kecepatan_maks:int) -> None:
        self.merek: str = merek
        self.kecepatan_maks: int = kecepatan_maks
        self._sedang_berjalan: bool = False
    
    def mulai(self) -> None:
        self._sedang_berjalan = True
        print(f"{self.merek} telah dinyalakan")
    
    def berhenti(self) -> None:
        self._sedang_berjalan = False
        print(f"{self.merek} berhenti")

# penggunaan super().__init__() ini menandakann bahwa class itu merupakan sebuah turunan

class Mobil(Kendaraan):
    def __init__(self, merek:str, kecepatan_maks:int,jumlah_pintu:int) -> None:
        super().__init__(merek, kecepatan_maks)
        self.jumlah_pintu: int = jumlah_pintu

    def  klakson(self) -> None:
        print(f"{self.merek} membunyikan klakson: slebeww")

class Motor(Kendaraan):
    def __init__(self, merek:str, kecepatan_maks:int,jenis_helm:str):
        super().__init__(merek, kecepatan_maks)
        self.jenis_helm: str = jenis_helm
    
    def wheelie(self) -> None:
        if self._sedang_berjalan:
            print(f"{self.merek} melakuka wheelie")
        else:
            print("nyalakan dahulu dari si motornya")

# multi inheritence(dihendari)

class Penyihir:
    def lempar_mantra(self) -> None:
        print("melempatt mantra: reducto!")

class Petarung:
    def serang(self) -> None:
        print("menyerang dengan kekuatan pedang ksatria")

class PenyihirPetarung(Penyihir,Petarung):
    def gunakan_kekuatan_multi(self) -> None:
        self.lempar_mantra()
        self.serang()
        print("kombinasi double: lempar serangan khas boyolali")