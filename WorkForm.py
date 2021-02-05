from PyQt5 import QtCore, QtWidgets


class MyWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel("Label")
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.btnQuit = QtWidgets.QPushButton("Quit")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnQuit)
        self.setLayout(self.vbox)
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)

    """диалог закрытия программы"""
    def closeEvent(self, e):
        result = QtWidgets.QMessageBox.question(self, "Closing confirmation", "Do you really want to quit?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            e.accept()
            QtWidgets.QWidget.closeEvent(self, e)
        else:
            e.ignore()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("SG Mechanicus by [INQ] Kate Simons v0.01 alpha")
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())
