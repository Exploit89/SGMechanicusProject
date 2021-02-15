"""Main window"""
from PyQt5 import QtCore, QtWidgets, QtGui


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent, flags=QtCore.Qt.Window | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("SG Mechanicus by [INQ]Kate Simons v0.0.1 alpha")
        self.resize(800, 600)
        self.settings = QtCore.QSettings("Author", "SG Mechanicus")  # Save current settings
#        self.setStyleSheet(
#            "QFrame QPushbutton {font-size:10pt;font-family:Verdana;"
#            "color:black;font-weight:normal;}"
#            "border:50px solid #9AA6A7;}"
#        )

        menubar = self.menuBar()
        toolbar = QtWidgets.QToolBar()
        sgm_menu_file = menubar.addMenu("File")
        action = sgm_menu_file.addAction("New Profile")
        action = sgm_menu_file.addAction("Save Profile")
        action = sgm_menu_file.addAction("Load Profile")
        sgm_menu_file.addSeparator()
        action = sgm_menu_file.addAction("Quit", QtWidgets.qApp.quit)

        sgm_menu_file = menubar.addMenu("Settings")
        # here I can add some setting button, like change window size

        sgm_menu_about = menubar.addMenu("Help")
        action = sgm_menu_about.addAction("About application", self.call_about_info)

        toolbar.setMovable(False)
        toolbar.setFloatable(False)
        toolbar.setFixedHeight(30)  # height of toolbar
        toolbar.addAction("Implants")  # I need to add event action before text
        toolbar.addAction("Recruit")  # I need to add event action before text
        toolbar.addAction("Academy")  # I need to add event action before text
        toolbar.addAction("Research")  # I need to add event action before text

        self.addToolBar(toolbar)

        if self.settings.contains("X") and self.settings.contains("Y"):
            self.move(self.settings.value("X"), self.settings.value("Y"))

    def close_event(self, event):
        g = self.geometry()
        self.settings.setValue("X", g.left())
        self.settings.setValue("Y", g.top())

    def call_about_info(self):
        QtWidgets.QMessageBox.about(self, "About application", "<center>\"SG Mechanicus\" v0.0.1<br><br>"
                                    "(c) [INQ]Kate Simons 2021.")
