# Основной виджет
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

from Modules import shiplist, equipmentlist, styles, fitlist, ships_tuples


class MainWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        grid = QtWidgets.QGridLayout()  # Создаем сетку для всех элементов главного виджета
        grid.setSpacing(1)  # Расстояние между элементами сетки

        shiptree = QtWidgets.QVBoxLayout()  # Дерево шипов
        frame_shiptree = QtWidgets.QFrame()  # Рамка
        frame_shiptree.setFixedSize(200, 250)
        frame_shiptree.setLayout(shiptree)
        grid.addWidget(frame_shiptree, 2, 1, 6, 1)
        self.shiptreebox = shiplist.ShipTreeView()  # определяем виджет для добавления списка шипов
        self.shiptreebox.clicked.connect(self.on_tree_view_click)

        fittreebox = fitlist.FitTreeView()  # определяем виджет для добавления списка фитов

        equipmenttree = QtWidgets.QVBoxLayout()  # Дерево эквипа
        frame_equipmenttree = QtWidgets.QFrame()  # Рамка
        frame_equipmenttree.setFixedSize(200, 230)
        frame_equipmenttree.setLayout(equipmenttree)
        grid.addWidget(frame_equipmenttree, 10, 1, 4, 1)
        equipmenttreebox = equipmentlist.EquipmentTreeView()

        ship_tab = QtWidgets.QTabWidget()
        ship_tab.addTab(self.shiptreebox, "Ship")  # страница шипов
        ship_tab.addTab(fittreebox, "Fit")  # страница фитов
        shiptree.addWidget(ship_tab)  # добавляем список шипов
        ship_tab.setCurrentIndex(0)
        ship_tab.setStyleSheet(styles.tab_style)

        equipmenttree.addWidget(equipmenttreebox)  # Добавляем кнопку

        main_image_frame = QtWidgets.QFrame()  # рамка для главной картинки
        main_image_frame.setFixedSize(250, 250)
        main_image_frame.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(main_image_frame, 2, 3, 6, 6)

        self.pixmap = QPixmap("../Images/SGM_logo.png")  # загрузка картинки шипа ships_tuples.mist.ship_image
        imagelabel = QLabel(self, alignment=Qt.AlignCenter)
        imagelabel.setScaledContents(True)
        imagelabel.setPixmap(self.pixmap)
        hmain_image = QtWidgets.QHBoxLayout()
        hmain_image.addWidget(imagelabel)
        vmain_image = QtWidgets.QVBoxLayout(self)
        vmain_image.addLayout(hmain_image)
        vmain_image.addStretch()
        self.setLayout(hmain_image)

        main_image_frame.setLayout(vmain_image)

        description_frame = QtWidgets.QFrame()  # рамка для показателей
        description_frame.setFixedSize(300, 500)
        description_frame.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(description_frame, 2, 12, 12, 1)

        superdevice_frame = QtWidgets.QFrame()  # рамка для супердевайса
        superdevice_frame.setFixedSize(50, 50)
        superdevice_frame.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(superdevice_frame, 2, 9, 1, 1)

        tactical_component_frame = QtWidgets.QFrame()  # рамка для тактического компонента
        tactical_component_frame.setFixedSize(50, 50)
        tactical_component_frame.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(tactical_component_frame, 4, 9, 1, 1)

        component_frame1 = QtWidgets.QFrame()
        component_frame1.setFixedSize(50, 50)
        component_frame1.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(component_frame1, 10, 3, 1, 1)

        component_frame2 = QtWidgets.QFrame()
        component_frame2.setFixedSize(50, 50)
        component_frame2.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(component_frame2, 10, 4, 1, 1)

        component_frame3 = QtWidgets.QFrame()
        component_frame3.setFixedSize(50, 50)
        component_frame3.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(component_frame3, 10, 5, 1, 1)

        component_frame4 = QtWidgets.QFrame()
        component_frame4.setFixedSize(50, 50)
        component_frame4.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(component_frame4, 12, 3, 1, 1)

        component_frame5 = QtWidgets.QFrame()
        component_frame5.setFixedSize(50, 50)
        component_frame5.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(component_frame5, 12, 4, 1, 1)

        component_frame6 = QtWidgets.QFrame()
        component_frame6.setFixedSize(50, 50)
        component_frame6.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(component_frame6, 12, 5, 1, 1)

        component_frame7 = QtWidgets.QFrame()
        component_frame7.setFixedSize(50, 50)
        component_frame7.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(component_frame7, 14, 3, 1, 1)

        weapon_frame1 = QtWidgets.QFrame()
        weapon_frame1.setFixedSize(50, 50)
        weapon_frame1.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(weapon_frame1, 10, 7, 1, 1)

        weapon_frame2 = QtWidgets.QFrame()
        weapon_frame2.setFixedSize(50, 50)
        weapon_frame2.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(weapon_frame2, 10, 8, 1, 1)

        weapon_frame3 = QtWidgets.QFrame()
        weapon_frame3.setFixedSize(50, 50)
        weapon_frame3.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(weapon_frame3, 10, 9, 1, 1)

        device_frame1 = QtWidgets.QFrame()
        device_frame1.setFixedSize(50, 50)
        device_frame1.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(device_frame1, 12, 7, 1, 1)

        device_frame2 = QtWidgets.QFrame()
        device_frame2.setFixedSize(50, 50)
        device_frame2.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(device_frame2, 12, 8, 1, 1)

        device_frame3 = QtWidgets.QFrame()
        device_frame3.setFixedSize(50, 50)
        device_frame3.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(device_frame3, 12, 9, 1, 1)

        grid.setColumnMinimumWidth(0, 1)  # ширина пустой колонки
        grid.setColumnMinimumWidth(2, 20)
        grid.setColumnMinimumWidth(6, 5)
        grid.setColumnMinimumWidth(11, 20)
        grid.setColumnMinimumWidth(13, 1)

        grid.setRowMinimumHeight(0, 1)  # высота пустой строки
        grid.setRowMinimumHeight(8, 10)
        grid.setRowMinimumHeight(15, 25)

        self.image_label = QtWidgets.QLabel("shipname")  # задаем лейбл над картинкой шип+фит
        image_fit_label = QtWidgets.QLabel("fit name")
        grid.addWidget(self.image_label, 1, 3, 1, 2)
        grid.addWidget(image_fit_label, 1, 5, 1, 3)

        description_label = QtWidgets.QLabel("Description")  # лейбл итоговых характеристик
        grid.addWidget(description_label, 1, 12, 1, 1, QtCore.Qt.AlignCenter)

        """в сетке grid по координатам 1-1-1-1 есть место для кнопок"""

        equipmenttree_label = QtWidgets.QLabel("Equipment")  # лейбл дерева эквипа
        grid.addWidget(equipmenttree_label, 9, 1, 1, 1, QtCore.Qt.AlignCenter)

        superdevice_label = QtWidgets.QLabel("S-Device")
        grid.addWidget(superdevice_label, 1, 9, 1, 1, QtCore.Qt.AlignCenter)

        tactical_component_label = QtWidgets.QLabel("Tactical")
        grid.addWidget(tactical_component_label, 3, 9, 1, 1, QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom)

        component_slot_label = QtWidgets.QLabel("Components")
        grid.addWidget(component_slot_label, 9, 3, 1, 3, QtCore.Qt.AlignCenter)

        weapon_slot_label = QtWidgets.QLabel("Weapons")
        grid.addWidget(weapon_slot_label, 9, 7, 1, 3, QtCore.Qt.AlignCenter)

        device_slot_label = QtWidgets.QLabel("Devices")
        grid.addWidget(device_slot_label, 11, 7, 1, 3, QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom)

        self.setLayout(grid)

        # self.my_tree_view = ShipTreeView()
        # self.my_tree_view.clicked.connect(self.on_tree_view_click)

    def on_tree_view_click(self, index):
        item = self.shiptreebox.get_item(index)
        pointerQStandardItem = self.shiptreebox.ship_standard_item_model.itemFromIndex(index)
        print(f'Вы кликнули -> {item.text():>8}, --> pointerQStandardItem -> {pointerQStandardItem}')
        print(item.text())  # Имя объекта

        self.image_label.setText(item.text())  # Задаем название шипа над картинкой
        shiptuple = ships_tuples.allships
        lowert = item.text().lower
        print(lowert)
        if lowert in shiptuple:
            self.pixmap.swap(shiptuple.mist[9])
        else:
            pass


    def get_data_profile(self):
        """получение данных для последующей записи в файл"""
        pass

    def set_data_profile(self):
        """вставка данных из файла в программу"""
        pass
