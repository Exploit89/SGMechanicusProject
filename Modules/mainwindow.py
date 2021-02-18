# Главное окно
from PyQt5 import QtCore, QtWidgets, QtGui
import sys


app = QtWidgets.QApplication(sys.argv)
main_window = QtWidgets.QWidget()  # попробовать поработать с QMainWindow вместо QWidget
main_window.setWindowTitle("SG Mechanicus by [INQ]Kate Simons v.0.0.1 alpha")
main_window.setFixedSize(800, 600)

ico = QtGui.QIcon(r"Images\SG_400x400.ico")
main_window.setWindowIcon(ico)
app.setWindowIcon(ico)

main_window.move(main_window.width() * -2, 0)  # блок центровки окна на экране
desktop = QtWidgets.QApplication.desktop()
x = (desktop.width() - main_window.frameSize().width()) // 2
y = (desktop.height() - main_window.frameSize().height()) // 2
main_window.move(x, y)

main_window_panel = QtWidgets.QVBoxLayout()  # Основной лейаут
top_panel = QtWidgets.QHBoxLayout()  # верхняя панель с кнопками
implant_button = QtWidgets.QPushButton("Implant")  # должна открывать окно с импами
top_panel.addWidget(implant_button)

main_window_panel.addLayout(top_panel)  # добавляем в основную панель окна верхнюю панель
main_window.setLayout(main_window_panel)  # задаем основной лейаут

main_window.show()
sys.exit(app.exec_())
