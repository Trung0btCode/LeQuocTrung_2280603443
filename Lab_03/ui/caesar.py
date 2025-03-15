# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './caesar.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = 'C:\\Users\\MSI\\AppData\\Roaming\\Python\\Python310\\site-packages\\PyQt5\\Qt5\\plugins\\platforms'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 100, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 240, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 350, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txt_plain = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_plain.setGeometry(QtCore.QRect(250, 100, 301, 91))
        self.txt_plain.setObjectName("txt_plain")
        self.txt_key = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_key.setGeometry(QtCore.QRect(250, 230, 111, 81))
        self.txt_key.setObjectName("txt_key")
        self.txt_cipher = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_cipher.setGeometry(QtCore.QRect(250, 350, 301, 91))
        self.txt_cipher.setObjectName("txt_cipher")
        self.btn_en = QtWidgets.QPushButton(self.centralwidget)
        self.btn_en.setGeometry(QtCore.QRect(250, 490, 93, 28))
        self.btn_en.setObjectName("btn_en")
        self.btn_de = QtWidgets.QPushButton(self.centralwidget)
        self.btn_de.setGeometry(QtCore.QRect(460, 490, 93, 28))
        self.btn_de.setObjectName("btn_de")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 20, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "PlainText"))
        self.label_2.setText(_translate("MainWindow", "Key"))
        self.label_3.setText(_translate("MainWindow", "CipherText"))
        self.btn_en.setText(_translate("MainWindow", "Encrypt"))
        self.btn_de.setText(_translate("MainWindow", "Decrypt"))
        self.label_4.setText(_translate("MainWindow", "CAESAR_CIPHER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
