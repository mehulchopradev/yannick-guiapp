# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.firstEdt = QtWidgets.QLineEdit(self.centralwidget)
        self.firstEdt.setGeometry(QtCore.QRect(80, 80, 113, 23))
        self.firstEdt.setObjectName("firstEdt")
        self.opsBox = QtWidgets.QComboBox(self.centralwidget)
        self.opsBox.setGeometry(QtCore.QRect(270, 80, 79, 23))
        self.opsBox.setObjectName("opsBox")
        self.secondEdt = QtWidgets.QLineEdit(self.centralwidget)
        self.secondEdt.setGeometry(QtCore.QRect(430, 80, 113, 23))
        self.secondEdt.setObjectName("secondEdt")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 140, 80, 23))
        self.pushButton.setObjectName("pushButton")
        self.resultEdt = QtWidgets.QLineEdit(self.centralwidget)
        self.resultEdt.setGeometry(QtCore.QRect(250, 210, 113, 23))
        self.resultEdt.setObjectName("resultEdt")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.calculate)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.firstEdt.setPlaceholderText(_translate("MainWindow", "1st No"))
        self.secondEdt.setPlaceholderText(_translate("MainWindow", "2nd No"))
        self.pushButton.setText(_translate("MainWindow", "Calc"))
        self.resultEdt.setPlaceholderText(_translate("MainWindow", "result"))

