# Списки имен эквипа
from PyQt5 import QtGui, QtWidgets
from Modules import styles


ammo_list = ['Railgun Charge', 'Blaster Charge', 'Laser Crystal', 'Drones', 'Missiles']
device_list = ['Enhancer', 'Extended Enhancer', 'Area Enhancer', 'Recharger', 'Extended Recharger', 'Area Recharger',
               'Extended Interference', 'Area Interference', 'Tactical', 'Exclusive Device']
component_list = ['Damage Enhancer', 'Range Enhancer', 'Electronic Enhancer', 'Shield Enhancer', 'Armor Enhancement',
                  'Piloting Enhancer', 'Exclusive Component']


class EquipmentTreeView(QtWidgets.QTreeView):

    def __init__(self, parent=None):
        QtWidgets.QTreeView.__init__(self, parent)

        t1r1_s_single_combat_railgun_name = QtGui.QStandardItem('T1R1 S Single Combat Railgun')
        t1r2_s_single_combat_railgun_name = QtGui.QStandardItem('T1R2 S Single Combat Railgun')
        t1r3_s_single_combat_railgun_name = QtGui.QStandardItem('T1R3 S Single Combat Railgun')

        railgun_list = (t1r1_s_single_combat_railgun_name, t1r2_s_single_combat_railgun_name,
                        t1r3_s_single_combat_railgun_name)

        self.equipment_standard_item_model = QtGui.QStandardItemModel()
        self.setStyleSheet(styles.scrollbar_style)
        self.setAnimated(True)
        self.setIndentation(0)
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.header().hide()
        self.setModel(self.equipment_standard_item_model)

        weapon_class = QtGui.QStandardItem('Weapon')
        self.equipment_standard_item_model.appendRow([weapon_class])

        railgun_class = QtGui.QStandardItem('Railgun')
        weapon_class.appendRow(railgun_class)
        for i in range(len(railgun_list)):
            stditem = QtGui.QStandardItem(railgun_list[i])
            railgun_class.appendRow([stditem])

        ammo_class = QtGui.QStandardItem('Ammo')
        for i in range(len(ammo_list)):
            std_item = QtGui.QStandardItem(ammo_list[i])
            ammo_class.appendRow([std_item])
        self.equipment_standard_item_model.appendRow([ammo_class])

        device_class = QtGui.QStandardItem('Device')
        for i in range(len(device_list)):
            std_item = QtGui.QStandardItem(device_list[i])
            device_class.appendRow([std_item])
        self.equipment_standard_item_model.appendRow([device_class])

        component_class = QtGui.QStandardItem('Component')
        for i in range(len(component_list)):
            std_item = QtGui.QStandardItem(component_list[i])
            component_class.appendRow([std_item])
        self.equipment_standard_item_model.appendRow([component_class])
