# Списки имен шипов

frigate_list = ['ECD', 'NEF', 'RS', 'OE', 'USSH']
ECD_frigate_list = ['T1', 'T2', 'T3']
T1_ECD_frigate_list = ['Mist', 'Frost', 'Glimmer']

destroyer_list = ['ECD', 'NEF', 'RS', 'OE', 'USSH']
cruiser_list = ['ECD', 'NEF', 'RS', 'OE', 'USSH']
battlecruiser_list = ['ECD', 'NEF', 'RS', 'OE', 'USSH']
battleship_list = ['ECD', 'NEF', 'RS', 'OE', 'USSH']
exclusive_list = ['Frigate', 'Destroyer', 'Cruiser', 'Battlecruiser', 'Battleship']

from PyQt5 import QtGui, QtWidgets
import sys


#app = QtWidgets.QApplication(sys.argv)
#window = QtWidgets.QWidget()
#window.setWindowTitle("QStandardItemModel")
#ship_tree_view = QtWidgets.QTreeView()
class ship_tree_view(QtWidgets.QTreeView):

    def __init__(self, parent=None):
        QtWidgets.QTreeView.__init__(self, parent)
        self.ship_standard_item_model = QtGui.QStandardItemModel()

        frigate_icon = "../Images/Icons/Frig.png"

        ship_class = QtGui.QStandardItem(QtGui.QIcon(frigate_icon), 'Frigate')
        for i in range(len(frigate_list)):
            std_item = QtGui.QStandardItem(frigate_list[i])
            ship_class.appendRow([std_item])

        self.ship_standard_item_model.appendRow([ship_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

#ship_tree_view.setColumnWidth(0, 300)
#ship_tree_view.resize(400, 300)
#window.show()
#sys.exit(app.exec_())