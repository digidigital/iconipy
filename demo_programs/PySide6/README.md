iconipy 'Hello world!' for PySide6:

    from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
    from PySide6.QtGui import QIcon
    from PySide6.QtCore import Qt
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

    # Try to initialize the IconFactory with custom settings
    create_icon = IconFactory(icon_set = 'lucide',       # One of iconipy's supported icon sets 
                            icon_size = 28,              # Size in px
                            font_size = 16,              # Size in px  
                            font_color = (0, 0, 0, 255), # Black solid in RGBA values
                            outline_color = '#ff0000',   # Red as hex-string
                            outline_width = 3,           # Width in px
                            background_color = 'white',  # Colors can be set as name strings
                            background_radius = 14)      # Radius in px
