import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import VestelTV
import db
import settingsDialog
from VestelTV import VestelRemoteController


class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()

        tv = VestelRemoteController()

        uic.loadUi("Templates/main.ui", self)

        menu_bar = self.menuBar()
        option_menu = menu_bar.addMenu('&Options')
        settings_action = QtWidgets.QAction('&Settings', self)
        close_action = QtWidgets.QAction('&Quit', self)
        option_menu.addAction(settings_action)
        option_menu.addAction(close_action)

        settings_action.triggered.connect(self.openSettingsDialog)
        close_action.triggered.connect(self.quitApplication)

        self.button = self.findChild(QtWidgets.QPushButton, 'btn1')
        self.button.clicked.connect(tv.btnOne)

        self.button = self.findChild(QtWidgets.QPushButton, 'btn2')
        self.button.clicked.connect(tv.btnTwo)

        self.button = self.findChild(QtWidgets.QPushButton, 'btn3')
        self.button.clicked.connect(tv.btnThree)

        self.button = self.findChild(QtWidgets.QPushButton, 'btn4')
        self.button.clicked.connect(tv.btnFour)

        self.button = self.findChild(QtWidgets.QPushButton, 'btn5')
        self.button.clicked.connect(tv.btnFive)

        self.button = self.findChild(QtWidgets.QPushButton, 'btn6')
        self.button.clicked.connect(tv.btnSix)

        self.button = self.findChild(QtWidgets.QPushButton, 'btn7')
        self.button.clicked.connect(tv.btnSeven)

        self.button = self.findChild(QtWidgets.QPushButton, 'btn8')
        self.button.clicked.connect(tv.btnEight)

        self.button = self.findChild(QtWidgets.QPushButton, 'btn9')
        self.button.clicked.connect(tv.btnNine)

        self.button = self.findChild(QtWidgets.QPushButton, 'btn0')
        self.button.clicked.connect(tv.btnZero)

        self.button = self.findChild(QtWidgets.QPushButton, 'okButton')
        self.button.clicked.connect(tv.OK)

        self.button = self.findChild(QtWidgets.QPushButton, 'VolumeUpButton')
        self.button.clicked.connect(tv.VolumeUp)

        self.button = self.findChild(QtWidgets.QPushButton, 'VolumeDownButton')
        self.button.clicked.connect(tv.VolumeDown)

        self.button = self.findChild(QtWidgets.QPushButton, 'backButton')
        self.button.clicked.connect(tv.Back)

        self.button = self.findChild(QtWidgets.QPushButton, 'ExitButton')
        self.button.clicked.connect(tv.Exit)

        self.button = self.findChild(QtWidgets.QPushButton, 'muteButton')
        self.button.clicked.connect(tv.Mute)

        self.button = self.findChild(QtWidgets.QPushButton, 'ProgramUpButton')
        self.button.clicked.connect(tv.pUp)

        self.button = self.findChild(QtWidgets.QPushButton, 'ProgramDownButton')
        self.button.clicked.connect(tv.pDown)

        self.button = self.findChild(QtWidgets.QPushButton, 'upButton')
        self.button.clicked.connect(tv.UpButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'downButton')
        self.button.clicked.connect(tv.DownButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'leftButton')
        self.button.clicked.connect(tv.LeftButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'rightButton')
        self.button.clicked.connect(tv.RightButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'powerButton')
        self.button.clicked.connect(tv.powerOnOffButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'qMenuButton')
        self.button.clicked.connect(tv.OpenQMenu)

        self.button = self.findChild(QtWidgets.QPushButton, 'changeButton')
        self.button.clicked.connect(tv.changeButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'btn3D')
        self.button.clicked.connect(tv.ThreeD)

        self.button = self.findChild(QtWidgets.QPushButton, 'menuButton')
        self.button.clicked.connect(tv.ThreeD)

        self.button = self.findChild(QtWidgets.QPushButton, 'sourceButton')
        self.button.clicked.connect(tv.ThreeD)

        self.button = self.findChild(QtWidgets.QPushButton, 'infoButton')
        self.button.clicked.connect(tv.InfoButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'internetButton')
        self.button.clicked.connect(tv.InternetButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'backwardButton')
        self.button.clicked.connect(tv.backwardButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'recButton')
        self.button.clicked.connect(tv.recButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'stopButton')
        self.button.clicked.connect(tv.stopButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'playButton')
        self.button.clicked.connect(tv.playButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'pauseButton')
        self.button.clicked.connect(tv.pauseButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'forwardButton')
        self.button.clicked.connect(tv.forwardButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'mediaButton')
        self.button.clicked.connect(tv.mediaButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'subtitleButton')
        self.button.clicked.connect(tv.subtitleButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'languageButton')
        self.button.clicked.connect(tv.languageButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'epgButton')
        self.button.clicked.connect(tv.epgButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'teletextButton')
        self.button.clicked.connect(tv.teletextButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'redButton')
        self.button.clicked.connect(tv.redButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'yellowButton')
        self.button.clicked.connect(tv.yellowButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'blueButton')
        self.button.clicked.connect(tv.blueButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'greenButton')
        self.button.clicked.connect(tv.greenButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'NetflixButton')
        self.button.clicked.connect(tv.NetflixButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'YouTubeButton')
        self.button.clicked.connect(tv.YouTubeButton)

        self.show()

        self.checkConfig()

    def checkConfig(self):
        ip_address = db.select_ip()
        if ip_address is None or ip_address == "":
            settingsDialog.SettingsDialog(self).exec()
        else:
            if VestelTV.tv_accessible_check(ip_address):
                pass
            else:
                self.messageBox()

    def messageBox(self):
        QMessageBox().setIcon(QMessageBox.Information)
        QMessageBox.information(self, "Warning", "TV is not accessible, please check your TV or network!")
        settingsDialog.SettingsDialog(self).exec()

    @staticmethod
    def quitApplication():
        sys.exit()

    def openSettingsDialog(self):
        settingsDialog.SettingsDialog(self).exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
