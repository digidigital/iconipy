#!/usr/bin/env python3

##################################################
# Copyright (c) 2024 Björn Seipel, digidigital   #
# This program is released under the MIT license.#
# Details can be found in the LICENSE file or at:#
# https://opensource.org/licenses/MIT            #
##################################################

"""Say goodbye to the tedious hassle of graphic programs! Now you can create stunning icons directly
from your Python code. With the look and feel defined right in the code, adjustments are a breeze.
Plus, the included icon sets can easily be expanded with your own sets based on font files.

**Installation**

    pip install iconipy

**Usage**

First you initialize an "IconFactory" with an icon set and look-and-feel settings like this:

    from iconipy import IconFactory 
    
    create_button_icon = IconFactory(
                            icon_set = 'lucide', 
                            icon_size = 64, 
                            font_size = 38,  
                            font_color = (0, 0, 0, 255), # black solid
                            outline_color = 'dimgrey', 
                            outline_width = 6,
                            background_color = 'silver', 
                            background_radius = 10
    ) 
    
Then you create your icons: 

    icon_home = create_button_icon.asPil('house')
    icon_reload = create_button_icon.asPil('refresh-cw')
    icon_files = create_button_icon.asPil('files')
    icon_exit_app = create_button_icon.asPil('log-out')

Depending on your GUI toolkit's whims, you can create PIL Image Objects, ByteIO Objects, Byte-Strings, Raw Pixel Lists, TkPhotoImage Objects, QImage Objects, save to file, and more.

You need to preview an icon? Here we go:

    create_button_icon.show('house')

The icon sets you can choose from include: lucide, boxicons, lineicons, material_icons_regular, material_icons_round_regular, material_icons_sharp_regular, and material_icons_outlined_regular.

Feeling adventurous? Dump all the icons to your hard drive and explore:

    create_button_icon.saveAll(<path to target directory>)

You need a hand? Check what the icon set has to offer:

    print(create_button_icon.search('hand'))

Just want a list with all icon names? No problem:

    print(create_button_icon.icon_names)
        
**More info**
    
Visit https://github.com/digidigital/iconipy or https://iconipy.digidigital.de for sample code for the most popular GUI toolkits and detailed documentation.

**API iconipy 0.2.0**"""

import os
import io
import re
import json
from PIL import Image, ImageTk, ImageQt, ImageDraw, ImageFont
from typing import Union, Tuple

_ColorAttributeType = Union[Tuple, str]
_SizeAttributeType = Union[Tuple, int]

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_ASSET_PATH = os.path.join(_SCRIPT_DIR, "assets")
_SCRIPT_VERSION = "0.2.0"

_lucide_cfg = {
    "FONT_FILE": os.path.join(_ASSET_PATH, "lucide", "lucide.ttf"),
    "METADATA_FILE": os.path.join(_ASSET_PATH, "lucide", "info.json"),
    "VERSION_FILE": os.path.join(_ASSET_PATH, "lucide", "version.txt"),
    "LICENSE_FILE": os.path.join(_ASSET_PATH, "lucide", "LICENSE.txt"),
}

_boxicons_cfg = {
    "FONT_FILE": os.path.join(_ASSET_PATH, "boxicons", "boxicons.ttf"),
    "METADATA_FILE": os.path.join(_ASSET_PATH, "boxicons", "boxicons.css"),
    "VERSION_FILE": os.path.join(_ASSET_PATH, "boxicons", "version.txt"),
    "LICENSE_FILE": os.path.join(_ASSET_PATH, "boxicons", "LICENSE.txt"),
}

_lineicons_cfg = {
    "FONT_FILE": os.path.join(_ASSET_PATH, "lineicons", "lineicons.ttf"),
    "METADATA_FILE": os.path.join(_ASSET_PATH, "lineicons", "unicodesMap.json"),
    "VERSION_FILE": os.path.join(_ASSET_PATH, "lineicons", "version.txt"),
    "LICENSE_FILE": os.path.join(_ASSET_PATH, "lineicons", "LICENSE.md"),
}

