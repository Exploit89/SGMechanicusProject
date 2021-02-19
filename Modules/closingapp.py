def closeEvent(e):
    result = QtWidgets.QMessageBox.question(main_window, "Closing confirmation",
                                            "Do you really want to close window?",
                                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                            QtWidgets.QMessageBox.No)
    if result == QtWidgets.QMessageBox.Yes:
        e.accept()
        QtWidgets.QWidget.closeEvent(main_window, e)
    else:
        e.ignore()