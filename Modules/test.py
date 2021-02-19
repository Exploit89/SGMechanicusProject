from PyQt5 import QtWidgets, QtGui
import sys


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.init_ui()

    def init_ui(self):
        main_window = QtWidgets.QWidget()  # попробовать поработать с QMainWindow вместо QWidget
        self.setWindowTitle("SG Mechanicus by [INQ]Kate Simons v.0.0.1 alpha")
        self.setFixedSize(800, 600)

        ico = QtGui.QIcon("../Images/SG_main.ico")  # Иконка приложения и окна
        self.setWindowIcon(ico)

        self.move(main_window.width() * -2, 0)  # блок центровки окна на экране
        desktop = QtWidgets.QApplication.desktop()
        x = (desktop.width() - main_window.frameSize().width()) // 2
        y = (desktop.height() - main_window.frameSize().height()) // 2
        self.move(x, y)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
