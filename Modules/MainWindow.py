# Основное окно приложения
from PyQt5 import QtCore, QtWidgets, QtGui
from Modules.Widget import Widget


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent, flags=QtCore.Qt.Window | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("SG Mechanicus by [INQ]Kate Simons v0.0.1 alpha")
        self.setStyleSheet(
            "QFrame QPushbutton {font-size:10pt;font-family:Verdana;"
            "color:black;font-weight:normal;}"
            "ShipTreeLabel {font-size:14pt;font-family:Verdana;"
            "border:1px solid #9AA6A7;}")
        self.resize(800, 600)
        self.settings = QtCore.QSettings("Author", "SG Mechanicus")
        self.SGM = Widget()
        self.setCentralWidget(self.SGM)
        menuBar = self.menuBar()
        toolBar = QtWidgets.QToolBar()
        SGMMenuFile = menuBar.addMenu("&File")
        action = SGMMenuFile.addAction(QtGui.QIcon(r"images/new.png"), "&New")
        toolBar.addAction(action)
        action.setStatusTip("Create new file")
        SGMMenuFile.addSeparator()
        toolBar.addSeparator()
        action = SGMMenuFile.addAction("&Quit", QtWidgets.qApp.quit)
        action.setStatusTip("Close application")
        SGMMenuAbout = menuBar.addMenu("&Help")
        action = SGMMenuAbout.addAction("About &application", self.aboutInfo)
        action.setStatusTip("Get help for application")
        toolBar.setMovable(False)
        toolBar.setFloatable(False)
        self.addToolBar(toolBar)
        if self.settings.contains("X") and self.settings.contains("Y"):
            self.move(self.settings.value("X"), self.settings.value("Y"))

    def closeEvent(self, event):
        g = self.geometry()
        self.settings.setValue("X", g.left())
        self.settings.setValue("Y", g.top())

    def aboutInfo(self):
        QtWidgets.QMessageBox.about(self, "About application", "<center>\"SG Mechanicus\" v0.0.1<br><br>"
        "(c) [INQ]Kate Simons 2021.")
