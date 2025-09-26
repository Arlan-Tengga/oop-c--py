import sys
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout
from PyQt6.QtCore import pyqtSlot

class AplikasiSederhana(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.inisialisai_interface()

    def inisialisai_interface(self) -> None:
        # ini title windows
        self.setWindowTitle("Contoh kode dengan pyqt6")

        # set ukuran
        self.setGeometry(300,300,400,200)
        self.tombol: QPushButton = QPushButton("Tombol")

        # memberikan sinyal
        self.tombol.clicked.connect(self.saat_tombol_ditekan)

        self.layout_utama: QVBoxLayout = QVBoxLayout()
        self.layout_utama.addWidget(self.tombol)

        self.setLayout(self.layout_utama)

    # menerima sinyal dan menjalankan terminal
    @pyqtSlot()
    def saat_tombol_ditekan(self) -> None:
        print("ini tampil di dalma terminal")

if __name__ == "__main__":
    aplikasi: QApplication = QApplication(sys.argv)

    jendela_utama: AplikasiSederhana = AplikasiSederhana()
    jendela_utama.show()

    sys.exit(aplikasi.exec())