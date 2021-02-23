# Модуль старта приложения
from PyQt5 import QtGui, QtWidgets, QtCore
import sys

from Modules.mainwindow import MainWindow

app = QtWidgets.QApplication(sys.argv)
ico = QtGui.QIcon("../Images/SG_main.ico")  # Иконка приложения и окна
app.setWindowIcon(ico)
splash = QtWidgets.QSplashScreen(QtGui.QPixmap("../Images/SGM_logo.png"))
splash.showMessage("Loading... 0%", QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.white)
splash.show()
QtWidgets.qApp.processEvents()
window = MainWindow()
window.load_data(splash)
window.show()
splash.finish(window)
sys.exit(app.exec_())
