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
    
Then you create your icons by just passing a name to a function call. Iconipy uses a codepoints dictionary to 'translate' names into characters/icons: 

    icon_home = create_button_icon.asPil('house')
    icon_reload = create_button_icon.asPil('refresh-cw')
    icon_files = create_button_icon.asPil('files')
    icon_exit_app = create_button_icon.asPil('log-out')

Depending on your GUI toolkit's whims, you can create PIL Image Objects, ByteIO Objects, Byte-Strings, Raw Pixel Lists, TkPhotoImage Objects, QImage Objects, save to file, and more.

You need to preview an icon? Here we go:

    create_button_icon.show('house')

The icon sets you can choose from include: lucide, boxicons, ligature_symbols, lineicons, material_icons_regular, material_icons_round_regular, material_icons_sharp_regular, material_icons_outlined_regular, microns and typicons.

Feeling adventurous? Dump all the icons to your hard drive and explore:

    create_button_icon.saveAll(<path to target directory>)

You need a hand? Check what the icon set has to offer:

    print(create_button_icon.search('hand'))

Just want a list with all icon names? No problem:

    print(create_button_icon.icon_names)
    
Are you curious if the new version has new icon sets to choose from? 
    
    print(create_button_icon.icon_sets_available)
        
**More info**
    
Visit https://github.com/digidigital/iconipy or https://iconipy.digidigital.de for sample code for the most popular GUI toolkits and detailed documentation.

**Iconify vs. iconipy**

Iconify is totally unrelated to the iconipy project. Iconify is more mature and powerful, but the focus is on SVG files rather than bitmaps. You can explore it further on their website: https://iconify.design

**PyInstaller issues**

As of 0.4.0, iconipy has a pyinstaller hook that fixes a previous issue where the assets folder was not added to the frozen application. You no longer need to specify a hidden import or customize the spec file.

# iconipy API 0.4.0"""

import os
import io
import re
import sys
import json
import uuid
from PIL import Image, ImageTk, ImageQt, ImageDraw, ImageFont, ImageOps
from tempfile import TemporaryDirectory
from typing import Union, Tuple

_ColorAttributeType = Union[Tuple, str]
_SizeAttributeType = Union[Tuple, int]

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_ASSET_PATH = os.path.join(_SCRIPT_DIR, "assets")
_SCRIPT_VERSION = "0.4.0"

_lucide_cfg = {
    "FONT_FILE": os.path.join(_ASSET_PATH, "lucide", "lucide.ttf"),
    "METADATA_FILE": os.path.join(_ASSET_PATH, "lucide", "info.json"),
    "VERSION_FILE": os.path.join(_ASSET_PATH, "lucide", "version.txt"),
    "LICENSE_FILE": os.path.join(_ASSET_PATH, "lucide", "LICENSE.txt"),
}

_ligature_symbols_cfg = {
    "FONT_FILE": os.path.join(_ASSET_PATH, "ligature_symbols", "LigatureSymbols-2.11.ttf"),
    "METADATA_FILE": os.path.join(_ASSET_PATH, "ligature_symbols", "index.html"),
    "VERSION_FILE": os.path.join(_ASSET_PATH, "ligature_symbols", "version.txt"),
    "LICENSE_FILE": os.path.join(_ASSET_PATH, "ligature_symbols", "LICENSE.txt"),
}

_microns_cfg = {
    "FONT_FILE": os.path.join(_ASSET_PATH, "microns", "microns.ttf"),
    "METADATA_FILE": os.path.join(_ASSET_PATH, "microns", "microns.css"),
    "VERSION_FILE": os.path.join(_ASSET_PATH, "microns", "version.txt"),
    "LICENSE_FILE": os.path.join(_ASSET_PATH, "microns", "LICENCE.md"),
}

_typicons_cfg = {
    "FONT_FILE": os.path.join(_ASSET_PATH, "typicons", "typicons.ttf"),
    "METADATA_FILE": os.path.join(_ASSET_PATH, "typicons", "typicons.css"),
    "VERSION_FILE": os.path.join(_ASSET_PATH, "typicons", "version.txt"),
    "LICENSE_FILE": os.path.join(_ASSET_PATH, "typicons", "LICENCE.md"),
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
    "ligature_symbols": _ligature_symbols_cfg,
    "microns": _microns_cfg,
    "typicons": _typicons_cfg,
    "boxicons": _boxicons_cfg,
    "lineicons": _lineicons_cfg,
    "material_icons_regular": _material_icons_regular_cfg,
    "material_icons_round_regular": _material_icons_round_regular_cfg,
    "material_icons_sharp_regular": _material_icons_sharp_regular_cfg,
    "material_icons_outlined_regular": _material_icons_outlined_regular_cfg,
}



