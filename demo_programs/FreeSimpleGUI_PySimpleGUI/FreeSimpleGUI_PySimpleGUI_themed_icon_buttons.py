#!/usr/bin/env python3
from iconipy import IconFactory

try:
    import FreeSimpleGUI as sg
except:
    import PySimpleGUI as sg # Tested with version 4.60    

# Set a theme first so you can access the themes colors
sg.theme('SystemDefault')
#sg.theme('DarkGrey1')

# Define default attributes that are valid for all icons in one central place
default_icon_size = (60,25)
default_font_size = 20
default_radius = 0

# Initialize IconFactory with desired settings
# Colors can be names, tuples (R, G, B, Alpha) or hex-strings (#ff0000)
# You can use the theme's colors or choose some other color
create_button_icon = IconFactory(icon_set = 'boxicons', 
                        icon_size = default_icon_size, 
                        font_size = default_font_size,  
                        font_color = sg.theme_button_color_text(),  
                        outline_color = 'grey', 
                        outline_width = 1,
                        background_color = sg.theme_button_color_background(), 
                        background_radius = default_radius)

# Initialize a second IconFactory for the application icon
create_app_icon = IconFactory(icon_set = 'lucide', 
                        icon_size = 64, 
                        font_color = ('black'), 
                        background_color = ('lime'),
                        background_radius = 10)

# First create the button images 
play = create_button_icon.asBytes('bx-play')
stop = create_button_icon.asBytes('bx-stop')
eject = create_button_icon.asBytes('bxs-eject')

# Hint: Use create_button_icon.search(<search term>) to search for available icon names that contain the search term
print(f'boxicons icons for "play": {create_button_icon.search("play")}')
print(f'lucide icons for "play": {create_app_icon.search("play")}')

# Hint: All available icon names are stored in create_button_icon.icon_names
# print(create_button_icon.icon_names)
# print(create_app_icon.icon_names)

# Define the window's layout
layout = [[sg.Button('No icon', key='-NO_ICON-',  border_width=0, tooltip='A regular button'),
           sg.Button(image_data=play, key='-PLAY-',  button_color=sg.theme_background_color(), border_width=0, tooltip='Play'),
           sg.Button(image_data=stop, key='-STOP-',  button_color=sg.theme_background_color(), border_width=0, tooltip='Stop'),
           sg.Button(image_data=eject, key='-EXIT-',  button_color=sg.theme_background_color(), border_width=0, tooltip='Eject')]]

# Create the window and application icon
window = sg.Window('Simple iconipy Buttons', layout, icon = create_app_icon.asBytes('sticker'))

while True:                             
    event, values = window.read()       
    
    if event in (sg.WIN_CLOSED, '-EXIT-'):
        break

window.close() 