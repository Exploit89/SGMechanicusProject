# Основное окно приложения
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QDesktopWidget, QLabel

from Modules.widget import Widget
from Modules import styles


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent, flags=QtCore.Qt.Window | QtCore.Qt.MSWindowsFixedSizeDialogHint |
                                       QtCore.Qt.FramelessWindowHint)
        self.setWindowTitle("SG Mechanicus by [INQ]Kate Simons v.0.0.1 alpha")
        self.setFixedSize(1000, 600)
        self.settings = QtCore.QSettings("Kate Simons", "SG Mechanicus")
        self.SGM = Widget()
        self.setCentralWidget(self.SGM)
        self.setStyleSheet(styles.window_style)
        self.SGM.setStyleSheet(styles.window_style)

        menubar = self.menuBar()  # главное меню
        menubar.setStyleSheet(styles.menu_style)
        menubar.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)  # убираем меню вызываемое правой кнопкой
        file_menu = menubar.addMenu("File")
        settings_menu = menubar.addMenu("Settings")  # добавить кнопки в меню настроек
        about_menu = menubar.addMenu("Help")

        save_action = QtWidgets.QAction("Save Profile", self)
        # добавить функцию выполнения в эту строку
        file_menu.addAction(save_action)

        load_action = QtWidgets.QAction("Load Profile", self)
        # добавить функцию выполнения в эту строку
        file_menu.addAction(load_action)

        file_menu.addSeparator()  # разделитель в меню

        exit_action = QtWidgets.QAction("Quit", self)  # Кнопка выхода - переместить в конец, добавить диалог -> Save
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

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

        self.label = QLabel(self)  # Новый лейбл для окна без рамки
        self.label.setText("SG Mechanicus by [INQ]Kate Simons v.0.0.1 alpha")
        self.label.setStyleSheet(styles.label_style)
        self.label.setGeometry(330, 1, 650, 20)

        quit_button = QtWidgets.QPushButton('X', self)  # кнопка закрытия окна
        quit_button.setFixedSize(20, 20)
        quit_button.move(980, 0)
        quit_button.setFlat(True)
        quit_button.clicked.connect(self.close)

        minimize_button = QtWidgets.QPushButton('_', self)  # кнопка сворачивания окна
        minimize_button.setFixedSize(20, 20)
        minimize_button.move(960, 0)
        minimize_button.setFlat(True)
        minimize_button.clicked.connect(self.showMinimized)

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

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            x_main = self.geometry().x()  # получаем координаты окна относительно экрана
            y_main = self.geometry().y()
            cursor_x = QtGui.QCursor.pos().x()  # получаем координаты курсора относительно окна нашей программы
            cursor_y = QtGui.QCursor.pos().y()
            if x_main <= cursor_x <= x_main + self.geometry().width():
                if y_main <= cursor_y <= y_main + self.label.geometry().height():
                    self.old_pos = event.pos()
                else:
                    self.old_pos = None
        elif event.button() == QtCore.Qt.RightButton:
            self.old_pos = None

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.old_pos = None

    def mouseMoveEvent(self, event):
        try:
            if not self.old_pos:
                return
            delta = event.pos() - self.old_pos
            self.move(self.pos() + delta)
        except:
            pass

    def aboutInfo(self):
        """Информация о программе"""
        QtWidgets.QMessageBox.about(self, "About app",
                                    "<center>\"SG Mechanicus\" v0.0.1 alpha<br><br>"
                                    "(c) [INQ]Kate Simons 2020-2021")
