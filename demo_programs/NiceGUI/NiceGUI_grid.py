#!/usr/bin/env python3

from nicegui import ui
from random import shuffle
from iconipy import IconFactory

# Initialize IconFactory
create_icon = IconFactory(icon_set='lucide', icon_size=(20), font_color='white')

# Get icon names and shuffle them so we get a 
# new set of icons each time we start the script
icons = create_icon.icon_names.copy()
shuffle(icons)

# Build the GUI
with ui.row().classes('justify-center'):
    ui.label(f"iconipy icons - NiceGUI Button Demo").classes('text-2xl')

rows = 15
buttons_per_row = 5

try:
    for row_counter in range(rows):
        with ui.row():
            for column_counter in range(buttons_per_row):
                if not icons:
                    break
                icon_name = icons.pop(0)          
                with ui.button().style('width: 310px'):
                    ui.image(create_icon.asPil(icon_name)).style('width: 20px; margin-right:5px;')
                    ui.label(icon_name)
            

except IndexError:
    # All icons "popped"
    pass

ui.run(title='iconipy Demo')
