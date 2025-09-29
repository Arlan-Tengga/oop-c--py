# polimorfisme
# satu aksi tapi bisa di lakukan banyak cara
from typing import Protocol


class MetodePembayaran(Protocol):
    def bayar(self,jumlah:float) -> None:
        ...

class PembayaranTunai:
    def bayar(self,jumlah:float) -> None:
        print(f"bayar dengan tunai jumlah: Rp {jumlah:0f}")

class PembayaranEWallet:
    def bayar(self,jumlah: float) -> None:
        print(f"bayar dengan ewallet : Rp{jumlah:.2f} (Qr terbaca - saldo gas)")

class PembayaranKartu:
    def bayar(self,jumlah: float) -> None:
        print(f"bayar dengan kartu (otorisasi): Rp {jumlah} (berhasil..!)")

def proses_bayar(metode:MetodePembayaran,jumlah:float) -> None:
    metode.bayar(jumlah)

