# Главное окно
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QGridLayout, QAction, QVBoxLayout
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

        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        exit_action = QAction("Quit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        toolbar = self.addToolBar("something")  # блок панели инструментов (кнопки настроек профиля)
        toolbar.setMovable(False)
        toolbar.setFloatable(False)
        toolbar.setFixedHeight(30)

        grid = QGridLayout()
        self.setLayout(grid)
        #central_widget = MainWindow(self)
        #self.setCentralWidget(central_widget)  # не фурычит

        shiptree = QtWidgets.QVBoxLayout()
        grid.addLayout(shiptree, 0, 0)

        button1 = QtWidgets.QPushButton("button1")
        shiptree.addWidget(button1, 0)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
