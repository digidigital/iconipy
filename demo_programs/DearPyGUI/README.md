iconipy code example for DearPyGUI:

```python
import random
from iconipy import IconFactory
import dearpygui.dearpygui as dpg

def image_refresh():
    # Create a new image with random codepoint
    random_icon_name = random.choice(create_image.icon_names)
    new_texture_data = create_image.asRawList(random_icon_name,'FLOAT')
    
    # Replace image in texture registry
    dpg.set_value("label_icon", new_texture_data)
    
    # Update text with icon codepoint name
    dpg.set_value("icon_info_text", random_icon_name)

dpg.create_context()

# Define default attributes that are valid for all icons at a central place
default_icon_size = 32
default_font_size = 19
default_image_size = 64    

# Initialize icon factories with desired settings
# Colors can be names or tuples (R, G, B, Alpha)
create_button_icon = IconFactory(
                        icon_set = 'lucide', 
                        icon_size = default_icon_size, 
                        font_size = default_font_size,  
                        font_color = (255, 0, 0, 125),
                        background_color = (255,255,255,0), 
)

create_image = IconFactory(
                        icon_set = 'lucide', 
                        icon_size = default_image_size, 
                        font_size = 38,  
                        font_color = (0, 0, 0, 255), # black solid
                        outline_color = 'dimgrey', 
                        outline_width = 6,
                        background_color = 'silver', 
                        background_radius = 10
)
    
# Create Pixmap for Icon & Label
default_icon_name = 'circle-user-round'        
label_icon = create_image.asRawList(default_icon_name,'FLOAT')
button_icon = create_button_icon.asRawList('refresh-cw','FLOAT')

with dpg.texture_registry(show=False):
    dpg.add_dynamic_texture(width=default_image_size, height=default_image_size, default_value=label_icon, tag="label_icon")
    dpg.add_static_texture(width=default_icon_size, height=default_icon_size, default_value=button_icon, tag="button_icon")

dpg.create_viewport(title='iconiPy Demo', width=320, max_width=320, max_height=150, min_height=150, height=150)

with dpg.window(label="Button-Icon and Image", tag = "My_Window", width=200):
    dpg.add_text(tag="icon_info_text", pos=(80,20), default_value = default_icon_name)
    dpg.add_image('label_icon', pos=(10,20))
    dpg.add_image_button('button_icon', callback=image_refresh, width=default_icon_size, height=default_icon_size, pos=(144,95) ) 

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("My_Window", True)

# below replaces, start_dearpygui()
while dpg.is_dearpygui_running():
    # insert here any code you would like to run in the render loop
    # you can manually stop by using stop_dearpygui()
    dpg.render_dearpygui_frame()

dpg.destroy_context()
```
