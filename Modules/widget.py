# Основной виджет
from PyQt5 import QtCore, QtGui, QtWidgets


class Widget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        grid = QtWidgets.QGridLayout()  # Создаем сетку для всех элементов главного виджета
        grid.setSpacing(5)  # Расстояние между элементами сетки

        shiptree = QtWidgets.QVBoxLayout()  # Дерево шипов
        frame_shiptree = QtWidgets.QFrame()  # Рамка
        frame_shiptree.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        frame_shiptree.setFixedSize(100, 300)
        frame_shiptree.setLayout(shiptree)
        grid.addWidget(frame_shiptree, 2, 1, 6, 1)

        equipmenttree = QtWidgets.QVBoxLayout()  # Дерево эквипа
        frame_equipmenttree = QtWidgets.QFrame()  # Рамка
        frame_equipmenttree.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        frame_equipmenttree.setFixedSize(100, 170)
        frame_equipmenttree.setLayout(equipmenttree)
        grid.addWidget(frame_equipmenttree, 10, 1, 4, 1)

        button1 = QtWidgets.QPushButton("Shipname1")  # определяем кнопку
        button2 = QtWidgets.QPushButton("Shipname2")
        button3 = QtWidgets.QPushButton("Shipname3")
        button4 = QtWidgets.QPushButton("Shipname4")
        button5 = QtWidgets.QPushButton("Shipname5")

        shiptree.addWidget(button1)  # Добавляем кнопку
        shiptree.addWidget(button2)
        shiptree.addWidget(button3)
        shiptree.addWidget(button4)
        shiptree.addWidget(button5)

        button01 = QtWidgets.QPushButton("equip1")  # определяем кнопку
        button02 = QtWidgets.QPushButton("equip2")
        button03 = QtWidgets.QPushButton("equip3")
        button04 = QtWidgets.QPushButton("equip4")
        button05 = QtWidgets.QPushButton("equip5")

        equipmenttree.addWidget(button01)  # Добавляем кнопку
        equipmenttree.addWidget(button02)
        equipmenttree.addWidget(button03)
        equipmenttree.addWidget(button04)
        equipmenttree.addWidget(button05)

        main_image_frame = QtWidgets.QFrame()  # рамка для главной картинки
        main_image_frame.setFixedSize(300, 300)
        main_image_frame.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(main_image_frame, 2, 3, 6, 7)

        description_frame = QtWidgets.QFrame()  # рамка для показателей
        description_frame.setFixedSize(300, 500)
        description_frame.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(description_frame, 2, 11, 12, 1)

        grid.setColumnMinimumWidth(0, 1)  # ширина пустой колонки
        grid.setColumnMinimumWidth(2, 20)
        grid.setColumnMinimumWidth(10, 1)
        grid.setColumnMinimumWidth(12, 1)

        grid.setRowMinimumHeight(0, 1)  # высота пустой строки
        grid.setRowMinimumHeight(8, 10)
        grid.setRowMinimumHeight(14, 15)

        image_label = QtWidgets.QLabel("shipname")  # задаем лейбл над картинкой шип+фит
        image_fit_label = QtWidgets.QLabel("fit name")
        grid.addWidget(image_label, 1, 4, 1, 2)
        grid.addWidget(image_fit_label, 1, 6, 1, 3)

        description_label = QtWidgets.QLabel("Description")  # лейбл итоговых характеристик
        grid.addWidget(description_label, 1, 11, 1, 1, QtCore.Qt.AlignCenter)

        shiptree_label = QtWidgets.QLabel("Ships")  # лейбл дерева шипов
        grid.addWidget(shiptree_label, 1, 1, 1, 1, QtCore.Qt.AlignCenter)

        equipmenttree_label = QtWidgets.QLabel("Equipment")  # лейбл дерева эквипа
        grid.addWidget(equipmenttree_label, 8, 1, 1, 1, QtCore.Qt.AlignCenter)

        self.setLayout(grid)

    def get_data_profile(self):
        """получение данных для последующей записи в файл"""
        pass

    def set_data_profile(self):
        """вставка данных из файла в программу"""
        pass
