# Основное окно приложения
from PyQt5 import QtCore, QtGui, QtWidgets
from Modules.widget import Widget
import time


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent, flags=QtCore.Qt.Window | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("SG Mechanicus by [INQ]Kate Simons v.0.0.1 alpha")
        self.setFixedSize(800, 600)
        self.settings = QtCore.QSettings("Kate Simons", "SG Mechanicus")
        self.SGM = Widget()
        self.setCentralWidget(self.SGM)

        menubar = self.menuBar()  # главное меню
        menubar.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)  # убираем меню вызываемое правой кнопкой
        file_menu = menubar.addMenu("File")
        settings_menu = menubar.addMenu("Settings")  # добавить кнопки в меню настроек
        about_menu = menubar.addMenu("Help")

        exit_action = QtWidgets.QAction("Quit", self)  # Кнопка выхода - переместить в конец, добавить диалог -> Save
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        file_menu.addSeparator()  # разделитель в меню

        save_action = QtWidgets.QAction("Save Profile", self)
        # добавить функцию выполнения в эту строку
        file_menu.addAction(save_action)

        load_action = QtWidgets.QAction("Load Profile", self)
        # добавить функцию выполнения в эту строку
        file_menu.addAction(load_action)

        about_action = about_menu.addAction("About", self.aboutInfo)

        toolbar = QtWidgets.QToolBar()
        self.addToolBar(toolbar)  # блок панели инструментов (кнопки настроек профиля)
        toolbar.setMovable(False)
        toolbar.setFloatable(False)
        toolbar.setFixedHeight(30)
        toolbar.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)

        open_implant = toolbar.addAction("Implant")  # Добавить в скобки перед именем - действие
        open_academy = toolbar.addAction("Academy")  # Добавить в скобки перед именем - действие
        open_research = toolbar.addAction("Research")  # Добавить в скобки перед именем - действие
        open_recruit = toolbar.addAction("Recruit")  # Добавить в скобки перед именем - действие
        take_screenshot = toolbar.addAction("Screenshot")  # Добавить в скобки перед именем - действие

        if self.settings.contains("X") and self.settings.contains("Y"):  # проверка и загрузка сохраненных координат
            self.move(self.settings.value("X"), self.settings.value("Y"))

    def load_data(self, sp):
        """Экран загрузки и сплэшскрин"""
        for i in range(1, 101):
            time.sleep(0.03)
            sp.showMessage("Loading... {0}%".format(i * 1),
                           QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom, QtCore.Qt.white)
            QtWidgets.qApp.processEvents()

    def closeEvent(self, evt):
        """при закрытии - сохранение координат положения окна и диалог сохранения"""
        g = self.geometry()
        self.settings.setValue("X", g.left())
        self.settings.setValue("Y", g.top())

        result = QtWidgets.QMessageBox.question(self.SGM, "Closing confirmation",
                                                "Do you really want to close window?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            evt.accept()
            QtWidgets.QWidget.closeEvent(self.SGM, evt)
        else:
            evt.ignore()

    def aboutInfo(self):
        """Информация о программе"""
        QtWidgets.QMessageBox.about(self, "About app",
                                    "<center>\"SG Mechanicus\" v0.0.1 alpha<br><br>"
                                    "(c) [INQ]Kate Simons 2020-2021")
