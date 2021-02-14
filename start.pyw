# Запускающий файл
from PyQt5 import QtGui, QtWidgets
import sys
from Modules.MainWindow import MainWindow


app = QtWidgets.QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon(r"Images/SG_400x400.ico"))
window = MainWindow()
window.show()
sys.exit(app.exec_())
