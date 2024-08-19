#!/usr/bin/env python3

from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.icons import Icon
from ttkbootstrap.dialogs import MessageDialog, Messagebox
from iconipy import IconFactory
from itertools import count
from random import shuffle

# Initialze root / tkinter
root = tb.Window(themename="morph")

# Available icon sets: 'lucide', 'boxicons', 'lineicons', 
# 'material_icons_regular', 'material_icons_round_regular', 
# 'material_icons_sharp_regular', and 'material_icons_outlined_regular'

create_icon = IconFactory(icon_set = 'lucide', 
                icon_size = (20,20), 
                # font_size = 14, 
                font_color = 'white',
                # outline_color = 'black', 
                # outline_width = 2,
                # background_color = 'silver', 
                # background_radius = 10
                )

# Get icon names and shuffle them
icons = create_icon.icon_names
shuffle(icons)

# If you want to see all the icon names:
# print(icons)

# Build the GUI
root.title(f"iconipy icons - ttkbootstrap Button Demo")
root.geometry("1200x800")
root.resizable(False,False)
root.grid_columnconfigure((0, 1), weight=1)

rows = 18
buttons_per_row = 4
images=[] 
try:
    for row_counter in count():
        if row_counter == rows:
            break

        for column_counter in range(buttons_per_row):
            icon_name = icons.pop(0)
            button = tb.Button(root, width=30, text=icon_name)
            img = create_icon.asTkPhotoImage(icon_name)
            images.append(img) # Keep a reference
            button.config(image=img, compound="left") # Set the image on the left of the text
            button.grid(row=row_counter, column=column_counter, padx=5, pady=5, sticky=W)

except IndexError:
    # All icons "popped"
    pass

root.mainloop()