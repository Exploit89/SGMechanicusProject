# Списки имен эквипа
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QImage


class ShipImageView(QImage):

    def __init__(self, parent=None):
        QImage.__init__(self, parent)
        self.imagepath = QImage.load()
