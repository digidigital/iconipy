#!/usr/bin/env python3

from iconipy import IconFactory
from itertools import count
from random import shuffle
from guizero import App, Box, Picture, Text
from PIL import ImageTk


# Initialize IconFactory with parameters that resemble a typical traffic sign
my_icons = IconFactory(
        icon_set= 'lucide', # Available icon sets: 'lucide', 'boxicons', 'lineicons', etc.
        icon_size=(30,30), 
        font_size=16,
        font_color=(0, 0, 0, 255),
        outline_color='red',
        outline_width=3,
        background_color='white',
        background_radius=15
    )

# Shuffle icons
icons = my_icons.icon_names
shuffle(icons)

# App setup
app = App(title=f"iconipy - guizero Demo", width=1500, height=650)
button_box = Box(app, layout="grid")

rows = 20
icons_per_row = 4

try:
    for row_counter in count():
        if row_counter == rows:
            break

        for column_counter in range(icons_per_row):
            icon_name = icons.pop(0)

            # Generate the icon as a TkPhotoImage image
            icon_image = my_icons.asTkPhotoImage(icon_name)

            # Add a Picture widget to display the icon
            Picture(button_box, image=icon_image, grid=[column_counter * 2, row_counter])

            # Add a Text widget to display the icon name
            Text(button_box, text=icon_name, grid=[column_counter * 2 + 1, row_counter])
            
except IndexError:
    # All icons "popped"
    pass

app.display()
