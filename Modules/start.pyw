# Модуль старта приложения
from PyQt5 import QtGui, QtWidgets, QtCore
import sys
import time

from Modules.mainwindow import MainWindow
import styles


sys._excepthook = sys.excepthook


def my_exception_hook(exctype, value, traceback):
    """блок отлова исключения при закрытии программы"""
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = my_exception_hook

app = QtWidgets.QApplication(sys.argv)
ico = QtGui.QIcon("../Images/SG_main.ico")  # Иконка приложения и окна
app.setWindowIcon(ico)

splash_pic = QtGui.QPixmap("../Images/SGM_logo.png")  # заставка
splash = QtWidgets.QSplashScreen(splash_pic)
splash.showMessage("Loading... 0%", QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.white)

progressbar = QtWidgets.QProgressBar(splash)  # Полоса загрузки на заставке
progressbar.setGeometry(0, 521, 700, 5)
progressbar.setTextVisible(False)
progressbar.setStyleSheet(styles.progressbar_style)  # стиль полосы загрузки

splash.setMask(splash_pic.mask())

splash.show()

app.processEvents()
for i in range(0, 101):
    progressbar.setValue(i)
    t = time.time()
    while time.time() < t + 0.003:  # установить значение 0.03
        splash.showMessage("Loading... {0}%".format(i * 1),
                           QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom, QtCore.Qt.white)
        app.processEvents()
#time.sleep(0.9)  # установить значение 0.9

window = MainWindow()
window.show()

"""постоянная центровка окна"""
window.move(window.width() * -2, 0)
desktop = QtWidgets.QApplication.desktop()
x = (desktop.width() - window.frameSize().width()) // 2
y = (desktop.height() - window.frameSize().height()) // 2
window.move(x, y)

splash.finish(window)
try:
    sys.exit(app.exec_())
except:
    print('exiting')
