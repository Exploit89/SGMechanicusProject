from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel

from Modules import styles


class AcademyWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(AcademyWindow, self).__init__(parent, flags=QtCore.Qt.Window | QtCore.Qt.MSWindowsFixedSizeDialogHint |
                                       QtCore.Qt.FramelessWindowHint)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setWindowTitle("Academy")
        self.resize(900, 500)
        self.label = QLabel(self, alignment=Qt.AlignCenter | Qt.AlignTop)  # Новый лейбл для окна без рамки
        self.label.setText("Academy")
        self.label.setStyleSheet(styles.label_style)
        self.label.setGeometry(0, 1, 900, 20)

        vbox = QtWidgets.QVBoxLayout()
        self.setLayout(vbox)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)

        quit_button = QtWidgets.QPushButton(QIcon("../Images/Icons/Window/close.png"), "", self)  # кнопка закрытия окна
        quit_button.setStyleSheet(styles.tab_style)
        quit_button.setFixedSize(20, 20)
        quit_button.move(880, 0)
        quit_button.setFlat(True)
        quit_button.clicked.connect(self.close)

    def closeEvent(self, evt):
        """при закрытии - сохранение координат положения окна и диалог сохранения"""

        result = QtWidgets.QMessageBox.question(self, "Closing confirmation",
                                                "Do you really want to close window?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            evt.accept()
            QtWidgets.QWidget.closeEvent(self, evt)
        else:
            evt.ignore()
