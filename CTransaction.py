from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal

from UI.TransactionUI import Ui_Transaction

class CTransaction(Ui_Transaction, QtWidgets.QMainWindow):
    cancelSignal=pyqtSignal()

    def __init__(self):
        super(Ui_Transaction,self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint |
                    QtCore.Qt.WindowCloseButtonHint|
                    QtCore.Qt.WindowStaysOnTopHint)
        desktop = QtWidgets.QApplication.desktop()
        x = desktop.width() - self.width()
        y = (desktop.height() - self.height()) / 3
        self.move(x, y)

    def closeEvent(self, *args, **kwargs):
        self.cancelSignal.emit()