class IconFactory:
    """Create an IconFactory for one of the icon sets included with iconipy. All icons created by this 
    IconFactory will share the same settings, allowing you to change the style for all icons upon 
    initialization.
    
        icon_set (str): The name of the icon set that will be used to create the icon.
        icon_size (int, tuple): The size of the icons in pixels. Single int value or (int, int)
        font_size (int): The size of the font. Default is icon_size
        font_color (str, tuple): The color of the font. Name, RGBA-Tuple or hex string
        outline_width (int): The width of the outline. 0 does not draw an outline
        outline_color (str, tuple): The color of the outline.  Name or RGBA-Tuple or hex string
        background_color (str, tuple): The background color. Name or RGBA-Tuple or hex string
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

        self.icon_set_name = icon_set
        '''Stores the name of the icon set that is used to create the icons'''
        
        self.icon_set_version = self._get_icon_set_version(
            _ICON_SETS[icon_set]["VERSION_FILE"]
        )
        '''Stores the version string for the icon set'''

        try:
            self._codepoints = IconFactory._all_codepoints[icon_set]
        except KeyError:
            IconFactory._all_codepoints = self._read_codepoints()
            self._codepoints = IconFactory._all_codepoints[icon_set]
               
        self.icon_names = list(self._codepoints.keys())
        '''A list of all icon names for the selected icon set. When the documentation states that *"name" must be a valid key for the codepoints dictionary*, it means the name you enter must be included in this list.'''
        
        self.license = self._get_license_text(
            _ICON_SETS[icon_set]["LICENSE_FILE"]
        )
        '''The icon set's license'''        
        font_size = self._check_font_vs_icon_size(font_size, icon_size)
        
        self.icon_sets_available = list(_ICON_SETS.keys())
        '''A list containing all icon sets that are installed'''
        
        self._drawing_kwargs = {
            "font_path": _ICON_SETS[icon_set]["FONT_FILE"],
            "icon_size": icon_size,
            "font_size": font_size,
            "font_color": font_color,
            "icon_outline_width": outline_width,
            "icon_outline_color": outline_color,
            "icon_background_color": background_color,
            "icon_background_radius": background_radius,
        }

        self._temp_dir = TemporaryDirectory()
    
    def changeIconSet(self, icon_set: str) -> list:
        '''Change to a different icon set and retrieve a list containing the icon names
        of the new set. Available icon sets include: lucide, boxicons, lineicons, material_icons_regular, 
        material_icons_round_regular, material_icons_sharp_regular, and material_icons_outlined_regular.
        
            icon_set (str): The name of the icon set that will be used to create the icons.
        '''
        if not icon_set in _ICON_SETS.keys():
            raise ValueError(f'Unknown icon set "{icon_set}"')
        self.icon_set_name=icon_set        
        self._drawing_kwargs['font_path']=_ICON_SETS[icon_set]["FONT_FILE"]
        self._codepoints = IconFactory._all_codepoints[icon_set]
        self.icon_names = list(self._codepoints.keys())
        self.license = self._get_license_text(
            _ICON_SETS[icon_set]["LICENSE_FILE"]
        )
        self.icon_set_version = self._get_icon_set_version(
            _ICON_SETS[icon_set]["VERSION_FILE"]
        )
        return self.icon_names
    
    def updateCfg (self,
                    icon_size: _SizeAttributeType = None,
                    font_size: int = None,
                    font_color: _ColorAttributeType = None,
                    outline_width: int = None,
                    outline_color: _ColorAttributeType = None,
                    background_color: _ColorAttributeType = None,
                    background_radius: int = None,
                    ) -> dict:
        '''Modify one or more parameters of the IconFactory object and retrieve a dictionary containing 
        the updated configuration. Typically, distinct IconFactories are created for different icon 
        styles, but there may be scenarios where reusing an existing object is desirable.
        
            icon_size (int, tuple): The size of the icons in pixels. Single int value or (int, int)
            font_size (int): The size of the font. Default is icon_size
            font_color (str, tuple): The color of the font. Name, RGBA-Tuple or hex string
            outline_width (int): The width of the outline. 0 does not draw an outline
            outline_color (str, tuple): The color of the outline.  Name or RGBA-Tuple or hex string
            background_color (str, tuple): The background color. Name or RGBA-Tuple or hex string
            background_radius (int): The radius of the background corners.        
        '''            
        if not icon_size == None:
            if isinstance(icon_size, int):
                icon_size = icon_size if icon_size>0 else 1
            elif isinstance(icon_size, tuple): 
                icon_size = (icon_size[0] if icon_size[0]>0 else 1, icon_size[1] if icon_size[1]>0 else 1)
            self._drawing_kwargs['icon_size']=icon_size
        if not font_size ==None:
            self._drawing_kwargs['font_size']=self._check_font_vs_icon_size(font_size, icon_size)
        if not font_color == None:
            self._drawing_kwargs['font_color']=font_color
        if not outline_width == None:
            self._drawing_kwargs['icon_outline_width']=outline_width if outline_width>=0 else 0 
        if not outline_color == None:
            self._drawing_kwargs['icon_outline_color']=outline_color
        if not background_color == None:
            self._drawing_kwargs['icon_background_color']=background_color
        if not background_radius == None:
            self._drawing_kwargs['icon_background_radius']=background_radius if background_radius>=0 else 0                                                                     
        
        return self._drawing_kwargs
        
    def _check_font_vs_icon_size(self, font_size, icon_size):
        if isinstance(icon_size, int):
            smallest_side = icon_size
        elif isinstance(icon_size, tuple) and len(icon_size)==2 and isinstance(icon_size[0], int) and isinstance(icon_size[1], int):
            smallest_side = icon_size[0] if icon_size[0] <= icon_size[1] else icon_size[1]    
        else:
            raise AttributeError('icon_size must be int or tuple (int,int)')     
         
        if isinstance(font_size, int) and font_size <= smallest_side:
            return font_size if font_size >= 0 else 0  
        else:  
            return smallest_side if smallest_side > 0 else 1
                
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

            elif icon_set in ("boxicons", "microns", "typicons"):
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

            elif icon_set == "ligature_symbols":
                # Read the HTML content from a file
                with open(_METADATA_FILE, 'r', encoding='utf-8') as ls_codepoint_file:
                    html_string = ls_codepoint_file.read()

                pattern = re.compile(
                    r'<td class="lsf symbol">(.+?)</td>\s*<td class="ligature">.+?</td>\s*<td class="unicode">\\(.+?)</td>'
                )
                
                # Find matches
                matches = pattern.findall(html_string)
                
                # Populate the dictionary with the matches
                icon_set_codepoints = {match[0]: match[1] for match in matches}              
                
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
        icon_background_radius=0,
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
                outline_radius = icon_background_radius,
            )
        else:
            image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

        if font_size > 0:
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
            (0, 0, (factor * width)-1, (factor * height)-1),
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
                f'Icon with name "{name}" not available. Icon Set: {self.icon_set_name}, Version: {self.icon_set_version}'
            )

        character = chr(int(self._codepoints[name], 16))
        return self._draw_character(character, **self._drawing_kwargs)

    def asTkPhotoImage(self, name: str):
        """Create image as tkinter PhotoImage Object. Make sure you initialize tkinter first. Place your function call after creating the root instance (root = Tk() or equivalent for other GUI frameworks), "name" must be a valid key for the codepoints dictionary"""
        return ImageTk.PhotoImage(self.asPil(name))

    def asTkBitmapImage(self, name: str):
        """Create image as *monochrome* (two-color) tkinter BitmapImage Object. Make sure you initialize tkinter first. Place your function call after creating the root instance (root = Tk() or equivalent for other GUI frameworks),  "name" must be a valid key for the codepoints dictionary"""
        mode_one_img = self.asPil(name).convert("1")
        inverted_img = ImageOps.invert(mode_one_img)
        return ImageTk.BitmapImage(inverted_img)
           
    def asBytes(self, name: str, image_format: str="PNG"):
        """Returns image data as bytestring, "name" must be a valid key for the codepoints dictionary, the image_format parameter should be set to one of the formats supported by Pillow. These formats include common image types like JPEG, PNG, ICO, and GIF"""
        with io.BytesIO() as output:
            self.asPil(name).save(output, format=image_format)
            return output.getvalue()

    def asBytesIo(self, name: str, image_format: str="PNG"):
        """Returns image data as BytesIO object, "name" must be a valid key for the codepoints dictionary, the image_format parameter should be set to one of the formats supported by Pillow. These formats include common image types like JPEG, PNG, ICO, and GIF"""
        output = io.BytesIO()
        self.asPil(name).save(output, format=image_format)
        output.seek(0)
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

    def asQImage(self, name: str):
        """Create image as QImage Object, "name" must be a valid key for the codepoints dictionary"""
        return ImageQt.ImageQt(self.asPil(name))

    def asQPixmap(self, name: str):
        """Create image as QPixmap Object, "name" must be a valid key for the codepoints dictionary"""
        return ImageQt.toqpixmap(self.asPil(name))
    
    def asTempFile(self, name: str, extension: str="png"):
        '''Returns a path to a temporary image file.  If your framework only accepts file paths, you can use this function. The image format is determined by the file extension (Default is "png") and should be set to one of the formats supported by Pillow. Only formats that support transparency (ico, png, gif, webp, jp2, ...) are supported. "name" must be a valid key for the codepoints dictionary.'''
        filepath = os.path.join(self._temp_dir.name, f'{str(uuid.uuid4())}.{extension.lower()}')
        self.save(name, filepath)   
        return filepath
    
    def save(self, name: str, save_as: str):
        """Saves the icon to file "save_as", the image format is determined by the file extension and should be set to one of the formats supported by Pillow. Only formats that support transparency (ico, png, gif, webp, jp2, ...) are supported. "name" must be a valid key for the codepoints dictionary"""
        kwargs={}
        if save_as.lower().endswith('.ico'):
            kwargs['sizes'] = [self._drawing_kwargs['icon_size']]
        self.asPil(name).save(save_as, **kwargs)

    def saveAll(self, save_to_dir: str, extension: str="png"):
        '''Saves all icons in the icon set to path "save_to_dir", the image format is determined by the "extension" and should be set to one of the formats supported by Pillow. Only formats that support transparency (ico, png, gif, webp, jp2, ...) are supported.'''
        for name in self._codepoints.keys():
            self.save(name, os.path.join(save_to_dir, f"{name}.{extension.lower()}"))

    def show(self, name: str):
        """Show the icon in an external viewer using the PIL Image.show() method. "name" must be a valid key for the codepoints dictionary"""
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
        font_color (str, tuple): The color of the font. Name, RGBA-Tuple or hex string
        outline_width (int): The width of the outline. 0 does not draw an outline
        outline_color (str, tuple): The color of the outline.  Name, RGBA-Tuple or hex string
        background_color (str, tuple): The background color. Name, RGBA-Tuple or hex string
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

        self.icon_set_name = icon_set
        '''Stores the name of the icon set'''

        self.icon_set_version = version
        '''Stores the version string for the icon set'''
        
        self._codepoints = codepoints

        self.icon_names = list(self._codepoints.keys())
        '''A list of all icon names for the selected icon set. When the documentation states that *"name" must be a valid key for the codepoints dictionary*, it means the name you enter must be included in this list.'''

        self.license = 'Unknown License'
        '''For custom icon sets the default value is "Unknown License"'''        
        
        font_size = self._check_font_vs_icon_size(font_size, icon_size)

        self._drawing_kwargs = {
            "font_path": font_path,
            "font_size": font_size,
            "font_color": font_color,
            "icon_size": icon_size,
            "icon_background_color": background_color,
            "icon_outline_width": outline_width,
            "icon_background_radius": background_radius,
            "icon_outline_color": outline_color,
        }

    def changeIconSet(self, icon_set: str):
        '''Not implemented for CustomIconFactory'''
        raise NotImplementedError('changeIconSet is not implemented for CustomIconFactory') 
 

if __name__ == "__main__":
    print(f"iconipy {_SCRIPT_VERSION}")
    print("--------------------------------------")
    for set in _ICON_SETS.keys():
        version = IconFactory._get_icon_set_version(None, _ICON_SETS[set]["VERSION_FILE"])
        print(f"{set} {version}")
