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
        Transaction.resize(618, 403)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Transaction.sizePolicy().hasHeightForWidth())
        Transaction.setSizePolicy(sizePolicy)
        self.statusLabel = QtWidgets.QLabel(Transaction)
        self.statusLabel.setGeometry(QtCore.QRect(40, 280, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.statusLabel.setFont(font)
        self.statusLabel.setObjectName("statusLabel")
        self.transactionAx = QAxContainer.QAxWidget(Transaction)
        self.transactionAx.setProperty("geometry", QtCore.QRect(0, 0, 621, 281))
        self.transactionAx.setObjectName("transactionAx")

        self.retranslateUi(Transaction)
        QtCore.QMetaObject.connectSlotsByName(Transaction)

    def retranslateUi(self, Transaction):
        _translate = QtCore.QCoreApplication.translate
        Transaction.setWindowTitle(_translate("Transaction", "Form"))
        self.statusLabel.setText(_translate("Transaction", "TextLabel"))

from PyQt5 import QAxContainer
