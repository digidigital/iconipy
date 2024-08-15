#!/usr/bin/env python3

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

from iconipy import IconFactory
from random import choice

class MyApp(App):  
    def build(self):
        ### Prepare the icon factories ###

        # Attributes that are the same for background_normal and background_pressed icons
        icon_kwargs = {
            'icon_set' : 'lucide',
            'icon_size' : (64,64),
            'font_size' : 32,
            'background_radius' : 12. 
        }

        # Initialize IconFactory for background_normal    
        self.normal_icon = IconFactory(
            font_color = 'black', 
            outline_color = 'grey', # Try 'red', (255, 0, 0, 255) or '#ff0000'
            background_color = 'silver', # Try 'white', (255, 255, 255, 255) or '#FFFFFF',
            outline_width = 6,
            **icon_kwargs
        )

        # Initialize IconFactory for background_pressed
        self.pressed_icon = IconFactory(
            font_color = 'black', 
            outline_color = 'red',
            background_color = 'pink',
            outline_width = 10,
            **icon_kwargs
        )
        
        ### Build the GUI ###

        # Set window title
        self.title = 'Kivy - iconipy - Demo'
        
        # Create a FloatLayout
        layout = FloatLayout()

        # Set the background color of the app
        Window.clearcolor = (0.8, 0.8, 0.8, 1)  # RGB values for light grey
        
        # Load an image from a file (replace 'icon.png' with your actual icon file)
        icon = self.random_icon()
        
        # Create a button
        button = Button(text="", background_normal=icon[0].source, background_down=icon[1].source, size_hint=(None, None), size=(64, 64))
        button.bind(on_release=self.change_image)  # Bind the press event

        # Add the button to the layout
        layout.add_widget(button)

        # Add a label for the icon's name
        self.label = Label(text=icon[2])
        layout.add_widget(self.label)

        # Position the button at the center of the layout
        button.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.label.pos_hint = {"center_x": 0.5, "center_y": 0.7}
        
        return layout

    def random_icon(self):
        # Pick a random name from all available icon names 
        # Note: Icon names are different in each icon set 
        icon_name = choice(self.normal_icon.icon_names)
        
        # Now use the two icon factories we prepared earlier to create the icons as Kivy Images
        normal_icon = Image(source=self.normal_icon.asTempFile(icon_name))
        pressed_icon = Image(source=self.pressed_icon.asTempFile(icon_name))
        
        return (normal_icon, pressed_icon, icon_name)
    
    def change_image(self, instance):
        # Change's the button's background image when released

        # Get new icons
        new_icon = self.random_icon()

        # Update the button
        instance.background_normal = new_icon[0].source
        instance.background_down = new_icon[1].source
        
        # Update the text label as well
        self.label.text = new_icon[2]

if __name__ == "__main__":
    MyApp().run()