from control import *
from control_2 import *
from tugas_gpt import *
from contro4_ import *
from control5 import *

# membuat branch
# git branch <nama_brach>

# untuk pindah ke branch git checkout <nama_brach>
# git merge <nama_brach>


# menghapus branch git branch -d<nama_brach>

# untuk melihat branch apa aja yang di brach
# git branch --merged

# test
# test_1
if __name__ == "__main__":
    # Perpustakaan_uny = Perpustakaan("mary L boas","mary L boas",2022)

    # Perpustakaan_uny.info_perpustakaa()

    # angka = coba_git(5)
    # angka.kalikan_angka()

    karyawan_pertama = Karyawan.dari_gaji_tahunan("arfy","backend",120_000,2020)
    
    karyawan_pertama.ingpo_karyawan()

    rata_rata_gaji = Karyawan.hitung_rata_rata_gaji()
    print(f"rata rata gaji dari karyawan {Karyawan.perusahaan} adalah : {rata_rata_gaji:0f} / bulan")
    


    


# *
# case 2 Perustakaan
# class attribute: kategori_umum = "Literasi"
#                  (kategori besar, sama untuk semua buku).
# Instance attribute: judul, penulis, tahun
# Method: info_buku() → cetak detail buku.
# 
# Latihan: Buat 2 buku berbeda dan tampilkan informasinya
# *#



#     Pelayan_arfy = Pelayan("Skylar",40,8.7)
#     Pelayan_nopal = Pelayan("Alex",21,5.6)

#     # Pelayan_arfy.ambil_pesanan("nasi Goreng")
#     print("\n")
# #     Pelayan_arfy.antar_makanan("nasi Goreng")
#     Pesawat = Terminal("Garuda",10)

#     Pesawat.kedatangan_pesawat(10,"amerika","indonesia")

    # resto_aceh = Restoran("Burger Cekcok - Aceh","jln tjuk nyak dhien",20)
    # resto_bandung = Restoran("Burger AWKWOKWOKWO - Bandung","jln perintis",10)

    # resto_aceh.ubah_menu_cabang(["air jahe","mie aceh"])

    # resto_aceh.tambah_pendapatan(14_000_000)
    # resto_bandung.tambah_pendapatan(14_500_000)

    # resto_aceh.info_restoran()
    # print()
    # print(50*"=")
    # print()
    # resto_bandung.info_restoran()
    


