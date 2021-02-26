# Модуль старта приложения
from PyQt5 import QtGui, QtWidgets, QtCore
import sys
import time

from Modules.mainwindow import MainWindow

app = QtWidgets.QApplication(sys.argv)
ico = QtGui.QIcon("../Images/SG_main.ico")  # Иконка приложения и окна
app.setWindowIcon(ico)

splash_pic = QtGui.QPixmap("../Images/SGM_logo.png")
splash = QtWidgets.QSplashScreen(splash_pic)
splash.showMessage("Loading... 0%", QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.white)

progressbar = QtWidgets.QProgressBar(splash)
splash.setMask(splash_pic.mask())

splash.show()

app.processEvents()
for i in range(0, 101):
    progressbar.setValue(i)
    t = time.time()
    while time.time() < t + 0.03:
        splash.showMessage("Loading... {0}%".format(i * 1),
                       QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom, QtCore.Qt.white)
        app.processEvents()

window = MainWindow()
window.show()
splash.finish(window)
sys.exit(app.exec_())
