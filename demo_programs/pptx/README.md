iconipy 'Hello world!' for pptx:

```python
from iconipy import IconFactory
from pptx import Presentation
from pptx.util import Cm

# Initialize IconFactory 
my_icons = IconFactory(
    icon_set='lucide',  # Available icon sets: 'lucide', 'boxicons', 'lineicons', etc.
    icon_size=(100, 100),
    font_size=70,
    font_color=(0, 0, 0, 255),
    outline_color='red',
    outline_width=14,
    background_color='white',
    background_radius=20
)

# Create icons
icons = {
    "globe": my_icons.asBytesIo('globe'),
    "ghost": my_icons.asBytesIo('ghost'),
    "house-plug": my_icons.asBytesIo('house-plug')
}

# Create a new PowerPoint presentation with 16:9 aspect ratio
ppt = Presentation()
ppt.slide_width = Cm(25.4)  # 16:9 width in cm
ppt.slide_height = Cm(14.29)  # 16:9 height in cm

slide_layout = ppt.slide_layouts[5]  # Using a blank layout
slide = ppt.slides.add_slide(slide_layout)

# Add title
title = slide.shapes.title
title.text = "Three Icons"

# Add description below the title
description = slide.shapes.add_textbox(Cm(2), Cm(3.5), Cm(21), Cm(2))
description.text = "This script demonstrates how to generate and place icons\nfrom the 'Lucide' icon set into a PowerPoint slide using Iconipy."

top_position = Cm(6)
left_icon_x = Cm(5)
left_text_x = Cm(6)

# Add icons and corresponding labels
for icon_name, icon_path in icons.items():
    # Add icon image
    img_shape = slide.shapes.add_picture(icon_path, left_icon_x, top_position, width=Cm(1.5))

    # Add text shout notice next to icon
    text_shape = slide.shapes.add_textbox(left_text_x, top_position, Cm(15), Cm(1))
    text_shape.text = f'Icon set "Lucide" - Icon "{icon_name}"'

    # Increase position for next icon
    top_position += Cm(2.25)

# Save the PowerPoint file
ppt.save("icons_presentation.pptx")

print("Presentation created successfully: icons_presentation.pptx")
```