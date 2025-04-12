#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')  # Specify the version of Gtk
from gi.repository import Gtk, GdkPixbuf
from iconipy import IconFactory
from random import choice, randrange

# Create IconFactory for generating icons 
# (uses random values - looks different each time the app is executed) 
random_width = randrange(40,150)
random_height = randrange(40,150)
random_outline_width = randrange (0,5)

my_icon_factory = IconFactory(icon_set='lucide', icon_size=(random_width, random_height), 
                              font_size=30,
                              font_color=(randrange(0,255), 0, 0, 255), 
                              outline_color='dimgrey',
                              outline_width=random_outline_width, 
                              background_color='silver',
                              background_radius=12)

# Create IconFactory for generating icons for use with buttons
buttonicon_factory = IconFactory(icon_set='lucide', icon_size=28, 
                                font_size=16,
                                outline_color='red',
                                outline_width=3, 
                                background_color='white',
                                background_radius=14)

def random_icon(icon_factory):
    '''Generates a random icon as a GdkPixbuf (uses a BytesIO object)'''
    # Create a Pixbuf from the bytes
    random_icon_as_bytesio = icon_factory.asBytesIo(choice(icon_factory.icon_names))
    pixbuf_loader = GdkPixbuf.PixbufLoader.new()
    pixbuf_loader.write(random_icon_as_bytesio.read())
    pixbuf_loader.close()
    return pixbuf_loader.get_pixbuf()

def get_icon(icon_factory, icon_name):
    '''Generates a icon as a GdkPixbuf (uses a temp file)'''    
    temp_file_path = icon_factory.asTempFile(icon_name)
    return GdkPixbuf.Pixbuf.new_from_file(temp_file_path)

def update_icon(widget, target_widget, icon_factory):
    '''Updates the image label with a new random icon'''
    new_pixbuf = random_icon(icon_factory)
    target_widget.set_from_pixbuf(new_pixbuf)

def on_label_clicked(widget, event):
    '''Handles the label click event'''
    dialog = Gtk.MessageDialog(
        parent=None,
        message_type=Gtk.MessageType.INFO,
        buttons=Gtk.ButtonsType.OK,
        text="You tapped on the icon! Move along, nothing to see!"
    )
    dialog.run()
    dialog.destroy()

# Create the Gtk Window
window = Gtk.Window(title="PyGObject Icon Demo")
window.set_default_size(300, 260)

# Create an Image widget for the random icon
random_icon_pixbuf = random_icon(my_icon_factory)
icon_image_widget = Gtk.Image(pixbuf=random_icon_pixbuf)

# Wrap the Image widget in an EventBox to handle click events
event_box = Gtk.EventBox()
event_box.add(icon_image_widget)
event_box.connect("button-press-event", on_label_clicked)

# Create a Pixbuf for the refresh icon
refresh_icon_pixbuf = get_icon(buttonicon_factory, 'refresh-cw')
refresh_icon_image = Gtk.Image(pixbuf=refresh_icon_pixbuf)

# Create the "Refresh Icon" Button with both the icon and text
update_button = Gtk.Button()
button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)

# Center the contents of the button box
button_box.set_halign(Gtk.Align.CENTER)
button_box.set_valign(Gtk.Align.CENTER)

# Add the refresh icon and label to the button
button_box.pack_start(refresh_icon_image, True, True, 0)
button_label = Gtk.Label(label="Refresh Icon")
button_box.pack_start(button_label, True, True, 0)

update_button.add(button_box)

# Connect the button to the update_icon function
update_button.connect("clicked", lambda w: update_icon(w, icon_image_widget, my_icon_factory))

# Arrange the widgets in a vertical Box
box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
box.pack_start(event_box, True, True, 0)
box.pack_start(update_button, False, False, 0)

window.add(box)

window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
