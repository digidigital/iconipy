#!/usr/bin/env python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf, PixbufLoader
from iconipy import IconFactory

class IconViewWindow(Gtk.Window):

    def __init__(self, icon_factory):
        # Initialize the parent Gtk.Window class
        super().__init__()
        # Set the default size for the window
        self.set_default_size(200, 200)
        
        # Create a ListStore to store icons and their names
        liststore = Gtk.ListStore(Pixbuf, str)
        # Create an IconView widget to display the icons
        iconview = Gtk.IconView.new()
        iconview.set_model(liststore)
        iconview.set_pixbuf_column(0)  # Specify the column for pixbuf (image)
        iconview.set_text_column(1)   # Specify the column for text (icon name)

        # List of icon names from the lucide icon set
        icons = ["house", "settings", "power"]
        
        # Populate the ListStore with icons and their names
        for icon in icons:
            liststore.append([self.get_pixbuf(icon_factory, icon), icon])

        # Add the IconView to the window
        self.add(iconview)
        
    def get_pixbuf(self, icon_factory, icon_name):
        '''Generates a Pixbuf object for a given icon name using the provided icon factory.'''
        # Create a Pixbuf from the bytes obtained from the icon factory
        icon_as_bytesio = icon_factory.asBytesIo(icon_name)
        pixbuf_loader = PixbufLoader.new()
        pixbuf_loader.write(icon_as_bytesio.read())
        pixbuf_loader.close()
        return pixbuf_loader.get_pixbuf()

# Create an IconFactory instance for generating icons with specific properties
my_icon_factory = IconFactory(
    icon_set='lucide',                # Specify the icon set
    icon_size=(64, 64),               # Set the size of the icons
    font_size=40,                     # Define the font size
    font_color=(0, 0, 0, 255),        # Define the RGBA color of the font (you can use names or hex values as well)
    outline_color='dimgrey',          # Define the color of the outline
    outline_width=3,                  # Set the width of the outline
    background_color='silver',        # Specify the background color
    background_radius=6               # Define the corner radius of the background
)

# Create the window instance and pass the IconFactory
win = IconViewWindow(my_icon_factory)
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()