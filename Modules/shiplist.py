# Списки имен шипов
from PyQt5 import QtGui, QtWidgets

from Modules import styles
from PyQt5.QtWidgets import *

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

t1_icon = "../Images/Icons/T1.png"
t2_icon = "../Images/Icons/T2.png"
t3_icon = "../Images/Icons/T3.png"


class ShipTreeView(QtWidgets.QTreeView):

    def __init__(self, parent=None):
        QtWidgets.QTreeView.__init__(self, parent)
        mist_shiplist_name = QtGui.QStandardItem('Mist')
        frost_shiplist_name = QtGui.QStandardItem('Frost')
        glimmer_shiplist_name = QtGui.QStandardItem('Glimmer')
        sprinkle_shiplist_name = QtGui.QStandardItem('Sprinkle')
        snowflake_shiplist_name = QtGui.QStandardItem('Snowflake')

        t1_frigate_list = (mist_shiplist_name, frost_shiplist_name, glimmer_shiplist_name)
        t2_frigate_list = (sprinkle_shiplist_name, snowflake_shiplist_name)

        self.ship_standard_item_model = QtGui.QStandardItemModel()
        self.setStyleSheet(styles.scrollbar_style)
        self.setAnimated(True)
        self.setIndentation(0)
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        frigate_class = QtGui.QStandardItem(QtGui.QIcon(frigate_icon), 'Frigate')
        self.ship_standard_item_model.appendRow([frigate_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        destroyer_class = QtGui.QStandardItem(QtGui.QIcon(destroyer_icon), 'Destroyer')
        self.ship_standard_item_model.appendRow([destroyer_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        cruiser_class = QtGui.QStandardItem(QtGui.QIcon(cruiser_icon), 'Cruiser')
        self.ship_standard_item_model.appendRow([cruiser_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        battlecruiser_class = QtGui.QStandardItem(QtGui.QIcon(battlecruiser_icon), 'BattleCruiser')
        self.ship_standard_item_model.appendRow([battlecruiser_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        battleship_class = QtGui.QStandardItem(QtGui.QIcon(battleship_icon), 'BattleShip')
        self.ship_standard_item_model.appendRow([battleship_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        exclusive_ship_class = QtGui.QStandardItem('Exclusive')
        self.ship_standard_item_model.appendRow([exclusive_ship_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        t1_frigate_class = QtGui.QStandardItem(QtGui.QIcon(t1_icon), 'T1')
        frigate_class.appendRow(t1_frigate_class)
        for i in range(len(t1_frigate_list)):
            stditem = QtGui.QStandardItem(t1_frigate_list[i])
            t1_frigate_class.appendRow([stditem])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        t2_frigate_class = QtGui.QStandardItem(QtGui.QIcon(t2_icon), 'T2')
        frigate_class.appendRow(t2_frigate_class)
        for i in range(len(t2_frigate_list)):
            stditem = QtGui.QStandardItem(t2_frigate_list[i])
            t2_frigate_class.appendRow([stditem])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        t3_frigate_class = QtGui.QStandardItem(QtGui.QIcon(t3_icon), 'T3')
        frigate_class.appendRow(t3_frigate_class)
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

    def get_item(self, index):
        return self.ship_standard_item_model.itemFromIndex(index)


"""блок исключительно для теста"""


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.my_tree_view = ShipTreeView()
        self.my_tree_view.clicked.connect(self.on_tree_view_click)

        self.text_edit = QPlainTextEdit()

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.my_tree_view)
        main_layout.addWidget(self.text_edit)  # виджет, куда нужно отправить данные

        self.setLayout(main_layout)

    def on_tree_view_click(self, index):
        """Добавляет item туда, куда нужно"""
        item = self.my_tree_view.get_item(index)
        self.text_edit.appendPlainText(item.text())  # добавление в конец списка
        print(item.text())  # вывод в консоль


if __name__ == '__main__':
    app = QApplication([])

    mw = MainWindow()
    mw.show()

    app.exec()
