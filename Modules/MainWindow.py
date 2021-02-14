# Основное окно приложения
from PyQt5 import QtCore, QtWidgets, QtGui


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
        menuBar = self.menuBar()
        toolBar = QtWidgets.QToolBar()
        vBoxMain = QtWidgets.QVBoxLayout()

        SGMMenuFile = menuBar.addMenu("&File")
        action = SGMMenuFile.addAction(QtGui.QIcon(r"images/new.png"), "&New Profile")
        action = SGMMenuFile.addAction(QtGui.QIcon(r"images/new.png"), "&Save Profile")
        action = SGMMenuFile.addAction(QtGui.QIcon(r"images/new.png"), "&Load Profile")

        toolBar.addAction("Implants")  # Нужно установить перед текстом переменную - действие, открывающее окно
        toolBar.addAction("Recruit")  # Нужно установить перед текстом переменную - действие, открывающее окно
        toolBar.addAction("Academy")  # Нужно установить перед текстом переменную - действие, открывающее окно
        toolBar.addAction("Research")  # Нужно установить перед текстом переменную - действие, открывающее окно

        action = SGMMenuFile.addAction("&Quit", QtWidgets.qApp.quit)

        SGMMenuFile = menuBar.addMenu("&Settings")
        SGMMenuAbout = menuBar.addMenu("&Help")
        action = SGMMenuAbout.addAction("About &application", self.aboutInfo)

        SGMMenuFile.addSeparator()
        toolBar.addSeparator()

        toolBar.setMovable(False)
        toolBar.setFloatable(False)

        toolBox = QtWidgets.QToolBox()  # это говно не работает
        toolBox.addItem(QtWidgets.QLabel("Put here Ships"), "ECD")
        toolBox.addItem(QtWidgets.QLabel("Put here Ships"), "NEF")
        toolBox.addItem(QtWidgets.QLabel("Put here Ships"), "RS")
        toolBox.addItem(QtWidgets.QLabel("Put here Ships"), "OE")
        toolBox.addItem(QtWidgets.QLabel("Put here Ships"), "USSH")
        toolBox.addItem(QtWidgets.QLabel("Put here Ships"), "Exclusive")
        toolBox.setCurrentIndex(0)

        vBoxMain.addWidget(toolBox)
        self.setLayout(vBoxMain)

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
