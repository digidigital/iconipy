#!/usr/bin/env python3

import sys
import random
from iconipy import IconFactory
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, QByteArray 

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Define default attributes that are valid for all icons at a central place
        default_icon_size = 64
        default_font_size = 38
           
        # Initialize icon factories with desired settings
        # Colors can be names or tuples (R, G, B, Alpha)
        create_button_icon = IconFactory(
                                icon_set = 'lucide', 
                                icon_size = default_icon_size, 
                                font_size = default_font_size,  
                                font_color = 'red'
        )
        
        self.create_label_icon = IconFactory(
                                icon_set = 'lucide', 
                                icon_size = default_icon_size, 
                                font_size = default_font_size,  
                                font_color = (0, 0, 0, 255), # black solid
                                outline_color = 'dimgrey', 
                                outline_width = 6,
                                background_color = 'silver', 
                                background_radius = 10
        )
         
        # Create Pixmap for Button-Icon & Label       
        default_icon_name = 'circle-user-round'
        label_icon = self.create_label_icon.asQPixmap(default_icon_name)
        button_icon = create_button_icon.asQPixmap('refresh-cw')
        
        # Set window size
        self.setFixedSize(220, 180)
        self.setWindowTitle("Button and Label")
        
        # Create a vertical layout
        layout = QVBoxLayout()
        
        # Create a label for icon name
        self.text_label = QLabel(default_icon_name)
        
        # Create a label to hold an image
        self.label = QLabel()
        self.label.setPixmap(label_icon)
        
        # Create a button
        button = QPushButton('')
        button.setFixedSize(100, 30)
        button.setIcon(QIcon(button_icon))  # Set your icon here
        button.setIconSize(button.size())  # Resize the icon to match the button size
        button.clicked.connect(self.update_labels)  # Connect button click to the function
         
        # Add button and label to the layout
        layout.addWidget(self.text_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Set the layout for the window
        self.setLayout(layout)
    
    def update_labels(self):
        # Create a new pixmap for the label
        random_icon_name = random.choice(self.create_label_icon.icon_names)
        new_label_icon = self.create_label_icon.asQPixmap(random_icon_name)

        # Update labels with new pixmap and text
        self.label.setPixmap(new_label_icon)
        self.text_label.setText(random_icon_name)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
