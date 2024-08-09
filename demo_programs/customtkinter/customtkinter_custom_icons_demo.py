#!/usr/bin/env python3

##################################################
# Copyright (c) 2024 Björn Seipel, digidigital   #
# This program is released under the MIT license.#
# Details can be found in the LICENSE file or at:#
# https://opensource.org/licenses/MIT            #
##################################################

from iconipy import IconFactory
from itertools import count
from random import shuffle

import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Available icon sets: 'lucide', 'boxicons', 'lineicons', 
        # 'material_icons_regular', 'material_icons_round_regular', 
        # 'material_icons_sharp_regular', and 'material_icons_outlined_regular'
        
        # Store settings in variables that we might need later in the code
        default_icon_set = 'lucide'
        default_icon_size = (24, 24) 

        # Attributes that are the same for light mode and dark mode icons
        icon_kwargs = {
            'icon_set' : default_icon_set,
            'icon_size' : default_icon_size,
             # 'font_size' : 14, # Same as icon size (lowest value) if omitted in icon_kwargs
            'outline_width' : 0,
            'background_radius' : 12. 
        }

        # Initialize IconFactory for light mode    
        lightmode_icon = IconFactory(
            font_color = 'white', 
            outline_color = None, # Try 'red', (255, 0, 0, 255) or '#ff0000'
            background_color = None, # Try 'white', (255, 255, 255, 255) or '#FFFFFF',
            **icon_kwargs
        )

        # Initialize IconFactory for dark mode
        darkmode_icon = IconFactory(
            font_color = 'silver', 
            outline_color = None, # If a color is None it will be transparent
            background_color = None,
            **icon_kwargs
        )

        # Get icon names and shuffle them
        icons = lightmode_icon.icon_names
        shuffle(icons)

        # If you want to see all the icon names:
        # print(lightmode_icon.icon_names)

        # Build the GUI
        self.title(f"iconipy - {default_icon_set} icons - CTkButton Demo")
        self.geometry("1000x800")
        self.resizable(False,False)
        self.grid_columnconfigure((0, 1), weight=1)
        
        rows = 20
        buttons_per_row = 4
        
        try:
            for row_counter in count():
                if row_counter == rows:
                    break

                for column_counter in range(buttons_per_row):
                    icon_name = icons.pop(0)
                    # Create a CTkImage that has one image for light mode and one for dark mode
                    button_icon = customtkinter.CTkImage(light_image=lightmode_icon.asPil(icon_name),
                                  dark_image=darkmode_icon.asPil(icon_name),
                                  size=default_icon_size)
                    
                    # Add a button with created icon and the icon name
                    self.button = customtkinter.CTkButton(self, width=240, text=icon_name, image=button_icon)
                    
                    # Put the button on the grid
                    self.button.grid(row=row_counter, column=column_counter, padx=5, pady=5)
        except IndexError:
            # All icons "popped"
            pass

app = App()
app.mainloop()