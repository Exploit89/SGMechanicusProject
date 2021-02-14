from PyQt5 import QtCore, QtWidgets, QtGui


class MainWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        ico = QtGui.QIcon("Images/SG_400x400.ico")
        self.shiptreebutton = QtWidgets.QPushButton("Some ship")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.shiptreebutton)
        self.setLayout(self.vbox)
        self.vbox.setAlignment(QtCore.Qt.AlignLeft)
        self.setWindowIcon(ico)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("SG Mechanicus by [INQ] Kate Simons v0.01 alpha")
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())
