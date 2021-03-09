# Список деталей
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt

from Modules import styles
from PyQt5.QtWidgets import *


class DescriptionView(QtWidgets.QVBoxLayout):

    def __init__(self, parent=None):
        QtWidgets.QVBoxLayout.__init__(self, parent)

        self.damage_label = QLabel("Damage / DPS", alignment=Qt.AlignHCenter)
        self.damage = QtWidgets.QHBoxLayout()
        self.totaldamagelabel = QLabel("Damage: ", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.totaldamagevalue = QLabel("100500", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.dpsdamagelabel = QLabel("DPS: ", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.dpsdamagevalue = QLabel("100500", alignment=Qt.AlignLeft | Qt.AlignTop)

        self.resistance_label = QLabel("Resistance", alignment=Qt.AlignHCenter)
        self.shield_resistance = QtWidgets.QHBoxLayout()
        self.shield_resistance_graph = QtWidgets.QHBoxLayout()
        self.armor_resistance_graph = QtWidgets.QHBoxLayout()

        self.shield_resistance_label = QLabel("Shield: ", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.em_shield_label = QLabel("EM", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.em_shieldvalue = QLabel("0%", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.thermal_shield_label = QLabel("Thermal", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.thermal_shieldvalue = QLabel("0%", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.kinetic_shield_label = QLabel("Kinetic", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.kinetic_shieldvalue = QLabel("0%", alignment=Qt.AlignLeft | Qt.AlignTop)

        self.armor_resistance_label = QLabel("Armor: ", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.em_armorvalue = QLabel("0%", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.thermal_armorvalue = QLabel("0%", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.kinetic_armorvalue = QLabel("0%", alignment=Qt.AlignLeft | Qt.AlignTop)

        # dmg - ttl / dps
        # range wpn / devic
        # crt chnc / crt dmg
        # proc / pow
        # cap shd/ar/en
        # rech shd/ar/en
        # cap stab
        # res shd/ar
        # vel/vol fact
        # warp vel/warp stab
        # cargo




"""блок исключительно для теста"""


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.my_tree_view = DescriptionView()
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
