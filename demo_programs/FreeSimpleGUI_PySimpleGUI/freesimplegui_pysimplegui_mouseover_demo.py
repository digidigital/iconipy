#!/usr/bin/env python3

from iconipy import IconFactory
import random
try:
    import FreeSimpleGUI as sg
except:
    import PySimpleGUI as sg # Tested with version 4.60    
    
# Define default attributes that are valid for all icons in one central place
default_icon_size = (60,25)
default_font_size = 18
default_radius = 5

# Initialize icon factory with desired settings
# Colors can be names or tuples (R, G, B, Alpha)
create_icon = IconFactory(icon_set = 'lucide', 
                        icon_size = default_icon_size, 
                        font_size = default_font_size,  
                        font_color = (0, 0, 0, 255), # black solid
                        outline_color = 'dimgrey', 
                        outline_width = 2,
                        background_color = 'silver', 
                        background_radius = default_radius)

create_mouseover_icon = IconFactory(icon_set = 'lucide', 
                        icon_size = default_icon_size, 
                        font_size = default_font_size,  
                        font_color = (255,255,255,255), # white solid
                        outline_color = 'silver', 
                        outline_width = 2,
                        background_color = 'dimgrey', 
                        background_radius = default_radius)

# Dictionary containing icon names for normal and mouseover state
# Hint: The icon names for the icon set 'lucide' are listed here -> https://lucide.dev/icons/
button_cfg ={
    '-HOME_BUTTON-':('house', 'house'),
    '-SETTINGS_BUTTON-':('settings','settings'),
    '-NOTEBOOK_BUTTON-':('notebook','notebook-pen'),
    '-EXIT_BUTTON-':('door-closed','door-open'),   
    }

# Create the icons
button_icons = {}
for button_name, icon_names in button_cfg.items():
    button_icons[button_name] = (create_icon.asBytes(icon_names[0]), create_mouseover_icon.asBytes(icon_names[1]))

# Create button_row (will be added to layout in the next step)
button_row =[]
for button_name, icons in button_icons.items():
    # Add one sg.Image for each button, set key to button name and enable events 
    button_row.append(sg.Image(icons[0], key = button_name, enable_events = True)) 


# GUI-Layout 
layout = [
    button_row,
    [sg.Text('Last event:', key='-EVENT_INFO-')], 
]

# Create Window
window = sg.Window('iconipy Mouseover-Demo', layout, size = (300,65), element_justification = 'center', finalize = True)

# Bind tkinter events to our buttons
for button_key in button_cfg.keys():
    window[button_key].bind('<Enter>', 'mouse_enter')
    window[button_key].bind('<Leave>', 'mouse_leave')

# Event loop
while True:
    event, values = window.read()

    if event in (sg.WINDOW_CLOSED, '-EXIT_BUTTON-'):
        break

    if '_BUTTON-' in event and 'mouse' in event:
        button_key = event[:-11]
        if 'mouse_leave' in event: # Set normal icon
            window[button_key].update(button_icons[button_key][0])
        elif 'mouse_enter' in event: # Set mouseover icon
            window[button_key].update(button_icons[button_key][1])
        else: # Mouse click
            pass # or do something e.g, play "click" sound  
    
    # Add your event checking code here  
    
    window['-EVENT_INFO-'].update(f'Last event: {event}')
         
# Close window
window.close()