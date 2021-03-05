from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPlainTextEdit
# from Modules import styles


first_item_name = QtGui.QStandardItem('first_item')
second_item_name = QtGui.QStandardItem('second_item')

first_list = (first_item_name, second_item_name)

second_list = ['11', '22', '33', '44', '55']


class MyTreeView(QtWidgets.QTreeView):
    def __init__(self, parent=None):
        QtWidgets.QTreeView.__init__(self, parent)
        self.standard_item_model = QtGui.QStandardItemModel()
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        first_class = QtGui.QStandardItem('First')
        self.standard_item_model.appendRow([first_class])
        self.header().hide()
        self.setModel(self.standard_item_model)

        second_class = QtGui.QStandardItem('Second')
        self.standard_item_model.appendRow([second_class])
        self.header().hide()
        self.setModel(self.standard_item_model)

        t1_first_class = QtGui.QStandardItem('T1')
        first_class.appendRow(t1_first_class)
        for i in range(len(first_list)):
            stditem = QtGui.QStandardItem(first_list[i])
            t1_first_class.appendRow([stditem])
        self.header().hide()
        self.setModel(self.standard_item_model)

        t2_first_class = QtGui.QStandardItem('T2')
        first_class.appendRow(t2_first_class)
        self.header().hide()
        self.setModel(self.standard_item_model)

        t3_first_class = QtGui.QStandardItem('T3')
        first_class.appendRow(t3_first_class)
        self.header().hide()
        self.setModel(self.standard_item_model)

    def get_item(self, index):
        return self.standard_item_model.itemFromIndex(index)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.my_tree_view = MyTreeView()
        self.my_tree_view.clicked.connect(self.on_tree_view_click)

        self.text_edit = QPlainTextEdit()

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.my_tree_view)
        main_layout.addWidget(self.text_edit)

        self.setLayout(main_layout)

    def on_tree_view_click(self, index):
        item = self.my_tree_view.get_item(index)
        self.text_edit.appendPlainText(item.text())


if __name__ == '__main__':
    app = QApplication([])

    mw = MainWindow()
    mw.show()

    app.exec()
