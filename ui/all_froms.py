# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\CHAT_2\ui\start_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox
from time import sleep
from Chat.src.sender import Sender
from Chat.cryptography.shifr import sh, unsh, hash
import sys


def write_tmp(js):
    with open("tmp.json", "w", encoding="UTF-8") as f:
        json.dump(js, f)


def read_tmp():
    with open("tmp.json", "r", encoding="UTF-8") as f:
        return json.load(f)


snd = Sender()


class MainForm(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(39, 39, 39);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.PostEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PostEdit.setGeometry(QtCore.QRect(10, 470, 261, 51))
        self.PostEdit.setStyleSheet("background-color: rgb(77, 77, 77);\n"
                                    "color: rgb(200, 200, 200);\n"
                                    "\n"
                                    "\n"
                                    "border: none;\n"
                                    "border-radius: 15px;")
        self.PostEdit.setText("")
        self.PostEdit.setObjectName("PostEdit")
        self.GetSmsEdit = QtWidgets.QTextBrowser(self.centralwidget)
        self.GetSmsEdit.setGeometry(QtCore.QRect(10, 10, 371, 431))
        self.GetSmsEdit.setStyleSheet("background-color: rgb(77, 77, 77);\n"
                                      "color: rgb(200, 200, 200);\n"
                                      "\n"
                                      "border: 3px solid rgb(222, 211, 208);\n"
                                      "border-radius: 30px;")
        self.GetSmsEdit.setObjectName("GetSmsEdit")
        self.sendMes_but = QtWidgets.QPushButton(self.centralwidget)
        self.sendMes_but.setGeometry(QtCore.QRect(300, 450, 81, 81))
        self.sendMes_but.setStyleSheet("background-color: rgb(223, 89, 217);\n"
                                       "color: rgb(200, 200, 200);\n"
                                       "\n"
                                       "border: none;\n"
                                       "border-radius: 40px;")
        self.sendMes_but.setObjectName("sendMes_but")
        self.Change_nameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Change_nameEdit.setGeometry(QtCore.QRect(510, 0, 141, 31))
        self.Change_nameEdit.setStyleSheet("background-color: rgb(77, 77, 77);\n"
                                           "color: rgb(200, 200, 200);\n"
                                           "\n"
                                           "border: none;\n"
                                           "\n"
                                           "border-radius:5px;")
        self.Change_nameEdit.setObjectName("Change_nameEdit")
        self.Change_passwordEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Change_passwordEdit.setGeometry(QtCore.QRect(510, 50, 141, 31))
        self.Change_passwordEdit.setStyleSheet("background-color: rgb(77, 77, 77);\n"
                                               "color: rgb(200, 200, 200);\n"
                                               "\n"
                                               "border: none;\n"
                                               "border-radius:5px;\n"
                                               "")
        self.Change_passwordEdit.setObjectName("Change_passwordEdit")
        self.IDROOM = QtWidgets.QLineEdit(self.centralwidget)
        self.IDROOM.setGeometry(QtCore.QRect(670, 500, 113, 31))
        self.IDROOM.setStyleSheet("background-color: rgb(77, 77, 77);\n"
                                  "color: rgb(200, 200, 200);\n"
                                  "\n"
                                  "border: none;\n"
                                  "\n"
                                  "border-radius:5px;")
        self.IDROOM.setObjectName("IDROOM")
        self.Change_ipEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Change_ipEdit.setGeometry(QtCore.QRect(510, 100, 151, 31))
        self.Change_ipEdit.setStyleSheet("background-color: rgb(77, 77, 77);\n"
                                         "color: rgb(200, 200, 200);\n"
                                         "\n"
                                         "border: none;\n"
                                         "\n"
                                         "border-radius:5px;")
        self.Change_ipEdit.setObjectName("Change_ipEdit")
        self.Change_nameBut = QtWidgets.QPushButton(self.centralwidget)
        self.Change_nameBut.setGeometry(QtCore.QRect(690, 0, 93, 28))
        self.Change_nameBut.setStyleSheet("background-color: rgb(77, 77, 77);\n"
                                          "color: rgb(200, 200, 200);\n"
                                          "\n"
                                          "")
        self.Change_nameBut.setObjectName("Change_nameBut")
        self.Change_passwordBut = QtWidgets.QPushButton(self.centralwidget)
        self.Change_passwordBut.setGeometry(QtCore.QRect(690, 50, 93, 28))
        self.Change_passwordBut.setStyleSheet("background-color: rgb(77, 77, 77);\n"
                                              "color: rgb(200, 200, 200);\n"
                                              "\n"
                                              "")
        self.Change_passwordBut.setObjectName("Change_passwordBut")
        self.Change_ipBut = QtWidgets.QPushButton(self.centralwidget)
        self.Change_ipBut.setGeometry(QtCore.QRect(690, 100, 93, 28))
        self.Change_ipBut.setStyleSheet("background-color: rgb(77, 77, 77);\n"
                                        "color: rgb(200, 200, 200);\n"
                                        "\n"
                                        "")
        self.Change_ipBut.setObjectName("Change_ipBut")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.set_parms()
        self.event_init_()
        self.id = "Main"
        self.name = self.get_name()
        self.keywords=["Succses","NoThisUser","HavingUsers","NoServerConnection","LoginOrPasswordIsUncorrect","CanNotWrite","NoThisRoom","CanNotRead"]
        
        
        self.smes = ["started"]
        self.timer = QTimer()
        self.timer.setInterval(1500)                    # Миллисекунды
        self.timer.timeout.connect(lambda: self.get_messange())
        self.timer.start()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def set_parms(self):
        tmp = read_tmp()
        self.login = tmp["login"]
        self.password = tmp["password"]
        self.name = tmp["name"]

    def event_init_(self):
        self.sendMes_but.clicked.connect(lambda: self.send_message())
        self.Change_ipBut.clicked.connect(lambda: self.change_ip())
        self.Change_nameBut.clicked.connect(lambda: self.change_name())
        self.Change_passwordBut.clicked.connect(lambda: self.change_password())
        self.IDROOM.textChanged.connect(lambda: self.change_id())

    def change_name(self):
        js1 = {"login": self.login,
               "password": self.password, "rule": "name", "znach": self.Change_nameEdit.text()}
        snd.chg(js1)
        self.name = self.get_name()

    def change_password(self):
        self.password = hash(self.Change_passwordEdit.text())
        js1 = {"login": self.login,
               "password": self.password, "rule": "password", "znach": self.password}
        snd.chg(js1)

    def change_ip(self):
        ip = self.Change_ipEdit.text()
        snd.ip_upd(ip)

    def change_id(self):
        self.id = self.IDROOM.text()

    def send_message(self):
        text = sh(f"{self.name} - {self.PostEdit.text()}")
        js1 = {"type": "post", "login": self.login,
               "password": self.password, "content": text}
        snd.mes(self.id, js1)

    def get_messange(self):
        txt = snd.mes(
            self.id, {"type": "get", "login": self.login, "password": self.password})
        txt2=unsh(txt)
        if txt in self.keywords:
            txt2=txt
        else:
            txt=txt2
        
        if txt == self.smes[-1]:
            pass
        else:
            self.GetSmsEdit.append(txt)
            self.smes.append(txt)

    def get_name(self):
        return snd.getname({"login": self.login,
                            "password": self.password})

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PostEdit.setPlaceholderText(
            _translate("MainWindow", "Введите сообщение"))
        self.GetSmsEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.sendMes_but.setText(_translate("MainWindow", "Отпрравить"))
        self.Change_nameEdit.setPlaceholderText(
            _translate("MainWindow", "Сменить имя"))
        self.Change_passwordEdit.setPlaceholderText(
            _translate("MainWindow", "Сменить пароль"))
        self.IDROOM.setPlaceholderText(_translate("MainWindow", "Room ID"))
        self.Change_ipEdit.setPlaceholderText(
            _translate("MainWindow", "Используемый IP"))
        self.Change_nameBut.setText(_translate("MainWindow", "Подтвердить"))
        self.Change_passwordBut.setText(
            _translate("MainWindow", "Подтвердить"))
        self.Change_ipBut.setText(_translate("MainWindow", "Подтвердить"))


class Ui_MainForm(object):
    def setupUi(self, MainForm):
        self.MainForm = MainForm
        MainForm.setObjectName("MainForm")
        MainForm.resize(400, 208)
        MainForm.setStyleSheet("\n"
                               "background-color: rgb(44, 44, 44)")
        self.Editlogin = QtWidgets.QLineEdit(MainForm)
        self.Editlogin.setGeometry(QtCore.QRect(120, 40, 141, 31))
        self.Editlogin.setStyleSheet("background-color: grey;\n"
                                     "border-radius: 10px;\n"
                                     "")
        self.Editlogin.setObjectName("Editlogin")
        self.EditPassword = QtWidgets.QLineEdit(MainForm)
        self.EditPassword.setGeometry(QtCore.QRect(120, 90, 141, 31))
        self.EditPassword.setStyleSheet("background-color: grey;\n"
                                        "border-radius: 10px;\n"
                                        "")
        self.EditPassword.setObjectName("EditPassword")
        self.button_vhod = QtWidgets.QPushButton(MainForm)
        self.button_vhod.setGeometry(QtCore.QRect(200, 140, 91, 28))
        self.button_vhod.setStyleSheet("\n"
                                       "background-color: rgb(66, 66, 66);\n"
                                       "color: rgb(214, 214, 214);")
        self.button_vhod.setObjectName("button_vhod")
        self.button_reg = QtWidgets.QPushButton(MainForm)
        self.button_reg.setGeometry(QtCore.QRect(90, 140, 91, 28))
        self.button_reg.setStyleSheet("\n"
                                      "background-color: rgb(66, 66, 66);\n"
                                      "color: rgb(214, 214, 214);")
        self.button_reg.setObjectName("button_reg")
        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

        self.but_event_init_()

    def but_event_init_(self):
        self.button_reg.clicked.connect(self.reg)
        self.button_vhod.clicked.connect(self.vhod)

    def reg(self):
        mes_box = QMessageBox()
        mes_box.setWindowTitle("Результат")
        login = self.Editlogin.text()
        password = hash(self.EditPassword.text())
        mes_box.setText(
            snd.reg({"login": login, "password": password, "name": "gust"}))
        mes_box.exec_()

    def set_new_window(self, window, app):
        self.newwin = window
        self.newapp = app

    def new_window(self):
        self.MainForm.hide()
        nw = MainForm()
        nw.setupUi(self.newwin)
        self.newwin.show()
        # sys.exit(self.newapp.exec_())

    def vhod(self):
        mes_box = QMessageBox()
        mes_box.setWindowTitle("Результат")
        login = self.Editlogin.text()
        password = hash(self.EditPassword.text())
        res = snd.vhod({"login": login, "password": password})
        mes_box.setText(res)
        mes_box.exec_()
        if res == "Succses":
            write_tmp({"login": login, "password": password, "name": "gust"})
            self.new_window()

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Form"))
        self.Editlogin.setPlaceholderText(_translate("MainForm", "Login"))
        self.EditPassword.setPlaceholderText(
            _translate("MainForm", "Password"))
        self.button_vhod.setText(_translate("MainForm", "Вход"))
        self.button_reg.setText(_translate("MainForm", "Регистрация"))
