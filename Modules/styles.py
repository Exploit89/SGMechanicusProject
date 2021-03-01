# Оформление программы
"""Стили"""

menu_style = """
QMenuBar {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #36393F, stop:1 #2F3136);
    color: gray;
    border: 0px solid #36393F;
}
QMenuBar::item:selected {
    background: #36393F;
    border: 1px solid #DCDDDE;
    color: white;
}
"""

window_style = """
QMainWindow {
    background-color: #36393F;
}
QMainWindow::separator {
    background: #36393F;
}
QMenu {
    background-color: #36393F;
    color: #DCDDDE;
}
QMenu::item:selected {
    background-color: #2F3136;
    border: 1px solid #DCDDDE;
    color: white;
}
QWidget {
    background: #36393F;
    color: #DCDDDE;
}
QToolBar {
    border-bottom: 1px solid #36393F;
}
"""

"""Стиль полосы загрузки"""
progressbar_style = """
QProgressBar {
    background-color: #36393F; 
    border: 1px black;
    border-radius: 1px;
}

QProgressBar::chunk {
    background-color: #EC6936;
}
"""


"""Стиль скроллбара"""
scrollbar_style = """
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