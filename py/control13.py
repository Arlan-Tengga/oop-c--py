# inner class
# seperti chip prosessor pada smartphone

class Smartphone:
    def __init__(self,merek:str,model:str) -> None:
        self.merek: str = merek
        self.model: str = model
        self.baterai: int = 100

    class __Prosesor:
        def __init__(self) -> None:
            self.nama = "snapslowy 8 gen 20"
            self.inti_cpu: int = 70
            self.kecepatan_ghz: float = 400.20

        def jalankan_simulasi(self) -> None:
            print(f"menjalankan sistem dengan {self.nama}")

        def tampilin_info(self) -> None:
            print(f"info chip: {self.nama}")
        
        de