iconipy ImageButton for appJar:

```python
#!/usr/bin/env python3

from appJar import gui
from iconipy import IconFactory
from random import choice

# Create the GUI (do this before you use .asTkPhotoImage)
app = gui("iconipy appJar App", "330x250")

# Define default attributes that are valid for all icons in one central place
default_icon_size = (150,30)
default_font_size = 18
default_radius = 12

# Initialize icon factory with desired settings
# Colors can be names or tuples (R, G, B, Alpha)

# Icon factories for the mouseover/image button
create_nrml_btn = IconFactory(icon_set = 'lucide', 
                        icon_size = default_icon_size, 
                        font_size = default_font_size,  
                        font_color = (0, 0, 0, 255), # black solid
                        outline_color = 'dimgrey', 
                        outline_width = 2,
                        background_color = 'silver', 
                        background_radius = default_radius)

create_msover_btn = IconFactory(icon_set = 'lucide', 
                        icon_size = default_icon_size, 
                        font_size = default_font_size,  
                        font_color = (0, 0, 0, 255), # black solid
                        outline_color = 'dimgrey', 
                        outline_width = 2,
                        background_color = (230, 230, 230, 255), 
                        background_radius = default_radius)

# Icon factory for the button with text
create_btn_icon = IconFactory(icon_set = 'lucide', 
                        icon_size = 21, 
                        )

# Icon factory for the large image
create_image = IconFactory(icon_set = 'boxicons', 
                        icon_size = 128, 
                        font_size = 80,  
                        font_color = (0, 0, 0, 255), # black solid
                        outline_color = 'red', 
                        outline_width = 14,
                        background_color = 'white', 
                        background_radius = 64)

# Create icons for the buttons as temporary .GIF files
button_icon=create_btn_icon.asTempFile('refresh-cw', extension='gif')
normal_btn_icon=create_nrml_btn.asTempFile('refresh-ccw', extension='gif')
msover_btn_icon=create_msover_btn.asTempFile('refresh-ccw-dot', extension='gif')

# Create icon for the image widget as PhotoImage 
initial_image=create_image.asTkPhotoImage(create_image.icon_names[0])

# Function to change the image in the image widget 
def change_image(button):
    icon_name = choice(create_image.icon_names)
    app.setImageData("mainImage", create_image.asTkPhotoImage(icon_name), fmt='PhotoImage')

# Add the image widget
app.addImageData("mainImage", initial_image, fmt='PhotoImage')

# Add an ImageButton with text
app.addImageButton("changeImageButton", change_image, button_icon, align='left')
app.setButton("changeImageButton", "Change Image")
app.setButtonTooltip("changeImageButton", "Click to change the image")

# Add an Image with mouseover-effect and SubmitFunction
app.addImage("mouseover_image", normal_btn_icon)
app.setImageMouseOver("mouseover_image", msover_btn_icon)
app.setImageSubmitFunction("mouseover_image", change_image)

# Start the GUI
app.go()
```
