from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal, QEvent
from PyQt5.QtWidgets import QApplication, QWidget

from UI.TransactionUI import Ui_Transaction

class CTransaction(Ui_Transaction, QtWidgets.QMainWindow):
    cancelSignal=pyqtSignal()

    def __init__(self):
        super(Ui_Transaction,self).__init__()
        self.setupUi(self)
        # self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint |
        #             QtCore.Qt.WindowCloseButtonHint|
        #             QtCore.Qt.WindowStaysOnTopHint)

    def closeEvent(self, *args, **kwargs):
        self.cancelSignal.emit()

    def event(self,vEvent):
        if vEvent.type()==QEvent.ActivationChange:
            if QApplication.activeWindow()!=self:
                # self.hide()
                pass
        #return QWidget.event(vEvent)
        return True

