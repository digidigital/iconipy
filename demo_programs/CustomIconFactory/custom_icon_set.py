#!/usr/bin/env python3

##################################################
# Copyright (c) 2024 Björn Seipel, digidigital   #
# This program is released under the MIT license.#
# Details can be found in the LICENSE file or at:#
# https://opensource.org/licenses/MIT            #
##################################################

import os
from iconipy import CustomIconFactory

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# We need a font file and metadata for the codepoints
path_to_font_file = os.path.join(_SCRIPT_DIR, 'MaterialSymbolsRounded[FILL,GRAD,opsz,wght].ttf')
path_to_metadata_file = os.path.join(_SCRIPT_DIR, 'MaterialSymbolsRounded[FILL,GRAD,opsz,wght].codepoints')

# Create a codepoint dictionary and parse metadata file
custom_icon_set_codepoints = dict()
with open(path_to_metadata_file) as material_icons_codepoint_file:
    for line in material_icons_codepoint_file:
        codepoint_key, codepoint_value = line.strip().split()
        custom_icon_set_codepoints[codepoint_key] = codepoint_value

# Print the result 
print(custom_icon_set_codepoints)   

# Initialize CustomIconFactory
create_image = CustomIconFactory( # Use CustomIconFactory instead of IconFactory!
                        icon_size = 64, 
                        font_size = 42,  
                        font_color = (0, 0, 0, 255), # black solid
                        outline_color = 'dimgrey', 
                        outline_width = 6,
                        background_color = 'silver', 
                        background_radius = 20,
                        font_path = path_to_font_file, # Path to your font 
                        codepoints = custom_icon_set_codepoints # Codepoint dictionary
)

# Test your custom icon set
create_image.show('favorite')

# Dump all icons to harddrive
# create_image.saveAll(os.path.join(_SCRIPT_DIR, 'icons'))