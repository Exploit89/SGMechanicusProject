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
        self.setModel(self.ship_standard_item_model)
        self.header().hide()

        frigate_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.frigate_icon), 'Frigate')
        self.ship_standard_item_model.appendRow([frigate_class])

        destroyer_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.destroyer_icon), 'Destroyer')
        self.ship_standard_item_model.appendRow([destroyer_class])

        cruiser_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.cruiser_icon), 'Cruiser')
        self.ship_standard_item_model.appendRow([cruiser_class])

        battlecruiser_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.battlecruiser_icon), 'BattleCruiser')
        self.ship_standard_item_model.appendRow([battlecruiser_class])

        battleship_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.battleship_icon), 'BattleShip')
        self.ship_standard_item_model.appendRow([battleship_class])

        exclusive_ship_class = QtGui.QStandardItem('Exclusive')
        self.ship_standard_item_model.appendRow([exclusive_ship_class])

        self.t1_frigate_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.t1_icon), 'T1')
        frigate_class.appendRow(self.t1_frigate_class)

        self.t2_frigate_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.t2_icon), 'T2')
        frigate_class.appendRow(self.t2_frigate_class)

        self.t3_frigate_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.t3_icon), 'T3')
        frigate_class.appendRow(self.t3_frigate_class)

        self.t1_destroyer_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.t1_icon), 'T1')
        destroyer_class.appendRow(self.t1_destroyer_class)

        self.t2_destroyer_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.t2_icon), 'T2')
        destroyer_class.appendRow(self.t2_destroyer_class)

        self.t3_destroyer_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.t3_icon), 'T3')
        destroyer_class.appendRow(self.t3_destroyer_class)

        self.t1_cruiser_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.t1_icon), 'T1')
        cruiser_class.appendRow(self.t1_cruiser_class)

        self.t2_cruiser_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.t2_icon), 'T2')
        cruiser_class.appendRow(self.t2_cruiser_class)

        self.t3_cruiser_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.t3_icon), 'T3')
        cruiser_class.appendRow(self.t3_cruiser_class)

        self.t1_battlecruiser_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.t1_icon), 'T1')
        battlecruiser_class.appendRow(self.t1_battlecruiser_class)

        self.t2_battlecruiser_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.t2_icon), 'T2')
        battlecruiser_class.appendRow(self.t2_battlecruiser_class)

        self.t3_battlecruiser_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.t3_icon), 'T3')
        battlecruiser_class.appendRow(self.t3_battlecruiser_class)

        self.t1_battleship_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.t1_icon), 'T1')
        battleship_class.appendRow(self.t1_battleship_class)

        self.t2_battleship_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.t2_icon), 'T2')
        battleship_class.appendRow(self.t2_battleship_class)

        self.t3_battleship_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.t3_icon), 'T3')
        battleship_class.appendRow(self.t3_battleship_class)

        self.t1_exclusive_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.t1_icon), 'T1')
        exclusive_ship_class.appendRow(self.t1_exclusive_class)

        self.t2_exclusive_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.t2_icon), 'T2')
        exclusive_ship_class.appendRow(self.t2_exclusive_class)

        self.t3_exclusive_class = QtGui.QStandardItem(QtGui.QIcon(shiplist.t3_icon), 'T3')
        exclusive_ship_class.appendRow(self.t3_exclusive_class)