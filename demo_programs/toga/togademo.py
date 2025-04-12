#!/usr/bin/env python3
import toga
from toga.style import Pack
from toga.style.pack import CENTER
from iconipy import IconFactory
from random import choice, randrange

# Create IconFactory for generating icons 
my_icon_factory = IconFactory(
    icon_set='lucide',
    icon_size=(64, 64),
    font_size=30,
    font_color=(randrange(0, 255), 0, 0, 255),  # Some random red color
    outline_color='dimgrey',
    outline_width=5,
    background_color='silver',
    background_radius=12
)

# Create IconFactory for generating icons for use with buttons
buttonicon_factory = IconFactory(
    icon_set='lucide',
    icon_size=28,
    font_size=16,
    outline_color='red',
    outline_width=3,
    background_color='white',
    background_radius=14
)

class ImageApp(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title="Image Display", size=(200, 200))

        # Create the initial image
        self.image_view = toga.ImageView(
            toga.Image(my_icon_factory.asBytes('globe')),
            style=Pack(width=64, height=64, align_items=CENTER)  # Updated alignment property
        )

        # Button with icon to refresh the image
        button = toga.Button(
            on_press=self.update_image,  # Updated event handler to change the image
            style=Pack(align_items=CENTER, margin=10),  # Updated padding property
            icon=buttonicon_factory.asTempFile('refresh-cw')
        )

        # Layout
        box = toga.Box(style=Pack(direction="column", align_items=CENTER, margin=20))
        box.add(self.image_view)
        box.add(button)

        self.main_window.content = box
        self.main_window.show()

    def update_image(self, widget):
        # Generate a new random icon
        random_icon_name = choice(my_icon_factory.icon_names)
        new_image = toga.Image(my_icon_factory.asBytes(random_icon_name))

        # Update the ImageView with the new image
        self.image_view.image = new_image

def main():
    return ImageApp("Image Display", "org.example.imageapp")

if __name__ == "__main__":
    main().main_loop()
