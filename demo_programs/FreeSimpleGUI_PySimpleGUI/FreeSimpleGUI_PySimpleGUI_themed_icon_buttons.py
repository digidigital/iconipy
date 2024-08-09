#!/usr/bin/env python3
from iconipy import IconFactory
from dataclasses import dataclass
from random import choice

try:
    import FreeSimpleGUI as sg
except:
    import PySimpleGUI as sg # Tested with version 4.60    

# set a random theme 
sg.theme(choice(sg.theme_list()))
    
# Class needed to provide dummy coordinates for the TooltipObject later on    
@dataclass
class Coordinates:
    x: int = 0
    y: int = 0
     
# Define default attributes that are valid for all icons in one central place
default_icon_size = (60,22)
default_font_size = 20

# Initialize IconFactory 
create_button_icon = IconFactory(icon_set = 'boxicons', 
                        icon_size = default_icon_size, 
                        font_size = default_font_size,  
                        font_color = sg.theme_button_color_text())

create_button_mouseover_icon = IconFactory(icon_set = 'boxicons', 
                        icon_size = default_icon_size, 
                        font_size = default_font_size,  
                        font_color = sg.theme_button_color_background())

# Initialize a second IconFactory for the application icon
create_app_icon = IconFactory(icon_set = 'lucide', 
                        icon_size = 64, 
                        font_color = ('black'), 
                        background_color = ('lime'),
                        background_radius = 10)

# Configure the regular and mousover icons for each button 
button_cfg ={
    '-PLAY_BUTTON-':('bx-play', 'bx-play'),
    '-STOP_BUTTON-':('bx-stop','bx-stop'),
    '-EXIT_BUTTON-':('bxs-eject','bxs-eject')   
    }

# Create the button images
button_icons = {}
for button_name, icon_names in button_cfg.items():
    button_icons[button_name] = (create_button_icon.asBytes(icon_names[0]), create_button_mouseover_icon.asBytes(icon_names[1]))


# Define the window's layout
layout = [[sg.Button('No icon',                                   key='-NO_ICON-',     tooltip='A regular button'),
           sg.Button(image_data=button_icons['-PLAY_BUTTON-'][0], key='-PLAY_BUTTON-', tooltip='Play'),
           sg.Button(image_data=button_icons['-STOP_BUTTON-'][0], key='-STOP_BUTTON-', tooltip='Stop'),
           sg.Button(image_data=button_icons['-EXIT_BUTTON-'][0], key='-EXIT_BUTTON-', tooltip='Eject')]]

# Create the window and application icon
window = sg.Window('Simple iconipy Buttons', layout, icon = create_app_icon.asBytes('sticker'), finalize = True)

# Bind tkinter events to our buttons
for button_key in button_cfg.keys():
    window[button_key].bind('<Enter>', 'mouse_enter')
    window[button_key].bind('<Leave>', 'mouse_leave')

while True:                             
    event, values = window.read()     
    
    if '_BUTTON-' in event and 'mouse' in event:
        button_key = event[:-11]    
        if 'mouse_leave' in event: # Set normal icon
            window[button_key].update(image_data=button_icons[button_key][0])
            window[button_key].TooltipObject.leave()
        elif 'mouse_enter' in event: # Set mouseover icon
            window[button_key].update(image_data=button_icons[button_key][1])
            window[button_key].TooltipObject.enter(Coordinates()) # Since we "hijacked" the <Enter>-event we need to activate the tooltip 
        else: # Mouse click
            pass # or do something e.g, play "click" sound  
   
    # Add your event checking code here    
    
    if event in (sg.WIN_CLOSED, '-EXIT_BUTTON-'):
        break

window.close() 
