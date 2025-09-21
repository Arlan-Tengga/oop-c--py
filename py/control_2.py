# class and atribut
from typing import Final

# Final itu sebuah konstanta
# Kalo data yang sering berubah jangan gunakan data attribut

class Restoran:
    # bersifat global
    nama_perusahaan:Final[str] = "burger warga slowy"
    pajak_nasional: Final[float] = 0.10
    daftar_menu_utama: Final[list[str]] = [
        "burger warga slowy ayam","burger rarek sapi","kentang goreng khas ngawi","es teh boyolali"
    ]

    def __init__(self,nama_cabang: str,alamat: str,jumlah_karyawan: int) -> None:
        self.nama_cabang: str = nama_cabang
        self.alamat: str = alamat
        self.jumlah_karyawan: int = jumlah_karyawan
        self.pendapatan_bulanan: float = 0.0
        self.menu_cabang: list[str] = Restoran.daftar_menu_utama.copy()

    def ubah_menu_cabang(self,menu_baru: list[str]) -> None:
        self.menu_cabang = menu_baru
        print(f"menu {self.nama_cabang} diubah menjadi: {', '.join(menu_baru)}")

    def tambah_pendapatan(self,jumlah:float) -> None:
        pendapatan_setelah_pajak = jumlah * (1 - Restoran.pajak_nasional)
        self.pendapatan_bulanan += pendapatan_setelah_pajak

    def info_restoran(self) -> None:
        print(f"info restoran")
        print(f"perusahaan :    {Restoran.nama_perusahaan}")
        print(f"cabang :        {self.nama_cabang}")
        print(f"alamat :        {self.alamat}")
        print(f"menu   :        {','.join(self.menu_cabang)}")
        print(f"pendapatan :    Rp{self.pendapatan_bulanan:.0f}")
        print(f"pajak  :        {Restoran.pajak_nasional*100:.0f} % ")
        