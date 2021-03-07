# Основной виджет
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

from Modules import shiplist, equipmentlist, styles, fitlist, ships_tuples, descriptionlist


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

        self.fittreebox = fitlist.FitTreeView()  # определяем виджет для добавления списка фитов

        ship_tab = QtWidgets.QTabWidget()
        ship_tab.addTab(self.shiptreebox, "Ship")  # страница шипов
        ship_tab.addTab(self.fittreebox, "Fit")  # страница фитов
        shiptree.addWidget(ship_tab)  # добавляем список шипов
        ship_tab.setCurrentIndex(0)
        ship_tab.setStyleSheet(styles.tab_style)

        equipmenttree = QtWidgets.QVBoxLayout()  # Дерево эквипа
        frame_equipmenttree = QtWidgets.QFrame()  # Рамка
        frame_equipmenttree.setFixedSize(200, 230)
        frame_equipmenttree.setLayout(equipmenttree)
        grid.addWidget(frame_equipmenttree, 10, 1, 4, 1)
        self.equipmenttreebox = equipmentlist.EquipmentTreeView()

        equipmenttree.addWidget(self.equipmenttreebox)  # Добавляем кнопку

        main_image_frame = QtWidgets.QFrame()  # рамка для главной картинки
        main_image_frame.setFixedSize(250, 250)
        main_image_frame.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(main_image_frame, 2, 3, 6, 6)

        self.pixmap = QPixmap("../Images/SGM_logo.png")  # загрузка(путь) начальной картинки шипа
        self.imagelabel = QLabel(self, alignment=Qt.AlignCenter)
        self.imagelabel.setScaledContents(True)
        self.imagelabel.setPixmap(self.pixmap)  # установка начальной картинки
        hmain_image = QtWidgets.QHBoxLayout()
        hmain_image.addWidget(self.imagelabel)
        vmain_image = QtWidgets.QVBoxLayout(self)
        vmain_image.addLayout(hmain_image)
        vmain_image.addStretch()
        self.setLayout(hmain_image)

        main_image_frame.setLayout(vmain_image)

        self.descriptiontree = descriptionlist.DescriptionView()
        description_frame = QtWidgets.QFrame()  # рамка для показателей
        description_frame.setFixedSize(300, 500)
        description_frame.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        description_frame.setLayout(self.descriptiontree)
        grid.addWidget(description_frame, 2, 12, 12, 1)

        self.descriptiontree.addWidget(self.descriptiontree.damage_label)
        self.descriptiontree.addLayout(self.descriptiontree.damage, QtCore.Qt.AlignTop)
        self.descriptiontree.damage.addWidget(self.descriptiontree.totaldamagelabel)
        self.descriptiontree.damage.addWidget(self.descriptiontree.totaldamagevalue)
        self.descriptiontree.damage.addWidget(self.descriptiontree.dpsdamagelabel)
        self.descriptiontree.damage.addWidget(self.descriptiontree.dpsdamagevalue)

        self.descriptiontree.addWidget(self.descriptiontree.resistance_label)
        self.descriptiontree.addLayout(self.descriptiontree.shield_resistance, QtCore.Qt.AlignTop)
        self.descriptiontree.shield_resistance.addWidget(QLabel(""))
        self.descriptiontree.shield_resistance.addWidget(self.descriptiontree.em_shield_label)
        self.descriptiontree.shield_resistance.addWidget(self.descriptiontree.thermal_shield_label)
        self.descriptiontree.shield_resistance.addWidget(self.descriptiontree.kinetic_shield_label)
        self.descriptiontree.addLayout(self.descriptiontree.shield_resistance_graph, QtCore.Qt.AlignTop)
        self.descriptiontree.shield_resistance_graph.addWidget(self.descriptiontree.shield_resistance_label)
        self.descriptiontree.shield_resistance_graph.addWidget(self.descriptiontree.em_shieldvalue)
        self.descriptiontree.shield_resistance_graph.addWidget(self.descriptiontree.thermal_shieldvalue)
        self.descriptiontree.shield_resistance_graph.addWidget(self.descriptiontree.kinetic_shieldvalue)
        self.descriptiontree.addLayout(self.descriptiontree.armor_resistance_graph, QtCore.Qt.AlignTop)
        self.descriptiontree.armor_resistance_graph.addWidget(self.descriptiontree.armor_resistance_label)
        self.descriptiontree.armor_resistance_graph.addWidget(self.descriptiontree.em_armorvalue)
        self.descriptiontree.armor_resistance_graph.addWidget(self.descriptiontree.thermal_armorvalue)
        self.descriptiontree.armor_resistance_graph.addWidget(self.descriptiontree.kinetic_armorvalue)


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

        ammo_frame1 = QtWidgets.QFrame()
        ammo_frame1.setFixedSize(50, 50)
        ammo_frame1.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(ammo_frame1, 14, 7, 1, 1)

        ammo_frame2 = QtWidgets.QFrame()
        ammo_frame2.setFixedSize(50, 50)
        ammo_frame2.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(ammo_frame2, 14, 8, 1, 1)

        ammo_frame3 = QtWidgets.QFrame()
        ammo_frame3.setFixedSize(50, 50)
        ammo_frame3.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(ammo_frame3, 14, 9, 1, 1)

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

        ammo_slot_label = QtWidgets.QLabel("Ammo")
        grid.addWidget(ammo_slot_label, 13, 7, 1, 3, QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom)

        self.setLayout(grid)

    def on_tree_view_click(self, index):
        item = self.shiptreebox.get_item(index)
        pointerQStandardItem = self.shiptreebox.ship_standard_item_model.itemFromIndex(index)
        print(f'{item.text():>5}, {pointerQStandardItem}')  # pointerQStandardItem | :>5 это размер отступа
        print(item.text())  # Имя объекта
        print(item.row())  # Номер строки объекта (возможно надо еще поработать, чтобы не было конфликтов)
        # print(item.flat)

        shiptuple = ships_tuples.allships_parts  # словарь с кортежами шипов
        shiptuple2 = ships_tuples.allships  # кортеж с кортежами шипов

        itemname = str(item.text()).lower()  # приводим имя объекта в строку с маленькой буквы
        itemrow = int(item.row())  # приводим номер строки объекта в число (получить через условия конкретный индекс)

        if itemname in shiptuple:
            self.newpixmap = QPixmap(shiptuple2[itemrow][9])
            self.imagelabel.setPixmap(self.newpixmap)
            self.image_label.setText(item.text())  # Задаем название шипа над картинкой
        else:
            pass

    def get_data_profile(self):
        """получение данных для последующей записи в файл"""
        pass

    def set_data_profile(self):
        """вставка данных из файла в программу"""
        pass
