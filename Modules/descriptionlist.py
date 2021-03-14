# Список деталей
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt

from Modules import styles
from PyQt5.QtWidgets import *


class DescriptionView(QtWidgets.QVBoxLayout):

    def __init__(self, parent=None):
        QtWidgets.QVBoxLayout.__init__(self, parent)

        self.damage_label = QLabel("Weapon", alignment=Qt.AlignHCenter)
        self.damage = QtWidgets.QHBoxLayout()
        self.totaldamagelabel = QLabel("Damage: ", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.totaldamagevalue = QLabel("100500", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.dpsdamagelabel = QLabel("DPS: ", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.dpsdamagevalue = QLabel("100500", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.rangelabel = QLabel("Range: ", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.rangevalue = QLabel("100 km", alignment=Qt.AlignLeft | Qt.AlignTop)

        self.crit = QtWidgets.QHBoxLayout()
        self.crit_chancelabel = QLabel("Crit chance: ", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.crit_chancevalue = QLabel("100%", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.crit_damagelabel = QLabel("Crit DMG: ", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.crit_damagevalue = QLabel("300%", alignment=Qt.AlignLeft | Qt.AlignTop)

        self.procpower_label = QLabel("Ship resources", alignment=Qt.AlignHCenter)
        self.proc = QtWidgets.QHBoxLayout()
        self.processorlabel = QLabel("Processor: ", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.processor_data = QLabel("0 / 0", alignment=Qt.AlignLeft | Qt.AlignTop)

        self.processorvalue = QtWidgets.QProgressBar(self.processorlabel)
        self.processorvalue.setFixedSize(280, 5)
        self.processorvalue.setTextVisible(False)
        self.processorvalue.setMaximum(100)
        self.processorvalue.setValue(10)
        self.processorvalue.setStyleSheet(styles.proc_style)

        self.power = QtWidgets.QHBoxLayout()
        self.powerlabel = QLabel("Power: ", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.power_data = QLabel("0 / 0", alignment=Qt.AlignLeft | Qt.AlignTop)

        self.powervalue = QtWidgets.QProgressBar(self.powerlabel)
        self.powervalue.setFixedSize(280, 5)
        self.powervalue.setTextVisible(False)
        self.powervalue.setMaximum(100)
        self.powervalue.setValue(10)
        self.powervalue.setStyleSheet(styles.power_style)

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

        self.capacity_label = QLabel("Capacity/Recharge (auto / self / projector)", alignment=Qt.AlignHCenter)
        self.shield_capacitylayout = QtWidgets.QHBoxLayout()
        self.shield_capacitylabel = QLabel("Shield: ", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.shield_capacityvalue = QLabel("100000", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.shield_rechargevalue_auto = QLabel("100 p/s", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.shield_rechargevalue_self = QLabel("100 p/s", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.shield_rechargevalue_projector = QLabel("100 p/s", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.armor_capacitylayout = QtWidgets.QHBoxLayout()
        self.armor_capacitylabel = QLabel("Armor: ", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.armor_capacityvalue = QLabel("200000", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.armor_rechargevalue_auto = QLabel("0 p/s", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.armor_rechargevalue_self = QLabel("50 p/s", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.armor_rechargevalue_projector = QLabel("100 p/s", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.energy_capacitylayout = QtWidgets.QHBoxLayout()
        self.energy_capacitylabel = QLabel("Energy: ", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.energy_capacityvalue = QLabel("0", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.energy_rechargevalue_auto = QLabel("250 p/s", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.energy_rechargevalue_self = QLabel("100 p/s", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.energy_rechargevalue_projector = QLabel("300 p/s", alignment=Qt.AlignLeft | Qt.AlignTop)

        self.capastab_label = QLabel("Energy Stability", alignment=Qt.AlignHCenter)
        self.capastablayout = QHBoxLayout()
        self.capastab_passivelabel = QLabel("Passive: ", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.capastab_passivevalue = QLabel("130 sec", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.capastab_activelabel = QLabel("Active: ", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.capastab_activevalue = QLabel("240 sec", alignment=Qt.AlignLeft | Qt.AlignTop)

        self.velocity_label = QLabel("Velocity / Volume / Warp speed", alignment=Qt.AlignHCenter)
        self.velocity_passive_layout = QHBoxLayout()
        self.velocity_passivelabel = QLabel("Velocity Passive: ", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.velocity_passivevalue = QLabel("800 m/s", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.velocity_maximum_layout = QHBoxLayout()
        self.velocity_maximumlabel = QLabel("Velocity Max: ", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.velocity_maximumvalue = QLabel("4500 m/s", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.volumefactor_layout = QHBoxLayout()
        self.volumefactor_label = QLabel("Volume factor: ", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.volumefactor_value = QLabel("130", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.warp_layout = QHBoxLayout()
        self.warp_label = QLabel("Warp speed: ", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.warp_value = QLabel("4,5 AU/s", alignment=Qt.AlignLeft | Qt.AlignTop)

        # range device?
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
