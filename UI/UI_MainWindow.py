# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(408, 290)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.incrementLabel = QtWidgets.QLabel(self.centralwidget)
        self.incrementLabel.setGeometry(QtCore.QRect(30, 50, 91, 20))
        self.incrementLabel.setObjectName("incrementLabel")
        self.todatLabel = QtWidgets.QLabel(self.centralwidget)
        self.todatLabel.setGeometry(QtCore.QRect(30, 90, 91, 20))
        self.todatLabel.setObjectName("todatLabel")
        self.totalLabel = QtWidgets.QLabel(self.centralwidget)
        self.totalLabel.setGeometry(QtCore.QRect(31, 130, 91, 20))
        self.totalLabel.setObjectName("totalLabel")
        self.incrementButton = QtWidgets.QPushButton(self.centralwidget)
        self.incrementButton.setGeometry(QtCore.QRect(30, 180, 93, 51))
        self.incrementButton.setObjectName("incrementButton")
        self.todayButton = QtWidgets.QPushButton(self.centralwidget)
        self.todayButton.setGeometry(QtCore.QRect(160, 180, 93, 51))
        self.todayButton.setObjectName("todayButton")
        self.totalButton = QtWidgets.QPushButton(self.centralwidget)
        self.totalButton.setGeometry(QtCore.QRect(290, 180, 93, 51))
        self.totalButton.setObjectName("totalButton")
        self.incrementLine = QtWidgets.QLineEdit(self.centralwidget)
        self.incrementLine.setGeometry(QtCore.QRect(160, 50, 221, 21))
        self.incrementLine.setReadOnly(True)
        self.incrementLine.setObjectName("incrementLine")
        self.todayLine = QtWidgets.QLineEdit(self.centralwidget)
        self.todayLine.setGeometry(QtCore.QRect(160, 90, 221, 21))
        self.todayLine.setReadOnly(True)
        self.todayLine.setObjectName("todayLine")
        self.totalLine = QtWidgets.QLineEdit(self.centralwidget)
        self.totalLine.setGeometry(QtCore.QRect(160, 130, 221, 21))
        self.totalLine.setReadOnly(True)
        self.totalLine.setObjectName("totalLine")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 408, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.incrementButton.clicked.connect(MainWindow.incrementButtonPushed)
        self.todayButton.clicked.connect(MainWindow.todayButtonPushed)
        self.totalButton.clicked.connect(MainWindow.totalButtonPushed)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main"))
        self.incrementLabel.setText(_translate("MainWindow", "Increment"))
        self.todatLabel.setText(_translate("MainWindow", "Today"))
        self.totalLabel.setText(_translate("MainWindow", "Total"))
        self.incrementButton.setText(_translate("MainWindow", "Increment"))
        self.todayButton.setText(_translate("MainWindow", "Today"))
        self.totalButton.setText(_translate("MainWindow", "Total"))

