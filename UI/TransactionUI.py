# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TransactionUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Transaction(object):
    def setupUi(self, Transaction):
        Transaction.setObjectName("Transaction")
        Transaction.setWindowModality(QtCore.Qt.NonModal)
        Transaction.resize(329, 342)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Transaction.sizePolicy().hasHeightForWidth())
        Transaction.setSizePolicy(sizePolicy)
        self.wordLabel = QtWidgets.QLabel(Transaction)
        self.wordLabel.setGeometry(QtCore.QRect(40, 20, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.wordLabel.setFont(font)
        self.wordLabel.setObjectName("wordLabel")
        self.transactionBrowser = QtWidgets.QTextBrowser(Transaction)
        self.transactionBrowser.setGeometry(QtCore.QRect(40, 70, 256, 192))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(10)
        self.transactionBrowser.setFont(font)
        self.transactionBrowser.setObjectName("transactionBrowser")
        self.statusLabel = QtWidgets.QLabel(Transaction)
        self.statusLabel.setGeometry(QtCore.QRect(40, 280, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.statusLabel.setFont(font)
        self.statusLabel.setObjectName("statusLabel")

        self.retranslateUi(Transaction)
        QtCore.QMetaObject.connectSlotsByName(Transaction)

    def retranslateUi(self, Transaction):
        _translate = QtCore.QCoreApplication.translate
        Transaction.setWindowTitle(_translate("Transaction", "Form"))
        self.wordLabel.setText(_translate("Transaction", "TextLabel"))
        self.statusLabel.setText(_translate("Transaction", "TextLabel"))

