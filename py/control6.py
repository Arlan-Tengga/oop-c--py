import re
from typing import Final

class validasiPengguna:
    panjang_minimal_password: Final[int] = 8
    domain_perusahaan: Final[str] = "@WargaSlowy.com"

    def __init__(self,email:str,password: str) -> None:
        self.email: str = email
        self.password: str = password
        self.adalah_valid: bool = False

    def validasi_lengkap(self) -> bool:
        if not validasiPengguna.validasi_email(self.email):
            print("email enggak valid")
            return False
        if not validasiPengguna.validasi_password(self.password):
            print("password tidak mengandung huruf besar, dan juga angka")
            return False
        self.adalah_valid = True
        return True

    @staticmethod
    def validasi_email(email:str) -> bool:
        pola = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pola, email) is not None
    
    @staticmethod
    def validasi_password(password: str) -> bool:
        if len(password) < validasiPengguna.panjang_minimal_password:
            return False
        if not any(c.isupper() for c in password):
            return False
        if not any(c.isdigit() for c in password):
            return False
        return True