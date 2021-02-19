# Главное окно
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QGridLayout, QAction, QVBoxLayout, QWidget
import sys


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.central_widget = QWidget()  # Создаем виджет для центрального виджета QMainWindow
        self.setCentralWidget(self.central_widget)  # Указываем центральный виджет
        self.init_ui()  # Выполняет основную функцию (метод)

    def init_ui(self):
        main_window = QtWidgets.QMainWindow()  # попробовать поработать с QMainWindow вместо QWidget
        self.setWindowTitle("SG Mechanicus by [INQ]Kate Simons v.0.0.1 alpha")
        self.setFixedSize(800, 600)

        ico = QtGui.QIcon("../Images/SG_main.ico")  # Иконка приложения и окна
        self.setWindowIcon(ico)

        self.move(main_window.width() * -2, 0)  # блок центровки окна на экране
        desktop = QtWidgets.QApplication.desktop()
        x = (desktop.width() - main_window.frameSize().width()) // 2
        y = (desktop.height() - main_window.frameSize().height()) // 2
        self.move(x, y)

        menubar = self.menuBar()  # главное меню
        file_menu = menubar.addMenu("File")
        exit_action = QAction("Quit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        toolbar = self.addToolBar("something")  # блок панели инструментов (кнопки настроек профиля)
        toolbar.setMovable(False)
        toolbar.setFloatable(False)
        toolbar.setFixedHeight(30)

        grid = QGridLayout()  # основная сетка (контейнер) компонентов
        shiptree = QVBoxLayout()  # список шипов
        grid.addLayout(shiptree, 0, 0)
        self.central_widget.setLayout(grid)  # устанавливаем сетку на центральный виджет

        button1 = QtWidgets.QPushButton("button1")  # определяем кнопку
        shiptree.addWidget(button1, 0)  # помещаем кнопку в компонент


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
