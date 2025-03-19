# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/rsa.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1172, 456)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(170, 340, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_encrypt.setFont(font)
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 20, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(34, 100, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txt_plaintext = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_plaintext.setGeometry(QtCore.QRect(140, 100, 411, 87))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_plaintext.setFont(font)
        self.txt_plaintext.setObjectName("txt_plaintext")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 210, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txt_ciphertext = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_ciphertext.setGeometry(QtCore.QRect(140, 210, 411, 87))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_ciphertext.setFont(font)
        self.txt_ciphertext.setObjectName("txt_ciphertext")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(620, 100, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(630, 210, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.txt_information = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_information.setGeometry(QtCore.QRect(730, 100, 411, 87))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_information.setFont(font)
        self.txt_information.setObjectName("txt_information")
        self.txt_signature = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_signature.setGeometry(QtCore.QRect(730, 210, 411, 87))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_signature.setFont(font)
        self.txt_signature.setObjectName("txt_signature")
        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(400, 340, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_decrypt.setFont(font)
        self.btn_decrypt.setObjectName("btn_decrypt")
        self.btn_sign = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(750, 340, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_sign.setFont(font)
        self.btn_sign.setObjectName("btn_sign")
        self.btn_verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(1000, 340, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_verify.setFont(font)
        self.btn_verify.setObjectName("btn_verify")
        self.btn_generatekey = QtWidgets.QPushButton(self.centralwidget)
        self.btn_generatekey.setGeometry(QtCore.QRect(780, 20, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_generatekey.setFont(font)
        self.btn_generatekey.setObjectName("btn_generatekey")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1172, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.label.setText(_translate("MainWindow", "RSA CIPHER"))
        self.label_2.setText(_translate("MainWindow", "Plain Text:"))
        self.label_3.setText(_translate("MainWindow", "Cipher Text:"))
        self.label_4.setText(_translate("MainWindow", "Information:"))
        self.label_5.setText(_translate("MainWindow", "Signature:"))
        self.btn_decrypt.setText(_translate("MainWindow", "Decrypt"))
        self.btn_sign.setText(_translate("MainWindow", "Sign"))
        self.btn_verify.setText(_translate("MainWindow", "Verify"))
        self.btn_generatekey.setText(_translate("MainWindow", "Generate Keys"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
