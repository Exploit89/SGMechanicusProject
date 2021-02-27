# Списки имен шипов
from PyQt5 import QtGui, QtWidgets

frigate_list = ['ECD', 'NEF', 'RS', 'OE', 'USSH']
ECD_frigate_list = ['T1', 'T2', 'T3']
T1_ECD_frigate_list = ['Mist', 'Frost', 'Glimmer']

destroyer_list = ['ECD', 'NEF', 'RS', 'OE', 'USSH']
cruiser_list = ['ECD', 'NEF', 'RS', 'OE', 'USSH']
battlecruiser_list = ['ECD', 'NEF', 'RS', 'OE', 'USSH']
battleship_list = ['ECD', 'NEF', 'RS', 'OE', 'USSH']
exclusive_ship_list = ['Frigate', 'Destroyer', 'Cruiser', 'Battlecruiser', 'Battleship']

frigate_icon = "../Images/Icons/Frig.png"
destroyer_icon = "../Images/Icons/Destr.png"
cruiser_icon = "../Images/Icons/Cruis.png"
battlecruiser_icon = "../Images/Icons/BC.png"
battleship_icon = "../Images/Icons/BS.png"


class ShipTreeView(QtWidgets.QTreeView):

    def __init__(self, parent=None):
        QtWidgets.QTreeView.__init__(self, parent)
        self.ship_standard_item_model = QtGui.QStandardItemModel()

        frigate_class = QtGui.QStandardItem(QtGui.QIcon(frigate_icon), 'Frigate')
        for i in range(len(frigate_list)):
            std_item = QtGui.QStandardItem(frigate_list[i])
            frigate_class.appendRow([std_item])

        self.ship_standard_item_model.appendRow([frigate_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        destroyer_class = QtGui.QStandardItem(QtGui.QIcon(destroyer_icon), 'Destroyer')
        for i in range(len(destroyer_list)):
            std_item = QtGui.QStandardItem(destroyer_list[i])
            destroyer_class.appendRow([std_item])

        self.ship_standard_item_model.appendRow([destroyer_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        cruiser_class = QtGui.QStandardItem(QtGui.QIcon(cruiser_icon), 'Cruiser')
        for i in range(len(cruiser_list)):
            std_item = QtGui.QStandardItem(cruiser_list[i])
            cruiser_class.appendRow([std_item])

        self.ship_standard_item_model.appendRow([cruiser_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        battlecruiser_class = QtGui.QStandardItem(QtGui.QIcon(battlecruiser_icon), 'BattleCruiser')
        for i in range(len(battlecruiser_list)):
            std_item = QtGui.QStandardItem(battlecruiser_list[i])
            battlecruiser_class.appendRow([std_item])

        self.ship_standard_item_model.appendRow([battlecruiser_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        battleship_class = QtGui.QStandardItem(QtGui.QIcon(battlecruiser_icon), 'BattleShip')
        for i in range(len(battleship_list)):
            std_item = QtGui.QStandardItem(battleship_list[i])
            battleship_class.appendRow([std_item])

        self.ship_standard_item_model.appendRow([battleship_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        exclusive_ship_class = QtGui.QStandardItem('Exclusive')
        for i in range(len(exclusive_ship_list)):
            std_item = QtGui.QStandardItem(exclusive_ship_list[i])
            exclusive_ship_class.appendRow([std_item])

        self.ship_standard_item_model.appendRow([exclusive_ship_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)
