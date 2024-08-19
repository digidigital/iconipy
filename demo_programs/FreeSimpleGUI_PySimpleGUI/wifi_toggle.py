#!/usr/bin/env python3

try:
    import FreeSimpleGUI as sg
except:
    import PySimpleGUI as sg


from iconipy import IconFactory

# Define default attributes that are valid for all icons in a central place
icon_kwargs={
    'icon_size': (60, 26),
    'font_size': 18,
    'outline_width':2,
    'outline_color':'dimgrey',
    'background_color': 'silver',
    'background_radius':13
}
 
# Initialize icon factory with desired settings
# Colors can be names, hex value-strings '#ff125a2' or tuples (R, G, B, Alpha)
create_on_icon = IconFactory(icon_set = 'lucide', 
                        font_color = (0, 125, 0, 255), # green solid
                        **icon_kwargs
                        )

create_off_icon = IconFactory(icon_set = 'lucide', 
                           
                        font_color = (255, 0, 0, 255), # red solid
                        **icon_kwargs)

# Function to toggle Bluetooth state
def toggle_bluetooth():
    global bluetooth_on
    bluetooth_on = not bluetooth_on
    if bluetooth_on:
        window['-BLUETOOTH-'].update(image_data=bluetooth_on_img)
    else:
        window['-BLUETOOTH-'].update(image_data=bluetooth_off_img)

# Function to toggle WiFi state
def toggle_wifi():
    global wifi_on
    wifi_on = not wifi_on
    if wifi_on:
        window['-WIFI-'].update(image_data=wifi_on_img)
    else:
        window['-WIFI-'].update(image_data=wifi_off_img)

# Load images
bluetooth_on_img = create_on_icon.asBytes('bluetooth')
bluetooth_off_img = create_off_icon.asBytes('bluetooth-off')
wifi_on_img = create_on_icon.asBytes('wifi')
wifi_off_img = create_off_icon.asBytes('wifi-off')

# Initial states
bluetooth_on = False
wifi_on = False

# Define the window layout
layout = [
    [sg.Button("", key='-BLUETOOTH-', image_data=bluetooth_off_img, button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
    [sg.Button("", key='-WIFI-', image_data=wifi_off_img, button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)]
]

# Create the window
window = sg.Window("Bluetooth and WiFi Toggle", layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == '-BLUETOOTH-':
        toggle_bluetooth()
    elif event == '-WIFI-':
        toggle_wifi()

# Close the window
window.close()