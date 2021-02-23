# Основной виджет
from PyQt5 import QtCore, QtGui, QtWidgets


class Widget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        grid = QtWidgets.QGridLayout()
        grid.setSpacing(5)

        shiptree = QtWidgets.QVBoxLayout()
        frame_shiptree = QtWidgets.QFrame()
        frame_shiptree.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        frame_shiptree.setFixedSize(100, 300)
        frame_shiptree.setLayout(shiptree)
        grid.addWidget(frame_shiptree, 2, 1, 6, 1)

        equipmenttree = QtWidgets.QVBoxLayout()
        frame_equipmenttree = QtWidgets.QFrame()
        frame_equipmenttree.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        frame_equipmenttree.setFixedSize(100, 200)
        frame_equipmenttree.setLayout(equipmenttree)
        grid.addWidget(frame_equipmenttree, 10, 1, 4, 1)

        button1 = QtWidgets.QPushButton("Shipname1")  # определяем кнопку
        button2 = QtWidgets.QPushButton("Shipname2")  # определяем кнопку
        button3 = QtWidgets.QPushButton("Shipname3")  # определяем кнопку
        button4 = QtWidgets.QPushButton("Shipname4")  # определяем кнопку
        button5 = QtWidgets.QPushButton("Shipname5")  # определяем кнопку

        shiptree.addWidget(button1)
        shiptree.addWidget(button2)
        shiptree.addWidget(button3)
        shiptree.addWidget(button4)
        shiptree.addWidget(button5)

        button01 = QtWidgets.QPushButton("equip1")  # определяем кнопку
        button02 = QtWidgets.QPushButton("equip2")  # определяем кнопку
        button03 = QtWidgets.QPushButton("equip3")  # определяем кнопку
        button04 = QtWidgets.QPushButton("equip4")  # определяем кнопку
        button05 = QtWidgets.QPushButton("equip5")  # определяем кнопку

        equipmenttree.addWidget(button01)
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

        self.setLayout(grid)
