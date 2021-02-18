# Главное окно
from PyQt5 import QtCore, QtWidgets, QtGui
import sys


application = QtWidgets.QApplication(sys.argv)
main_window = QtWidgets.QWidget()  # попробовать поработать с QMainWindow вместо QWidget
main_window.setWindowTitle("SG Mechanicus by [INQ]Kate Simons v.0.0.1 alpha")
main_window.resize(800, 600)
main_window_panel = QtWidgets.QVBoxLayout()  # Основной лейаут
top_panel = QtWidgets.QHBoxLayout()  # верхняя панель с кнопками
implant_button = QtWidgets.QPushButton("Implant")  # должна открывать окно с импами
top_panel.addWidget(implant_button)

main_window_panel.addLayout(top_panel)  # добавляем в основную панель окна верхнюю панель
main_window.setLayout(main_window_panel)  # задаем основной лейаут

main_window.show()
sys.exit(application.exec_())
