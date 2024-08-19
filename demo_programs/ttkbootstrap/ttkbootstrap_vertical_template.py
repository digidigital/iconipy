#!/usr/bin/env python3

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.tooltip import ToolTip
from iconipy import IconFactory

def button_callback():
    print('Do something here')

# Create the main window
root = tk.Tk()
root.geometry("800x600")
root.title("Frames with Navigation and Grid Layout")

# Apply the ttkbootstrap style
style = ttk.Style(theme="cosmo")  # You can choose any theme you like

# Adjust navbar appearance in this place
nav_bootstyle='light' # can be 'info', 'primary', 'secondary', 'success', 'info', 'warning', 'danger', 'light', 'dark
nav_font_color = 'lightgrey' if nav_bootstyle != 'light' else 'dimgrey'

# Create tootips?
create_tooltips=True

# Define default attributes that are valid for all icons in a central place
default_icon_size = 21

# Initialize icon factory with desired settings
create_nav_icon = IconFactory(icon_set = 'lucide', 
                        icon_size = default_icon_size,  
                        font_color = nav_font_color
                        )

#### Configuration of your nav-buttons ###
# [<icon name>, <tooltip text>, <command when clicked>]
# Set the second value to '' or None if you don't need (or like) tooltips
# In the boilerplate each button triggers the same function button_callback

nav_buttons=[['file-plus-2', 'New file', button_callback],
             ['file-up', 'Open file', button_callback],
             ['save', 'Save file', button_callback],
             ['save-all', 'Save all files', button_callback],
             ['circle-user-round', 'Accounts', button_callback],
             ['settings', 'Settings', button_callback],
             ['info', 'About', button_callback],
]

# Add icon image to config
for button in nav_buttons:
    button.append(create_nav_icon.asTkPhotoImage(button[0]))

# Create the frame for the nav bar
frame1 = ttk.Frame(root, bootstyle=nav_bootstyle)
frame1.grid(row=0, column=0, sticky="ns")

# Add buttons to the nav bar (frame1)
for row in range(len(nav_buttons)):
    button_cfg = nav_buttons[row]
    
    nav_button = ttk.Button(frame1, text="", image=button_cfg[3], command=button_cfg[2], bootstyle=nav_bootstyle) # Create button with icon
    
    if button_cfg[1] and create_tooltips: # Add tooltip
        ToolTip(nav_button, text=button_cfg[1], delay=0)
    
    # Add button to grid-layout of frame1, padding of 1 prevents tooltip from getting stuck
    nav_button.grid(row=row, column=0, padx=1, pady=1)  


# Create the second frame
frame2 = ttk.Frame(root, padding="10")
frame2.grid(row=0, column=1, sticky="nsew")


####### Add your GUI-elements in frame2 here #########

# Create a Notebook (tab view) in the second frame
notebook = ttk.Notebook(frame2)
notebook.grid(row=0, column=0, sticky="nsew")

# Create three tabs
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")

# Add input forms to each tab
for tab in (tab1, tab2):
    label = ttk.Label(tab, text="Input:")
    label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    
    entry = ttk.Entry(tab)
    entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Configure the grid to expand properly
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
frame2.columnconfigure(0, weight=1)
frame2.rowconfigure(0, weight=1)

##################################################

# Start the main event loop
root.mainloop()