_material_icons_regular_cfg = {
    "FONT_FILE": os.path.join(
        _ASSET_PATH, 
        "material_icons_regular", 
        "MaterialIcons-Regular.ttf"
    ),
    "METADATA_FILE": os.path.join(
        _ASSET_PATH, 
        "material_icons_regular", 
        "MaterialIcons-Regular.codepoints"
    ),
    "VERSION_FILE": os.path.join(
        _ASSET_PATH, 
        "material_icons_regular", 
        "version.txt"
    ),
    "LICENSE_FILE": os.path.join(
        _ASSET_PATH, 
        "material_icons_regular", 
        "LICENSE.txt"
    ),
}

_material_icons_round_regular_cfg = {
    "FONT_FILE": os.path.join(
        _ASSET_PATH, 
        "material_icons_round_regular", 
        "MaterialIconsRound-Regular.otf"
    ),
    "METADATA_FILE": os.path.join(
        _ASSET_PATH,
        "material_icons_round_regular",
        "MaterialIconsRound-Regular.codepoints"
    ),
    "VERSION_FILE": os.path.join(
        _ASSET_PATH, 
        "material_icons_round_regular", 
        "version.txt"
    ),
    "LICENSE_FILE": os.path.join(
        _ASSET_PATH, 
        "material_icons_round_regular", 
        "LICENSE.txt"
    ),
}

_material_icons_sharp_regular_cfg = {
    "FONT_FILE": os.path.join(
        _ASSET_PATH, 
        "material_icons_sharp_regular", 
        "MaterialIconsSharp-Regular.otf"
    ),
    "METADATA_FILE": os.path.join(
        _ASSET_PATH,
        "material_icons_sharp_regular",
        "MaterialIconsSharp-Regular.codepoints"
    ),
    "VERSION_FILE": os.path.join(
        _ASSET_PATH, 
        "material_icons_sharp_regular", 
        "version.txt"
    ),
    "LICENSE_FILE": os.path.join(
        _ASSET_PATH, 
        "material_icons_sharp_regular", 
        "LICENSE.txt"
    ),
}

_material_icons_outlined_regular_cfg = {
    "FONT_FILE": os.path.join(
        _ASSET_PATH,
        "material_icons_outlined_regular",
        "MaterialIconsOutlined-Regular.otf"
    ),
    "METADATA_FILE": os.path.join(
        _ASSET_PATH,
        "material_icons_outlined_regular",
        "MaterialIconsOutlined-Regular.codepoints"
    ),
    "VERSION_FILE": os.path.join(
        _ASSET_PATH, 
        "material_icons_outlined_regular", 
        "version.txt"
    ),
    "LICENSE_FILE": os.path.join(
        _ASSET_PATH, 
        "material_icons_outlined_regular", 
        "LICENSE.txt"
    ),
}

_ICON_SETS = {
    "lucide": _lucide_cfg,
    "boxicons": _boxicons_cfg,
    "lineicons": _lineicons_cfg,
    "material_icons_regular": _material_icons_regular_cfg,
    "material_icons_round_regular": _material_icons_round_regular_cfg,
    "material_icons_sharp_regular": _material_icons_sharp_regular_cfg,
    "material_icons_outlined_regular": _material_icons_outlined_regular_cfg,
}


