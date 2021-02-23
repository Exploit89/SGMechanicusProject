# Модуль старта приложения
from PyQt5 import QtGui, QtWidgets
import sys

from Modules.mainwindow import MainWindow

app = QtWidgets.QApplication(sys.argv)
ico = QtGui.QIcon("../Images/SG_main.ico")  # Иконка приложения и окна
app.setWindowIcon(ico)
window = MainWindow()
window.show()
sys.exit(app.exec_())
