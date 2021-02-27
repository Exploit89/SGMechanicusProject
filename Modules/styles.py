# Оформление программы
"""Стили"""

"""Стиль полосы загрузки"""
progressbar_style = """
QProgressBar{
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