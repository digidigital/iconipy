#!/usr/bin/env python3
try:
    import PySimpleGUI as sg
except:
    import PySimpleGUI as sg
    
from iconipy import IconFactory   

# Initialize IconFactory (default settings except for a custom icon size of 20)
create_icon = IconFactory(icon_size=20)

# Create the icon as Bytes
icon_bytes = create_icon.asBytes('globe')

layout = [
    [sg.Text('Hello World Button Demo')],
    [sg.Button('', image_data=icon_bytes, button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0, key='Exit')]
]

window = sg.Window('Hello world button!', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

