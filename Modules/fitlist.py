# Списки имен шипов
from PyQt5 import QtGui, QtWidgets
from Modules import styles, shiplist


class FitTreeView(QtWidgets.QTreeView):

    def __init__(self, parent=None):
        QtWidgets.QTreeView.__init__(self, parent)
        self.ship_standard_item_model = QtGui.QStandardItemModel()
        self.setStyleSheet(styles.scrollbar_style)
        self.setAnimated(True)
        self.setIndentation(0)
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        frigate_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.frigate_icon), 'Frigate')
        self.ship_standard_item_model.appendRow([frigate_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        destroyer_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.destroyer_icon), 'Destroyer')
        self.ship_standard_item_model.appendRow([destroyer_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        cruiser_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.cruiser_icon), 'Cruiser')
        self.ship_standard_item_model.appendRow([cruiser_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        battlecruiser_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.battlecruiser_icon), 'BattleCruiser')
        self.ship_standard_item_model.appendRow([battlecruiser_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        battleship_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.battleship_icon), 'BattleShip')
        self.ship_standard_item_model.appendRow([battleship_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        exclusive_ship_class = QtGui.QStandardItem('Exclusive')
        self.ship_standard_item_model.appendRow([exclusive_ship_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        self.t1_frigate_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.t1_icon), 'T1')
        frigate_class.appendRow(self.t1_frigate_class)
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        self.t2_frigate_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.t2_icon), 'T2')
        frigate_class.appendRow(self.t2_frigate_class)
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        t3_frigate_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.t3_icon), 'T3')
        frigate_class.appendRow(t3_frigate_class)
        self.header().hide()
        self.setModel(self.ship_standard_item_model)
