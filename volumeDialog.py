from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMessageBox
import VestelTV
import time


class volumeDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(volumeDialog, self).__init__(*args, **kwargs)
        uic.loadUi("Templates/volume.ui", self)

        self.button = self.findChild(QtWidgets.QPushButton, 'volumeUpButton')
        self.button.clicked.connect(self.VolumeUp)

        self.button = self.findChild(QtWidgets.QPushButton, 'volumeDownButton')
        self.button.clicked.connect(self.VolumeDown)

        self.input = self.findChild(QtWidgets.QLineEdit, 'txtVolNumber')

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def VolumeUp(self):
        try:
            volume = int(self.input.text())
            i = 1
            while i <= volume:
                VestelTV.call_key_code(1016)
                time.sleep(0.3)
                i += 1
            self.close()
        except:
            QMessageBox().setIcon(QMessageBox.Information)
            QMessageBox.information(self, "Warning", "Entered value is not integer, please check again!")

    def VolumeDown(self):
        try:
            volume = int(self.input.text())
            i = 1
            while i <= volume:
                VestelTV.call_key_code(1017)
                time.sleep(0.3)
                i += 1
            self.close()
        except:
            QMessageBox().setIcon(QMessageBox.Information)
            QMessageBox.information(self, "Warning", "Entered value is not integer, please check again!")
