#!/usr/bin/env python3

##################################################
# Copyright (c) 2024 Björn Seipel, digidigital   #
# This program is released under the MIT license.#
# Details can be found in the LICENSE file or at:#
# https://opensource.org/licenses/MIT            #
##################################################

import tkinter as tk
from iconipy import IconFactory

# Define default attributes that are valid for all icons in a central place
default_icon_size = 54
default_font_size = 30
default_radius = 0
default_background_color = None # Transparent background

# Initialize icon factory with desired settings
# Colors can be names or tuples (R, G, B, Alpha)
create_icon = IconFactory(icon_set = 'lucide', 
                        icon_size = default_icon_size, 
                        font_size = default_font_size,  
                        font_color = (0, 0, 0, 255), # black solid
                        outline_color = 'dimgrey', 
                        outline_width = 6,
                        background_color = default_background_color, 
                        background_radius = default_radius)

create_mouseover_icon = IconFactory(icon_set = 'lucide', 
                        icon_size = default_icon_size, 
                        font_size = default_font_size,  
                        font_color = (255,0,0,255), # red solid
                        outline_color = 'red', 
                        outline_width = 10,
                        background_color = default_background_color, 
                        background_radius = default_radius)

# Functions triggerd by events 
def toggle_switch():
    global switch_state
    if switch_state == "left":
        switch_button.config(image=icon_toggle_right)
        switch_state = "right"
        # Add code here for when the switch is on the right
    else:
        switch_button.config(image=icon_toggle_left)
        switch_state = "left"
        # Add code here for when the switch is on the left
    switch_position_label.config(text=f"Switch position: {switch_state}")

def door_mouse_over(event):
    if event.type == '7': # 7 is "<Enter>" event
        door_button.config(image=icon_door_mouseover)
    else:
        door_button.config(image=icon_door)

def door_click(event):
    # Code here for when the door is clicked
    exit()

# Create the window
window = tk.Tk()
window.title("iconipy Button Demo")
window.geometry("160x100")  # Set window size

# Create regular icons 
# Hint: The icon names for the icon set 'lucide' are listed here -> https://lucide.dev/icons/
icon_toggle_left = create_icon.asTkPhotoImage('toggle-left')
icon_toggle_right = create_icon.asTkPhotoImage('toggle-right')
icon_door = create_icon.asTkPhotoImage('door-closed')

# Create mouseover icon
icon_door_mouseover = create_mouseover_icon.asTkPhotoImage('door-open')

# Switch state
switch_state = "left"

# Display switch position
switch_position_label = tk.Label(window, text="Switch position: left")
switch_position_label.pack(side="bottom")

# Switch button
switch_button = tk.Button(window, image=icon_toggle_left, command=toggle_switch, bd=0, highlightthickness=0)
switch_button.pack(side="left")

# Door button
door_button = tk.Button(window, image=icon_door, bd=0, highlightthickness=0)
door_button.pack(side="right")  
door_button.bind("<Enter>", door_mouse_over)
door_button.bind("<Leave>", door_mouse_over)
door_button.bind("<Button-1>", door_click)

# Start the event loop
window.mainloop()