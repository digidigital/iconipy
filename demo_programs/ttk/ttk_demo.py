#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
from iconipy import IconFactory

# Define default attributes that are valid for all icons in a central place
default_icon_size = 20

# Initialize icon factory with desired settings
# Colors can be names, hex value-strings '#ff125a2' or tuples (R, G, B, Alpha)
create_on_icon = IconFactory(icon_set = 'lucide', 
                        icon_size = default_icon_size,  
                        font_color = (0, 125, 0, 255) # green solid
                        )

create_off_icon = IconFactory(icon_set = 'lucide', 
                        icon_size = default_icon_size,   
                        font_color = (255, 0, 0, 255) # red solid
                        )

# Function to toggle Bluetooth state
def toggle_bluetooth():
    global bluetooth_on
    bluetooth_on = not bluetooth_on
    if bluetooth_on:
        bluetooth_button.config(text="Bluetooth On", image=bluetooth_on_img)
    else:
        bluetooth_button.config(text="Bluetooth Off", image=bluetooth_off_img)

# Function to toggle WiFi state
def toggle_wifi():
    global wifi_on
    wifi_on = not wifi_on
    if wifi_on:
        wifi_button.config(text="WiFi On", image=wifi_on_img)
    else:
        wifi_button.config(text="WiFi Off", image=wifi_off_img)

# Initialize main window
root = tk.Tk()
root.title("Bluetooth and WiFi Toggle")

# Load images
bluetooth_on_img = create_on_icon.asTkPhotoImage('bluetooth')
bluetooth_off_img = create_off_icon.asTkPhotoImage('bluetooth-off')

wifi_on_img = create_on_icon.asTkPhotoImage('wifi')
wifi_off_img = create_off_icon.asTkPhotoImage('wifi-off')

# Initial states
bluetooth_on = False
wifi_on = False

# Create style for buttons with border
style = ttk.Style()
style.configure("TButton", borderwidth=1, relief="solid", bordercolor="dimgrey")

# Create Bluetooth button
bluetooth_button = ttk.Button(root, text="Bluetooth Off", width=15, image=bluetooth_off_img, compound=tk.LEFT, command=toggle_bluetooth, style='TButton')
bluetooth_button.grid(row=0, column=0, padx=10, pady=10)

# Create WiFi button
wifi_button = ttk.Button(root, text="WiFi Off", width=15, image=wifi_off_img, compound=tk.LEFT, command=toggle_wifi, style='TButton')
wifi_button.grid(row=0, column=1, padx=10, pady=10)

# Run the application
root.mainloop()
