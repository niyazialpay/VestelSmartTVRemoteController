import requests
from PyQt5.QtWidgets import QMessageBox

import db


def call_key_code(key_code):
    try:
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        xml = '<?xml version="1.0" ?> <remote> <key code="' + str(key_code) + '"/> </remote>'
        requests.post('http://' + db.select_ip() + ':56791/apps/vr/remote', data=xml, headers=headers)
        return True
    except requests.exceptions.ConnectionError:
        return False


def call_application(app):
    try:
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        requests.post('http://' + db.select_ip() + ':56791/apps/' + app, headers=headers)
        return True
    except requests.exceptions.ConnectionError:
        return False


def tv_accessible_check(IP):
    try:
        requests.get('http://' + IP + ':56792/dd.xml')
        return True
    except requests.exceptions.ConnectionError:
        return False


class VestelRemoteController:
    @staticmethod
    def powerOnOffButton():
        call_key_code(1012)

    @staticmethod
    def OpenQMenu():
        call_key_code(1043)

    @staticmethod
    def OpenMenu():
        call_key_code(1048)

    @staticmethod
    def changeButton():
        call_key_code(1034)

    @staticmethod
    def SourceButton():
        call_key_code(1056)

    @staticmethod
    def btnOne():
        call_key_code(1001)

    @staticmethod
    def btnTwo():
        call_key_code(1002)

    @staticmethod
    def btnThree():
        call_key_code(1003)

    @staticmethod
    def btnFour():
        call_key_code(1004)

    @staticmethod
    def btnFive():
        call_key_code(1005)

    @staticmethod
    def btnSix():
        call_key_code(1006)

    @staticmethod
    def btnSeven():
        call_key_code(1007)

    @staticmethod
    def btnEight():
        call_key_code(1008)

    @staticmethod
    def btnNine():
        call_key_code(1009)

    @staticmethod
    def btnZero():
        call_key_code(1000)

    @staticmethod
    def VolumeUp():
        call_key_code(1016)

    @staticmethod
    def VolumeDown():
        call_key_code(1017)

    @staticmethod
    def pUp():
        call_key_code(1032)

    @staticmethod
    def pDown():
        call_key_code(1033)

    @staticmethod
    def OK():
        call_key_code(1053)

    @staticmethod
    def Exit():
        call_key_code(1037)

    @staticmethod
    def Back():
        call_key_code(1010)

    @staticmethod
    def Mute():
        call_key_code(1013)

    @staticmethod
    def UpButton():
        call_key_code(1020)

    @staticmethod
    def DownButton():
        call_key_code(1019)

    @staticmethod
    def LeftButton():
        call_key_code(1021)

    @staticmethod
    def RightButton():
        call_key_code(1022)

    @staticmethod
    def ThreeD():
        call_key_code(1040)

    @staticmethod
    def InfoButton():
        call_key_code(1018)

    @staticmethod
    def InternetButton():
        call_key_code(1046)

    @staticmethod
    def backwardButton():
        call_key_code(1027)

    @staticmethod
    def forwardButton():
        call_key_code(1028)

    @staticmethod
    def playButton():
        call_key_code(1025)

    @staticmethod
    def pauseButton():
        call_key_code(1049)

    @staticmethod
    def stopButton():
        call_key_code(1024)

    @staticmethod
    def recButton():
        call_key_code(1051)

    @staticmethod
    def mediaButton():
        call_key_code(1057)

    @staticmethod
    def subtitleButton():
        call_key_code(1031)

    @staticmethod
    def languageButton():
        call_key_code(1015)

    @staticmethod
    def epgButton():
        call_key_code(1047)

    @staticmethod
    def redButton():
        call_key_code(1055)

    @staticmethod
    def yellowButton():
        call_key_code(1050)

    @staticmethod
    def blueButton():
        call_key_code(1052)

    @staticmethod
    def greenButton():
        call_key_code(1054)

    @staticmethod
    def NetflixButton():
        call_application("Netflix")

    @staticmethod
    def YouTubeButton():
        call_application("YouTube")
