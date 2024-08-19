iconipy 'Hello world!' for PyQt6:

    from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
    from PyQt6.QtGui import QIcon
    from PyQt6.QtCore import Qt
    from iconipy import IconFactory
    import sys
    
    # Initialize IconFactory (default settings except for a custom icon size of 18 and font color 'dimgrey')
    create_icon = IconFactory(icon_size=18, font_color='dimgrey')
    
    # Initialize the application
    app = QApplication(sys.argv)
    
    # Create the main window
    window = QMainWindow()
    
    # Create a central widget and set a layout
    central_widget = QWidget()
    layout = QVBoxLayout(central_widget)
    
    # Create icon as QPixmap
    globe_icon=create_icon.asQPixmap('globe')
    
    # Create a button with text and an icon
    button = QPushButton("Hello World!")
    button.setIcon(QIcon(globe_icon))
    
    # Add the button to the layout
    layout.addWidget(button)
    
    # Set the central widget
    window.setCentralWidget(central_widget)
    
    # Show the main window
    window.show()
    
    # Run the application's event loop
    sys.exit(app.exec())

Check out the other scripts in this directory for more complex examples
