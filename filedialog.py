import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(200, 200)

        self.btn = QPushButton("Open Files", self)
        self.btn.move(40, 40)
        self.btn.clicked.connect(self.evt_btn_clicked)

        self.btn1 = QPushButton("Open File", self)
        self.btn1.move(40, 70)
        self.btn1.clicked.connect(self.evt_btn1_clicked)

        self.btn2 = QPushButton("Save File", self)
        self.btn2.move(40, 100)
        self.btn2.clicked.connect(self.evt_btn2_clicked)

    def evt_btn_clicked(self):
        res = QFileDialog.getOpenFileNames(
            self, "Open Files", "/Users", "JPG File (*.jpg);;PNG Files (*.png)")
        print(res)

    def evt_btn1_clicked(self):
        res = QFileDialog.getSaveFileName(
            self, "Open File", "/Users", "JPG File (*.jpg);;PNG Files (*.png)")
        print(res)

    def evt_btn2_clicked(self):
        res = QFileDialog.getSaveFileName(
            self, "Save File", "/Users", "JPG File (*.jpg);;PNG Files (*.png)")
        print(res)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
