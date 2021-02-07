from PyQt5 import QtGui, QtWidgets
import sys


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("blblblblb")
window.resize(640, 480)
ico = QtGui.QIcon("SG_400x400.ico")
window.setWindowIcon(ico)
app.setWindowIcon(ico)
window.show()
sys.exit(app.exec_())
