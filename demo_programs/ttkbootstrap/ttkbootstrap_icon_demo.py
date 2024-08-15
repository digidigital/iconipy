#!/usr/bin/env python3

from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.icons import Icon
from ttkbootstrap.dialogs import MessageDialog, Messagebox
from iconipy import IconFactory
from random import choice

def random_PhotoImage_icon(icon_factory):
    return icon_factory.asTkPhotoImage(choice(icon_factory.icon_names))

def update_label():
    '''Updates the image label with a new random icon'''
    new_image = random_PhotoImage_icon(create_icon)
    random_icon_label.config(image=new_image)
    random_icon_label.image = new_image 

def random_icon_message_box():
    '''Spawns a Messagebox with random icon'''
    # Here we use '.asBytes' to create the icon since the MessageDialog expects bytes instead of PhotoImages!
    md = MessageDialog('You dared to press the forbidden button, and now behold: another random icon emerges from the digital abyss, mocking your curiosity!', 
                       icon=create_message_dialog_icon.asBytes(choice(create_message_dialog_icon.icon_names)))
    md.show()

def display_message(event):
    '''Display  message if the image label is clicked'''
    # Create a toast message with custom icon
    Messagebox.show_info('You "accidentally" tapped on an everyday image instead of a button. Move along, nothing to behold!', title ='Label clicked info')


### Create your IconFactories ###

# Icons for the buttons will be created by this factory
create_danger_icon = IconFactory(icon_set = 'material_icons_regular', 
                        icon_size = 25,  
                        font_color = 'red')

# Will be used to create the random icons after the refresh-button is clicked
create_icon = IconFactory(icon_set = 'lucide', 
                        icon_size = (142,40), 
                        font_size = 30, 
                        font_color = (0, 0, 0, 255), # black solid
                        outline_color = 'dimgrey', 
                        outline_width = 2,
                        background_color = 'silver', 
                        background_radius = 12)

# Will be used to create the random icons after the forbidden button is clicked
create_message_dialog_icon = IconFactory(icon_set = 'material_icons_regular', 
                        icon_size = 64, 
                        font_size = 30, 
                        font_color = (0, 0, 0, 255), # black solid
                        outline_color = '#ff0000', # red
                        outline_width = 8, 
                        background_color = 'white',
                        background_radius = 32)

# ...to demonstrate the use of BitmapIcon
create_monochrome_icon = IconFactory(icon_set = 'lineicons', 
                        icon_size = 48,   
                        font_color = 'black',
                        background_color ='white')

# Initialze root / tkinter
root = tb.Window(themename="morph")


### Use IconFactories to create your icons ### 

# Create a random icon with the 'create_icon' factory
icon_image = random_PhotoImage_icon(create_icon)

# Create an icon for the app
app_icon = create_icon.asTkPhotoImage('sticker')

# Create icons for the buttons
button1_icon = create_danger_icon.asTkPhotoImage('refresh')
button2_icon = create_danger_icon.asTkPhotoImage('warning_amber')

# Create the python logo as BitmapImage
mono_image = create_monochrome_icon.asTkBitmapImage('lni-python')


### Build your GUI ###

root.title("TTK! Bootstrap! Icons!")
root.iconphoto(1, app_icon)
root.geometry('300x260')

# Label for the random icon
random_icon_label = tb.Label(image=icon_image)
random_icon_label.pack(pady=10)

# Bind the function to the label
random_icon_label.bind("<Button-1>", display_message)

button1 = tb.Button(root, width=15)
button1.config(image=button1_icon, compound="center", command=update_label) # Set the image on the left of the text
button1.pack(pady=10)

button2 = tb.Button(root, text="Don't click me!")
button2.config(image=button2_icon, compound="left", command=random_icon_message_box)  # Set the image on the left of the text
button2.pack(pady=10)

monochrome_icon_label = tb.Label(image=mono_image)
monochrome_icon_label.pack(pady=10)

root.mainloop()