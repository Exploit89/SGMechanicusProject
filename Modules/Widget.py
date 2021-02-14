# Класс поля ShipTree
from PyQt5 import QtCore, QtGui, QtWidgets
from Modules.ShipTreeLabel import ShipTreeLabel


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        vBoxMain = QtWidgets.QVBoxLayout()
        frame1 = QtWidgets.QFrame()
