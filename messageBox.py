import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(200, 200)

        self.btn = QPushButton("Show Message", self)
        self.btn.move(40, 40)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        # method1
        # result = QMessageBox.question(
        #     self, "Disk Full", "Your Disk Drive Is Almost Full")
        # if result == QMessageBox.Yes:
        #     QMessageBox.information(self, "", "You Clicked Yes")
        # else:
        #     QMessageBox.information(self, "", "You Clicked No")
        # method2
        msgDiskFul = QMessageBox()
        msgDiskFul.setText("Your Disk Drive Is Almost Full")
        msgDiskFul.setDetailedText("Please make some room on your disk")
        msgDiskFul.setIcon(QMessageBox.Information)
        msgDiskFul.setWindowTitle("Full Drive")
        msgDiskFul.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgDiskFul.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
