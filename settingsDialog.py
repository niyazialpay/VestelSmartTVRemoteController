from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QDialog, QMessageBox
import VestelTV
import db


def validate(IP):
    """
  :type IP: str
  :rtype: str
  """

    def isIPv4(s):
        try:
            return str(int(s)) == s and 0 <= int(s) <= 255
        except:
            return False

    def isIPv6(s):
        if len(s) > 4:
            return False
        try:
            return int(s, 16) >= 0 and s[0] != '-'
        except:
            return False

    if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
        return "IPv4"
    if IP.count(":") == 7 and all(isIPv6(i) for i in IP.split(":")):
        return "IPv6"
    return "Neither"


class SettingsDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(SettingsDialog, self).__init__(*args, **kwargs)
        uic.loadUi("Templates/settings.ui", self)

        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)

        self.button = self.findChild(QtWidgets.QPushButton, 'cancelButton')
        self.button.clicked.connect(self.closeAction)

        self.button = self.findChild(QtWidgets.QPushButton, 'saveButton')
        self.button.clicked.connect(self.saveSettings)
        self.input = self.findChild(QtWidgets.QLineEdit, 'txtIP')

        ip_address = db.select_ip()
        if ip_address is not None:
            self.input.setText(ip_address)

    def saveSettings(self):
        IP_address = str(self.input.text()).strip()
        if validate(IP_address) == "IPv4":
            if VestelTV.tv_accessible_check(IP_address):
                db.insert_or_change_ip(IP_address)
                self.close()
            else:
                QMessageBox().setIcon(QMessageBox.Information)
                QMessageBox.information(self, "Warning", "TV is not accessible, please check entered IP address!")
        else:
            QMessageBox().setIcon(QMessageBox.Information)
            QMessageBox.information(self, "Warning", "IP address is not valid!")

    def closeAction(self):
        ip_address = db.select_ip()
        if ip_address is None or ip_address == "":
            pass
        else:
            self.close()
