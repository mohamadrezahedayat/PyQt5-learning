import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(200, 200)

        self.btn = QPushButton("Show Input", self)
        self.btn.move(40, 40)
        self.btn.clicked.connect(self.evt_btn2_clicked)

        self.btn2 = QPushButton("Show Input", self)
        self.btn2.move(40, 70)
        self.btn2.clicked.connect(self.evt_btn2_clicked)

        self.btn3 = QPushButton("Show Input", self)
        self.btn3.move(40, 100)
        self.btn3.clicked.connect(self.evt_btn3_clicked)

    def evt_btn_clicked(self):
        sName, bOk = QInputDialog.getText(self, "Text", "Enter Your Name:")
        if bOk:
            QMessageBox.information(self, "Name", f"Your name is {sName}")
        else:
            QMessageBox.critical(self, "Canceled", "User canceled")

    def evt_btn2_clicked(self):
        Age, Ok = QInputDialog.getInt(
            self, "Text", "Enter Your Age:", 18, 18, 65, 1)
        if Ok:
            QMessageBox.information(self, "Name", f"Your name is {Age}")
        else:
            QMessageBox.critical(self, "Canceled", "User canceled")

    def evt_btn3_clicked(self):
        colors = ["blue", "red", "yellow", "brown"]
        Age, Ok = QInputDialog.getItem(
            self, "Text", "Enter Your Favorite Color:", colors)
        if Ok:
            QMessageBox.information(
                self, "Name", f"Your  Favorite Color is {Age}")
        else:
            QMessageBox.critical(self, "Canceled", "User canceled")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
