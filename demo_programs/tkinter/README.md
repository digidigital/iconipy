Hello world example for tkinter:

```python
import tkinter as tk
from iconipy import IconFactory

# Initialize IconFactory (default settings except for a custom icon size of 20)
create_icon = IconFactory(icon_size=20)

# Create the main application window
window = tk.Tk()

# Generate an icon of a globe
world_icon = create_icon.asTkPhotoImage('globe')

# Create a button with text and an icon, then add it to the window
button = tk.Button(window, text='Hello World!', image=world_icon, compound=tk.LEFT)
button.grid(row=0, column=0, padx=10, pady=10)

# Run the application's event loop
window.mainloop()
```

A bit more complex:

```python
import tkinter as tk
from iconipy import IconFactory

# Initialize IconFactory with custom settings
create_icon = IconFactory(icon_set = 'lucide',       # One of iconipy's supported icon sets 
                        icon_size = 28,              # Size in px
                        font_size = 16,              # Size in px  
                        font_color = (0, 0, 0, 255), # Black solid in RGBA values
                        outline_color = '#ff0000',   # Red as hex-string
                        outline_width = 3,           # Width in px
                        background_color = 'white',  # Colors can be set as name strings
                        background_radius = 14)      # Radius in px

# Create the main application window
window=tk.Tk()

# Create icon
bike_icon=create_icon.asTkPhotoImage('bike')

# Create a button with text and an icon, then add it to the window
button = tk.Button(window, text='No Bikes!', image=bike_icon, compound=tk.LEFT)
button.grid(row=0, column=0, padx=10, pady=10)

# Start the event loop
window.mainloop()
```
