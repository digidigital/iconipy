#!/usr/bin/env python3

import gradio as gr
import random
from iconipy import IconFactory

# Define default attributes for all icons
default_icon_size = 30
default_image_size = 256  

# Initialize icon factories with desired settings
# Colors can be names or tuples (Red, Green, Blue, Alpha)
create_button_icon = IconFactory(
    icon_set='lucide', 
    icon_size=default_icon_size, 
    font_size=int(default_icon_size * 0.8),
    font_color=(255, 255, 255, 255)  # white solid color
)

create_image = IconFactory(
    icon_set='lucide', 
    icon_size=default_image_size, 
    font_size=int(default_image_size * 0.7),  
    font_color=(0, 0, 0, 255),  # black solid color
    outline_color='dimgrey', 
    outline_width=int(default_image_size * 0.1),
    background_color='silver', 
    background_radius=int(default_image_size * 0.2)
)

# Generate a temporary file for the button icon
load_button_icon = create_button_icon.asTempFile('refresh-cw')

# Function to load a new image
def load_image():
    # Create a new image with a random icon name
    random_icon_name = random.choice(create_image.icon_names)
    return create_image.asPil(random_icon_name)

# Gradio Interface
with gr.Blocks() as demo:
    img = gr.Image(load_image())
    btn1 = gr.Button("Load New Image", icon=load_button_icon)

    # Event handler for the button
    btn1.click(fn=load_image, inputs=[], outputs=img)

# Launch the app and open it in the browser
demo.launch(inbrowser=True)