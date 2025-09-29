import sys
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,QLabel
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtCore import Qt
from random import choice

class AplikasiSederhana(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.inisialisai_interface()

    def inisialisai_interface(self) -> None:
        # ini title windows
        # self.setGeometry(x = posisi,y = posisi ,ukuran x ,ukuran y)
        self.setWindowTitle("Contoh kode dengan pyqt6")
        # self.setGeometry(x=muncul,y_muncul,lebar,tinggi(dalam bentuk pixel))
        self.setGeometry(120,320,300,300)

        # label
        self.label_sambutan: QLabel = QLabel("ini label")
        self.label_sambutan.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_sambutan.setStyleSheet(
            """
            font-size: 24px;
            font-weight: bold;
            color: #2c3e50;
            background-color: #ecf0f1;
            padding: 15px;
            border-radius: 10px
                                      
        """)
        self.label_kedua: QLabel = QLabel("label pengguna")
        self.label_kedua.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_kedua.setStyleSheet(
            """
            font-size: 25px;
            font-weight: bold;
        """)


        # membuat sebuah tombol
        self.tombol: QPushButton = QPushButton("Tombol")
        self.tombol_2: QPushButton = QPushButton("tombol 2")

        self.tombol_3: QPushButton = QPushButton("Tombol 3")
        self.tombol_3.setStyleSheet(
            """
        font-size: 16px;
        background-color: #3498db;
        border-radius: 8px

        """
        )

        # memberikan sinyal
        self.tombol.clicked.connect(self.saat_tombol_ditekan)
        self.tombol_2.clicked.connect(self.tombo_di_tekan)
        self.tombol_3.clicked.connect(self.tombol_nama)

        # taruh di layout
        self.layout_utama: QVBoxLayout = QVBoxLayout()
        self.layout_utama.addWidget(self.tombol)
        self.layout_utama.addWidget(self.tombol_2)
        self.layout_utama.addWidget(self.label_sambutan)
        self.layout_utama.addWidget(self.label_kedua)
        self.layout_utama.addWidget(self.tombol_3)
    

        self.setLayout(self.layout_utama)

    # menerima sinyal dan menjalankan terminal
    @pyqtSlot()
    def saat_tombol_ditekan(self) -> None:
        print("ini tampil di dalma terminal")

    @pyqtSlot()
    def tombo_di_tekan(self) -> None:
        print("wookwokw")

    @pyqtSlot()
    def tombol_nama(self) -> None:
        nama: list[str] = [
            "amba",
            "arief",
            "arfy",
            "nongpal",
            "mamad",
            "mochie",
            "vinx",
        ]
        self.layout_utama.setText(choice(nama))    
        print("label diganti!")

if __name__ == "__main__":
    aplikasi: QApplication = QApplication(sys.argv)

    jendela_utama: AplikasiSederhana = AplikasiSederhana()
    jendela_utama.show()

    sys.exit(aplikasi.exec())