#!/usr/bin/env python3

# Adapted from:
# https://www.pythonguis.com/faq/built-in-qicons-pyqt/
# https://www.pythonguis.com/tutorials/pyqt6-qscrollarea/#adding-a-qscrollarea-from-code


from PySide6.QtWidgets import (QWidget, QPushButton, QScrollArea,
                             QGridLayout, QMainWindow)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6 import QtWidgets
from iconipy import IconFactory
import sys

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Setting the values here allows you to compute other values
        # based on the default sizes -> outline_width = default_font_size // 4 
        default_icon_size = 32 
        default_font_size = 32 # Icon can be smaller due to font specific whitespace 

        create_icon = IconFactory(
            icon_set = 'lucide', # See docs for available icon sets 
            icon_size = default_icon_size, 
            font_size = default_font_size,  
            font_color = (160, 160, 160, 255), # Use a value that works in darkmode or add background 
            outline_color = None, # Try 'blue', (0, 0, 255, 255) or '#0000ff'
            outline_width = 0,
            background_color = None, # Try 'lightgreen', (100, 255, 100, 255) or '#66FF66'
            background_radius = 10 # Hint: try default_icon_size // 2 for round icons
        )

        self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()                 # Widget that contains the collection of Vertical Box
        self.vbox = QGridLayout()               # The Box that contains the buttons

        icons = sorted(create_icon.icon_names)
  
        for n, name in enumerate(icons):
            btn = QPushButton(name)

            icon = QIcon(create_icon.asQPixmap(name))
            btn.setIcon(icon)
            self.vbox.addWidget(btn, int(n/4), int(n%4))
        
        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.setGeometry(100, 100, 1000, 800)
        self.setWindowTitle(f'{create_icon.icon_set_name} - Icon Set Demonstration')
        self.show()

        return

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()