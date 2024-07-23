#!/usr/bin/env python3

##################################################
# Copyright (c) 2024 Björn Seipel, digidigital   #
# This program is released under the MIT license.#
# Details can be found in the LICENSE file or at:#
# https://opensource.org/licenses/MIT            #
##################################################

from nicegui import ui
import random
from iconipy import IconFactory

# Define default attributes that are valid for all icons at a central place
default_icon_size = 32
default_font_size = 19
default_image_size = 64  

default_image_name = 'circle-user-round'    

# Initialize icon factories with desired settings
# Colors can be names or tuples (Red, Green, Blue, Alpha)
create_button_icon = IconFactory(
                        icon_set = 'lucide', 
                        icon_size = default_icon_size, 
                        font_size = default_font_size,  
                        font_color = (255, 255, 255, 255) # white solid
)

create_image = IconFactory(
                        icon_set = 'lucide', 
                        icon_size = default_image_size, 
                        font_size = 38,  
                        font_color = (0, 0, 0, 255), # black solid
                        outline_color = 'dimgrey', 
                        outline_width = 6,
                        background_color = 'silver', 
                        background_radius = 10
)

# ui.image works with PIL images :D
icon_image = create_image.asPil(default_image_name)
button_image = create_button_icon.asPil('refresh-cw')

# Callback that gets triggered when refresh button is clicked
def image_refresh(): 
    # Create a new image with random codepoint
    random_icon_name = random.choice(create_image.icon_names)
    new_texture_data = create_image.asPil(random_icon_name)
    
    # Replace image in texture registry
    image_element.set_source(new_texture_data)
    
    # Update text with icon codepoint name
    image_name_label.set_text(random_icon_name)

# UI definition
with ui.row():
    image_element = ui.image(icon_image).classes('w-16')
    image_name_label = ui.label(default_image_name)
with ui.button(on_click=lambda: image_refresh()).classes('w-16'):
        ui.image(button_image).classes('w-8 h-8')
         
ui.run()
