# Класс поля ShipTree
from PyQt5 import QtCore, QtGui, QtWidgets


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        vBoxMain = QtWidgets.QVBoxLayout()
        toolBox = QtWidgets.QToolBox()
        toolBox.addItem(QtWidgets.QLabel("Put here Ships"), "ECD")
        toolBox.addItem(QtWidgets.QLabel("Put here Ships"), "NEF")
        toolBox.addItem(QtWidgets.QLabel("Put here Ships"), "RS")
        toolBox.addItem(QtWidgets.QLabel("Put here Ships"), "OE")
        toolBox.addItem(QtWidgets.QLabel("Put here Ships"), "USSH")
        toolBox.addItem(QtWidgets.QLabel("Put here Ships"), "Exclusive")
        toolBox.setCurrentIndex(0)
        vBoxMain.addWidget(toolBox)
