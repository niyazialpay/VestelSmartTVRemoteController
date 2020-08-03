import sys

from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMessageBox
from VestelTV import VestelRemoteController as tv
import time


class channelDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(channelDialog, self).__init__(*args, **kwargs)
        uic.loadUi("Templates/go_to_channel.ui", self)

        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)

        self.button = self.findChild(QtWidgets.QPushButton, 'cancelButton')
        self.button.clicked.connect(self.closeAction)

        self.button = self.findChild(QtWidgets.QPushButton, 'goButton')
        self.button.clicked.connect(self.go)
        self.input = self.findChild(QtWidgets.QLineEdit, 'txtChNumber')

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def go(self):
        try:
            channel = self.input.text()
            int(channel)
            i = 0
            second = 0.2
            while i < len(channel):
                ch = int(channel[i])
                if ch == 1:
                    tv.btnOne()
                elif ch == 2:
                    tv.btnTwo()
                elif ch == 3:
                    tv.btnThree()
                elif ch == 4:
                    tv.btnFour()
                elif ch == 5:
                    tv.btnFive()
                elif ch == 6:
                    tv.btnSix()
                elif ch == 7:
                    tv.btnSeven()
                elif ch == 8:
                    tv.btnEight()
                elif ch == 9:
                    tv.btnNine()
                elif ch == 0:
                    tv.btnZero()
                else:
                    tv.btnZero()
                time.sleep(second)
                i += 1
            tv.OK()
            self.close()
        except:
            QMessageBox().setIcon(QMessageBox.Information)
            QMessageBox.information(self, "Warning", "Entered value is not integer, please check again!")

    def closeAction(self):
        self.close()
