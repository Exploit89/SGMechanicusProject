# Ячейка поля ShipTree
from PyQt5 import QtCore, QtWidgets


class ShipTreeLabel(QtWidgets.QLabel):
    changeCellFocus = QtCore.pyqtSignal(int)

    def __init__(self, id, parent=None):
        QtWidgets.QLabel.__init__(self, parent)
        self.setAlignment(QtCore.Qt.AlignLeft)
        self.setFixedSize(40, 10)
        self.setMargin(0)
        self.setText("")
        if id < 0:
            id = 0
        self.id = id
        self.isCellChange = True

    def mousePressEvent(self, event):
        self.changeCellFocus.emit(self, id)
        QtWidgets.QLabel.mousePressEvent(self, event)

    def setNewText(self, text):
        if self.isCellChange:
            self.setText(text)