class IconFactory:
    """Create an IconFactory for one of the icon sets included with iconiPy. All icons created by this 
    IconFactory will share the same settings, allowing you to change the style for all icons upon 
    initialization. Note that switching between icon sets may cause issues due to differing icon names.
    
        icon_set (str): The name of the icon set that will be used to create the icon.
        icon_size (int, tuple): The size of the icons in pixels. Single int value or (int, int)
        font_size (int): The size of the font. Default is icon_size
        font_color (str, tuple): The color of the font. Name or RGBA-Tuple
        outline_width (int): The width of the outline. 0 does not draw an outline
        outline_color (str, tuple): The color of the outline.  Name or RGBA-Tuple
        background_color (str, tuple): The background color. Name or RGBA-Tuple
        background_radius (int): The radius of the background corners.
    """

    _all_codepoints = {}

    def __init__(
        self,
        icon_set: str = "lucide",
        icon_size: _SizeAttributeType = 64,
        font_size: int = None,
        font_color: _ColorAttributeType = "black",
        outline_width: int = 0,
        outline_color: _ColorAttributeType = "black",
        background_color: _ColorAttributeType = None,
        background_radius: int = 0,
    ) -> None:
        if not icon_set in _ICON_SETS.keys():
            raise ValueError(f'Unknown icon set "{icon_set}"')

        self.icon_set_version = self._get_icon_set_version(
            _ICON_SETS[icon_set]["VERSION_FILE"]
        )
        '''Stores the version string for the icon set'''
        
        self.icon_set = icon_set
        '''Stores the name of the icon set'''
        
        self.license = self._get_license_text(
            _ICON_SETS[icon_set]["LICENSE_FILE"]
        )
        '''The icon set's license'''

        try:
            self._codepoints = IconFactory._all_codepoints[icon_set]
        except KeyError:
            IconFactory._all_codepoints = self._read_codepoints()
            self._codepoints = IconFactory._all_codepoints[icon_set]
        
        self.icon_names = list(self._codepoints.keys())
        '''A list containing all icon names for the selected icon set'''
        
        font_size = self._check_font_vs_icon_size(font_size, icon_size)
        
        self._drawing_kwargs = {
            "font_path": _ICON_SETS[icon_set]["FONT_FILE"],
            "font_size": font_size,
            "font_color": font_color,
            "icon_size": icon_size,
            "icon_background_color": background_color,
            "icon_outline_width": outline_width,
            "icon_outline_radius": background_radius,
            "icon_outline_color": outline_color,
        }

    def _check_font_vs_icon_size(self, font_size, icon_size):
        if isinstance(icon_size, int):
            smallest_side = icon_size
        elif isinstance(icon_size, tuple) and len(icon_size)==2 and isinstance(icon_size[0], int) and isinstance(icon_size[1], int):
            smallest_side = icon_size[0] if icon_size[0] <= icon_size[1] else icon_size[1]    
        else:
            raise AttributeError('icon_size must be int or tuple (int,int)')     
         
        if font_size and font_size <= smallest_side:
            return font_size  
        else:  
            return smallest_side
            
        
    def _read_codepoints(self):
        codepoints = {}
        for icon_set in _ICON_SETS.keys():
            icon_set_codepoints = {}
            _METADATA_FILE = _ICON_SETS[icon_set]["METADATA_FILE"]

            if icon_set == "lucide":
                with open(_METADATA_FILE) as json_data:
                    codepoint_data = json.load(json_data)
                for key in codepoint_data.keys():
                    icon_set_codepoints[key] = codepoint_data[key]["encodedCode"][1:]

            elif icon_set == "boxicons":
                pattern = re.compile(
                    r'.*\.(?P<codepoint_key>([a-z0-9]*-){1,4}[a-z0-9]*):.*\n.*"\\(?P<codepoint_value>.*)";'
                )

                with open(_METADATA_FILE, "r") as boxicons_codepoint_file:
                    raw_content = boxicons_codepoint_file.read()

                    # Find all matches in the file content
                    matches = pattern.finditer(raw_content)

                    # Populate the dictionary with the matches
                    for match in matches:
                        codepoint_key = match.group("codepoint_key")
                        codepoint_value = match.group("codepoint_value")
                        icon_set_codepoints[codepoint_key] = codepoint_value

            elif icon_set == "lineicons":
                with open(_METADATA_FILE) as json_data:
                    codepoint_data = json.load(json_data)
                for key, value in codepoint_data.items():
                    icon_set_codepoints[key] = hex(value)[2:]

            else:
                # Material icons
                with open(_METADATA_FILE) as material_icons_codepoint_file:
                    for line in material_icons_codepoint_file:
                        codepoint_key, codepoint_value = line.strip().split()
                        icon_set_codepoints[codepoint_key] = codepoint_value

            codepoints[icon_set] = icon_set_codepoints

        return codepoints

    def _get_license_text(self, license_file):
        with open(license_file, "r") as file_handle:
            return file_handle.read()

    def _get_icon_set_version(self, version_file):
        with open(version_file, "r") as file_handle:
            return file_handle.readline().rstrip()

    def _draw_character(
        self,
        character,
        font_path,
        font_size=32,
        font_color="grey",
        icon_size=32,
        icon_background_color=None,
        icon_outline_width=0,
        icon_outline_radius=0,
        icon_outline_color="dimgrey",
    ):

        # Create image
        if isinstance (icon_size, int):
            width = height = icon_size
        elif isinstance (icon_size, tuple) and isinstance (icon_size[0], int) and isinstance (icon_size[1], int):
            width = icon_size[0]
            height = icon_size[1]
        else:
            raise AttributeError ('icon_size must be of type int or tuple (int, int)')
        
        # Add a background
        if icon_background_color or icon_outline_width:
            image = self._image_round_background(
                size = (width, height),
                fill = icon_background_color,
                outline = icon_outline_color,
                outline_width = icon_outline_width,
                outline_radius = icon_outline_radius,
            )
        else:
            image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

        # Load font
        font = ImageFont.truetype(font_path, font_size)

        # Draw character
        draw = ImageDraw.Draw(image)

        x = width // 2
        y = height // 2

        draw.text((x, y), character, font=font, anchor="mm", fill=font_color)
        return image

    def _image_round_background(
        self,
        size = (64,64),
        fill = "silver",
        outline = "grey",
        outline_width = 7,
        outline_radius = 10,
        factor = 3,
    ):
        """Create and return a background image with rounded corners. Set the outline radius to size/2 to achieve a circular background."""
        width = size[0] 
        height = size[1]
        im = Image.new("RGBA", (factor * width, factor * height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(im, "RGBA")
        draw.rounded_rectangle(
            (0, 0, factor * width, factor * height),
            radius=factor * outline_radius,
            outline=outline,
            fill=fill,
            width=factor * outline_width,
        )
        im = im.resize((width, height), Image.LANCZOS)
        return im

    def search(self, search_name: str) -> list:
        """Search for an icon name. Returns a list of icon names containing the search_name"""
        return [icon_name for icon_name in self.icon_names if search_name.lower() in icon_name.lower()]

    def asPil(self, name: str):
        """Create image as PIL Image Object, "name" must be a valid key for the codepoints dictionary"""
        if not name in self._codepoints:
            raise ValueError(
                f'Icon with name "{name}" not available. Icon Set: {self.icon_set}, Version: {self.icon_set_version}'
            )

        character = chr(int(self._codepoints[name], 16))
        return self._draw_character(character, **self._drawing_kwargs)

    def asTkPhotoImage(self, name: str):
        """Create image as tkinter PhotoImage Object, "name" must be a valid key for the codepoints dictionary"""
        return ImageTk.PhotoImage(self.asPil(name))

    def asBytes(self, name: str, image_format: str="PNG"):
        """Returns image data as byte-string, "name" must be a valid key for the codepoints dictionary, image_format is one of PIL Image formats"""
        with io.BytesIO() as output:
            self.asPil(name).save(output, format=image_format)
            return output.getvalue()

    def asBytesIo(self, name: str, image_format: str="PNG"):
        """Returns image data as BytesIO object, name" must be a valid key for the codepoints dictionary, image_format is one of PIL Image formats"""
        with io.BytesIO() as output:
            self.asPil(name).save(output, format=image_format)
            return output

    def asRawList(self, name: str, type: str="RGB"):
        """Returns the pixel data of the image as a list. "name" must be a valid key for the codepoints dictionary, type="RGB" contains values 0-255, type="FLOAT" contains values 0-1"""

        def _calc_pixel_value(value, type):
            if type == "FLOAT":
                return value / 255.0
            return value  # 'RGB' or any other type

        icon = self.asPil(name)
        pixel_data = []
        # Process image to list
        # numpy etc. are WAY faster but introduce new dependencies
        for i in range(0, icon.height):
            for j in range(0, icon.width):
                pixel = icon.getpixel((j, i))
                pixel_data.append(_calc_pixel_value(pixel[0], type))
                pixel_data.append(_calc_pixel_value(pixel[1], type))
                pixel_data.append(_calc_pixel_value(pixel[2], type))
                pixel_data.append(_calc_pixel_value(pixel[3], type))
        return pixel_data

    def asQtImage(self, name: str):
        """Create image as QImage Object, "name" must be a valid key for the codepoints dictionary"""
        return ImageQt.ImageQt(self.asPil(name))

    def save(self, name: str, save_as: str):
        """Saves the icon to path "save_as", the format of the image is determined by the file extension, "name" must be a valid key for the codepoints dictionary"""
        self.asPil(name).save(save_as)

    def saveAll(self, save_to_dir: str, extension="png"):
        '''Saves all icons in the icon set to path "save_to_dir", the format of the image is determined by the file extension "extension"'''
        for name in self._codepoints.keys():
            self.save(name, os.path.join(save_to_dir, f"{name}.{extension}"))

    def show(self, name: str):
        """Show the icon in an external viewer using the PIL Image.show() method. Name must be a valid key for the codepoints dictionary"""
        self.asPil(name).show()


class CustomIconFactory(IconFactory):
    """Create an IconFactory for a custom icon set by providing a font path
    (supported by the FreeType library, e.g., TrueType, OpenType) and a
    dictionary of codepoints. The dictionary keys should be the icon names
    ('microphone'), and the values should be the corresponding
    hexadecimal codepoints ('E02A').
    
        icon_set (str): The name of the icon set that will be used to create the icon.
        icon_size (int, tuple): The size of the icons in pixels. Single int value or (int, int)
        font_size (int): The size of the font. Default is icon_size
        font_color (str, tuple): The color of the font. Name or RGBA-Tuple
        outline_width (int): The width of the outline. 0 does not draw an outline
        outline_color (str, tuple): The color of the outline.  Name or RGBA-Tuple
        background_color (str, tuple): The background color. Name or RGBA-Tuple
        background_radius (int): The radius of the background corners.
        font_path (str): The path to the custom icon set font file.
        codepoints (dict): A dictionary of icon names and codepoints.
        version (str): The version of the icon set.
    """

    def __init__(
        self,
        icon_set: str = "custom",
        icon_size: _SizeAttributeType = 64,
        font_size: int = None,
        font_color: _ColorAttributeType = "black",
        outline_width: int = 0,
        outline_color: _ColorAttributeType = "black",
        background_color: _ColorAttributeType = None,
        background_radius: int = 0,
        font_path: str = None,
        codepoints: dict = None,
        version: str = "0.1",
    ) -> None:
        if not font_path or not codepoints:
            raise ValueError(
                f'You need to supply a font path and codepoint dictionary"'
            )

        self.icon_set_version = version
        '''Stores the version string for the icon set'''
        
        self.icon_set = icon_set
        '''Stores the name of the icon set'''
        
        self.license = 'Unknown License'
        '''For custom icon sets the default value is "Unknown License"'''

        self._codepoints = codepoints

        self.icon_names = list(self._codepoints.keys())
        '''A list containing all icon names for the selected icon set'''
        
        font_size = self._check_font_vs_icon_size(font_size, icon_size)

        self._drawing_kwargs = {
            "font_path": font_path,
            "font_size": font_size,
            "font_color": font_color,
            "icon_size": icon_size,
            "icon_background_color": background_color,
            "icon_outline_width": outline_width,
            "icon_outline_radius": background_radius,
            "icon_outline_color": outline_color,
        }

if __name__ == "__main__":
    print(f"iconipy {_SCRIPT_VERSION}")
    print("--------------------------------------")
    for set in _ICON_SETS.keys():
        version = IconFactory._get_icon_set_version(None, _ICON_SETS[set]["VERSION_FILE"])
        print(f"{set} {version}")