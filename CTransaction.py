from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal, QEvent
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

from UI.TransactionUI import Ui_Transaction

class CTransaction(Ui_Transaction, QtWidgets.QMainWindow):
    cancelSignal=pyqtSignal()

    def __init__(self,vParent=None):
        super(Ui_Transaction,self).__init__(vParent)
        self.setupUi(self)
        # self.__mWidth=self.width()
        # self.__mHeight=self.height()
        # self.setCentralWidget(self.transactionAx)

    # self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint |
        #             QtCore.Qt.WindowCloseButtonHint|
        #             QtCore.Qt.WindowStaysOnTopHint)

    def closeEvent(self, vEvent):
        vEvent.ignore()
        self.cancelSignal.emit()
        self.hide()

    # def event(self,vEvent):
    #     if vEvent.type()==QEvent.ActivationChange:
    #         if QApplication.activeWindow()!=self:
    #             # self.hide()
    #             pass
    #     #return QWidget.event(vEvent)
    #     return True