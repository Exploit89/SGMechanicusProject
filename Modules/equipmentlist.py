# Списки имен эквипа
from PyQt5 import QtGui, QtWidgets, QtCore

weapon_list = ['Railgun', 'Blaster', 'Laser', 'Drone Bay', 'Launcher']
tier_weapon_list = ['T1', 'T2', 'T3']
T1_weapon_list = ['Single', 'Double']  # поработать над деревом эквипа

ammo_list = ['Railgun Charge', 'Blaster Charge', 'Laser Crystal', 'Drones', 'Missiles']
device_list = ['Enhancer', 'Extended Enhancer', 'Area Enhancer', 'Recharger', 'Extended Recharger', 'Area Recharger',
               'Extended Interference', 'Area Interference', 'Tactical', 'Exclusive Device']
component_list = ['Damage Enhancer', 'Range Enhancer', 'Electronic Enhancer', 'Shield Enhancer', 'Armor Enhancement',
                  'Piloting Enhancer', 'Exclusive Component']


class EquipmentTreeView(QtWidgets.QTreeView):

    def __init__(self, parent=None):
        QtWidgets.QTreeView.__init__(self, parent)
        self.ship_standard_item_model = QtGui.QStandardItemModel()

        self.equipmentscrollbar = """
            QScrollBar:vertical {
                border: 1px black;
                width: 5px;
                height: 100px;
                margin: 0 0 0 0;
            }
            QScrollBar::handle:vertical {
                background: #36393F;
                min-height: 20px;
            }
            """
        self.setStyleSheet(self.equipmentscrollbar)

        weapon_class = QtGui.QStandardItem('Weapon')
        for i in range(len(weapon_list)):
            std_item = QtGui.QStandardItem(weapon_list[i])
            weapon_class.appendRow([std_item])

        self.ship_standard_item_model.appendRow([weapon_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        ammo_class = QtGui.QStandardItem('Ammo')
        for i in range(len(ammo_list)):
            std_item = QtGui.QStandardItem(ammo_list[i])
            ammo_class.appendRow([std_item])

        self.ship_standard_item_model.appendRow([ammo_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        device_class = QtGui.QStandardItem('Device')
        for i in range(len(device_list)):
            std_item = QtGui.QStandardItem(device_list[i])
            device_class.appendRow([std_item])

        self.ship_standard_item_model.appendRow([device_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        component_class = QtGui.QStandardItem('Component')
        for i in range(len(component_list)):
            std_item = QtGui.QStandardItem(component_list[i])
            component_class.appendRow([std_item])

        self.ship_standard_item_model.appendRow([component_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)
