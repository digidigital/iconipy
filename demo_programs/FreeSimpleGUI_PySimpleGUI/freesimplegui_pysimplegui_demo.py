#!/usr/bin/env python3

from iconipy import IconFactory
import random
try:
    import FreeSimpleGUI as sg
except:
    import PySimpleGUI as sg # Tested with version 4.60    
    
# Define default attributes that are valid for all icons at a central place
default_icon_size = 54
default_font_size = 30
radius_alternatives = [0, 10, 32] # corners, rounded edges, circular
default_radius = random.choice(radius_alternatives) # choose one option randomly

# Initialize icon factory with desired settings
# Colors can be names or tuples (R, G, B, Alpha)
create_icon = IconFactory(icon_set = 'lucide', 
                        icon_size = default_icon_size, 
                        font_size = default_font_size,  
                        font_color = (0, 0, 0, 255), # black solid
                        outline_color = 'dimgrey', 
                        outline_width = 6,
                        background_color = 'silver', 
                        background_radius = default_radius)

create_mouseover_icon = IconFactory(icon_set = 'lucide', 
                        icon_size = default_icon_size, 
                        font_size = default_font_size,  
                        font_color = (255,255,255,255), # white solid
                        outline_color = 'silver', 
                        outline_width = 8,
                        background_color = 'dimgrey', 
                        background_radius = default_radius)

# Create regular icons
# Hint: The icon names for the icon set 'lucide' are listed here -> https://lucide.dev/icons/
icon_toggle_left = create_icon.asBytes('toggle-left')
icon_toggle_right = create_icon.asBytes('toggle-right')
icon_door = create_icon.asBytes('door-closed')

# Create mouseove icon
icon_door_mouseover = create_mouseover_icon.asBytes('door-open')

# Initial switch state is "left"
toggle_switch_state = "left"

# GUI-Layout 
layout = [
    [sg.Image(icon_toggle_left, key='-SWITCH-', tooltip='Click icon to switch', enable_events=True), 
     sg.Image(icon_door, key='-DOOR-', enable_events=True)],
    [sg.Text('Switch position: left', key='-SWITCH_POSITION-')],
    [sg.Text('Last event:', key='-EVENT_INFO-')], 
]

# Create Window
window = sg.Window('iconipy Button-Demo', layout, size = (240,125), element_justification = 'center', finalize = True)

# Bind tkinter events to our power-icon
window['-DOOR-'].bind('<Enter>', 'mouse_enter')
window['-DOOR-'].bind('<Leave>', 'mouse_leave')

# Event loop
while True:
    event, values = window.read()

    if event in (sg.WINDOW_CLOSED,):
        break
    
    if event == '-SWITCH-':
        if toggle_switch_state == 'left':
            window['-SWITCH-'].update(icon_toggle_right)
            toggle_switch_state = 'right'
            # Add code thats does something when switch is on the right here
        else:
            window['-SWITCH-'].update(icon_toggle_left)
            toggle_switch_state = 'left'
            # Add code thats does something when switch is on the left here

        # Add code that does something any time the switch was clicked here
        window['-SWITCH_POSITION-'].update(f'Switch position: {toggle_switch_state}')
         
    if '-DOOR-' in event:
        if 'mouse_leave' in event:
            window['-DOOR-'].update(icon_door)
        elif 'mouse_enter' in event:
            window['-DOOR-'].update(icon_door_mouseover)
        else: # Mouse click
            break
    
    window['-EVENT_INFO-'].update(f'Last event: {event}')
         
# Close window
window.close()