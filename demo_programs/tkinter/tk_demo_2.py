#!/usr/bin/env python3

import tkinter as tk
from iconipy import IconFactory

# Mininalistic example - see documentation for all options
create_icon = IconFactory(
    icon_size = 20
)

# Create the main window
root = tk.Tk()
root.title("iconipy - tk - Button Grid")

# Stores images to prevent garbage collection
image_store=[]

# Create an iterator with available icon names
name_iterator = iter(create_icon.icon_names)

# Create and place buttons in a grid
for row in range(17):
    for col in range(5):
        name = next(name_iterator)
        icon = create_icon.asTkPhotoImage(name)
        button = tk.Button(root, width=210, text=name, image=icon, compound=tk.LEFT)
        button.grid(row=row, column=col, padx=5, pady=5)
        image_store.append(icon)

# Run the application
root.mainloop()
