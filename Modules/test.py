# Главное окно
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QGridLayout, QAction, QVBoxLayout, QWidget, QFrame, QScrollArea, QHBoxLayout
import sys


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        """Конструктор класса - содержит определение центрального виджета"""
        QtWidgets.QMainWindow.__init__(self, parent)
        self.central_widget = QWidget()  # Создаем виджет для центрального виджета QMainWindow
        self.setCentralWidget(self.central_widget)  # Указываем центральный виджет
        self.init_ui()  # Выполняет основную функцию (метод)

    def init_ui(self):
        """основная функция(метод класса) - интерфейс программы"""
        main_window = QtWidgets.QMainWindow()  # попробовать поработать с QMainWindow вместо QWidget
        self.setWindowTitle("SG Mechanicus by [INQ]Kate Simons v.0.0.1 alpha")
        self.setFixedSize(800, 600)

        ico = QtGui.QIcon("../Images/SG_main.ico")  # Иконка приложения и окна
        self.setWindowIcon(ico)

        self.move(main_window.width() * -2, 0)  # блок центровки окна на экране
        desktop = QtWidgets.QApplication.desktop()
        x = (desktop.width() - main_window.frameSize().width()) // 2
        y = (desktop.height() - main_window.frameSize().height()) // 2
        self.move(x, y)

        menubar = self.menuBar()  # главное меню
        menubar.setContextMenuPolicy(Qt.PreventContextMenu)  # убираем меню вызываемое правой кнопкой
        file_menu = menubar.addMenu("File")
        settings_menu = menubar.addMenu("Settings")  # добавить кнопки в меню настроек

        exit_action = QAction("Quit", self)  # Кнопка выхода - переместить в конец, добавить диалог -> Save
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        file_menu.addSeparator()  # разделитель в меню

        save_action = QAction("Save Profile", self)
        # добавить функцию выполнения в эту строку
        file_menu.addAction(save_action)

        load_action = QAction("Load Profile", self)
        # добавить функцию выполнения в эту строку
        file_menu.addAction(load_action)

        toolbar = self.addToolBar("something")  # блок панели инструментов (кнопки настроек профиля)
        toolbar.setMovable(False)
        toolbar.setFloatable(False)
        toolbar.setFixedHeight(30)
        toolbar.setContextMenuPolicy(Qt.PreventContextMenu)

        open_implant = toolbar.addAction("Implant")  # Добавить в скобки перед именем - действие
        open_academy = toolbar.addAction("Academy")  # Добавить в скобки перед именем - действие
        open_research = toolbar.addAction("Research")  # Добавить в скобки перед именем - действие
        open_recruit = toolbar.addAction("Recruit")  # Добавить в скобки перед именем - действие
        take_screenshot = toolbar.addAction("Screenshot")  # Добавить в скобки перед именем - действие

        grid = QGridLayout()  # основная сетка (контейнер) компонентов
        grid.setContentsMargins(5, 5, 5, 5)  # отступы компонентов на сетке
        shiptree = QHBoxLayout()  # список шипов
        equipmenttree = QHBoxLayout()  # список оборудки

        grid.addLayout(shiptree, 2, 1, 6, 1)  # имя, координаты, кол-во строк и столбцов
        grid.addLayout(equipmenttree, 10, 1, 4, 1)

        scroll = QScrollArea()
        scr = QWidget()

        shiptreebox = QtWidgets.QToolBox(self)  # аккордеон шипов
        shiptreebox.setFixedSize(100, 300)
        shiptreebox.setFrameStyle(QFrame.StyledPanel)  # Рамка
        shiptree.addWidget(shiptreebox)
        shiptree.addWidget(scroll)

        scr.setLayout(shiptree)
        scroll.setWidget(shiptreebox)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setFixedSize(5, 300)
        scroll.setGeometry(0, 0, 10, 300)  # не фурычит

        equipmenttreebox = QtWidgets.QToolBox(self)  # аккордеон оборудки
        equipmenttreebox.setFixedSize(100, 200)
        equipmenttreebox.setFrameStyle(QFrame.StyledPanel)  # Рамка
        equipmenttree.addWidget(equipmenttreebox)

        button01 = QtWidgets.QPushButton("Railgun")
        button02 = QtWidgets.QPushButton("Recharger")
        button03 = QtWidgets.QPushButton("Enhancer")

        equipmenttreebox.insertItem(0, button01, "Weapon")
        equipmenttreebox.insertItem(1, button02, "Device")
        equipmenttreebox.insertItem(2, button03, "Component")

        self.central_widget.setLayout(grid)  # устанавливаем сетку на центральный виджет

        button1 = QtWidgets.QPushButton("Shipname1")  # определяем кнопку
        button2 = QtWidgets.QPushButton("Shipname2")  # определяем кнопку
        button3 = QtWidgets.QPushButton("Shipname3")  # определяем кнопку
        button4 = QtWidgets.QPushButton("Shipname4")  # определяем кнопку
        button5 = QtWidgets.QPushButton("Shipname5")  # определяем кнопку
        button6 = QtWidgets.QPushButton("Shipname6")  # определяем кнопку

        shiptreebox.insertItem(0, button1, "ECD")  # помещаем кнопку в компонент
        shiptreebox.insertItem(1, button2, "NEF")  # помещаем кнопку в компонент
        shiptreebox.insertItem(2, button3, "RS")  # помещаем кнопку в компонент
        shiptreebox.insertItem(3, button4, "OE")  # помещаем кнопку в компонент
        shiptreebox.insertItem(4, button5, "USSH")  # помещаем кнопку в компонент
        shiptreebox.insertItem(5, button6, "Exclusive")  # помещаем кнопку в компонент


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
