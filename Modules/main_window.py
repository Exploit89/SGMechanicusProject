# Главное окно
from PyQt5 import QtCore, QtWidgets, QtGui
import sys


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.main_window = QtWidgets.QWidget()  # попробовать поработать с QMainWindow вместо QWidget
        self.setWindowTitle("SG Mechanicus by [INQ]Kate Simons v.0.0.1 alpha")
        self.setFixedSize(800, 600)

        self.ico = QtGui.QIcon("../Images/SG_main.ico")  # Иконка приложения и окна
        self.setWindowIcon(self.ico)

        self.move(self.main_window.width() * -2, 0)  # блок центровки окна на экране
        self.desktop = QtWidgets.QApplication.desktop()
        self.x = (self.desktop.width() - self.main_window.frameSize().width()) // 2
        self.y = (self.desktop.height() - self.main_window.frameSize().height()) // 2
        self.move(self.x, self.y)

        self.main_window_panel = QtWidgets.QVBoxLayout()  # Основной лейаут
        self.top_panel = QtWidgets.QHBoxLayout()  # верхняя панель с кнопками
        self.implant_button = QtWidgets.QPushButton("Implant")  # должна открывать окно с импами
        self.top_panel.addWidget(self.implant_button)

        self.main_window_panel.addLayout(self.top_panel)  # добавляем в основную панель окна верхнюю панель
        self.setLayout(self.main_window_panel)  # задаем основной лейаут


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
