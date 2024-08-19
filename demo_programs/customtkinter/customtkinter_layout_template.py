#!/usr/bin/env python3

import tkinter as tk
import customtkinter as ctk
from iconipy import IconFactory

class NavFrame(ctk.CTkFrame):
    def __init__(self, 
                master, 
                icon_set = 'lucide', 
                default_icon_size = 21,         
                font_color_light  = 'dimgrey',
                font_color_dark   = 'lightgrey',
                hover_color_dark  = 'dimgrey',
                hover_color_light = 'lightgrey',
                button_with_text  = True, # False will show icons only 
                hover_effect      = True, # False disables mouseover hover effect
                fly_out           = False, # True activates the flyout effect 
                nav_buttons=[],
                **kwargs):
        super().__init__(master, **kwargs)

        self.configure(corner_radius=0)

        high_res_factor   = 4 # Used to create larger images for scaling
        
        # initialize icon factory with desired settings
        create_light_icon = IconFactory(icon_set = icon_set, 
                                icon_size = default_icon_size * high_res_factor,    
                                font_color = font_color_light
                                )
        
        create_dark_icon = IconFactory(icon_set = icon_set, 
                                icon_size = default_icon_size * high_res_factor,  
                                font_color = font_color_dark
                                )

        # append icon images to nav_buttons 
        for button in nav_buttons:
            button.append(ctk.CTkImage(
                            light_image = create_light_icon.asPil(button[0]),
                            dark_image  = create_dark_icon.asPil(button[0]),
                            size        = (default_icon_size, default_icon_size)
                            )
                        )
            
        # add buttons to the nav bar
        hover_color = None if not hover_color_light or not hover_color_dark else (hover_color_light, hover_color_dark)

        self.all_buttons=[]
        
        for row in range(len(nav_buttons)):
            button_cfg = nav_buttons[row]
            
            button_text = button_cfg[1] if button_with_text else None

            nav_button = ctk.CTkButton(self, 
                                       command=button_cfg[2],
                                       width=default_icon_size, # width is adjusted to fit text automatically 
                                       text=button_text, 
                                       text_color=(font_color_light,font_color_dark),
                                       image=button_cfg[3], 
                                       fg_color='transparent', 
                                       compound='left', 
                                       hover=hover_effect,
                                       hover_color = hover_color,
                                       corner_radius = 0,
                                       border_spacing=5,
                                       anchor='w')

            self.all_buttons.append((nav_button, button_text))

            nav_button.grid(row=row, column=0, padx=0, pady=0, sticky='ew')  # Add button to grid-layout

        if fly_out:
            for button in self.all_buttons:
                button[0].bind("<Enter>", self.show_text)
                button[0].bind("<Leave>", self.hide_text)
                button[0].configure(text='')        
            self.bind("<Enter>", self.show_text)
            self.bind("<Leave>", self.hide_text)    
    
    def show_text(self, event):
        for button in self.all_buttons:
            button[0].configure(text=button[1])

    def hide_text(self, event):
        # the coordinate check is needed to prevent a strange flickering effect 
        # because the leave event seems to be misfired in a certain area.
        if any((event.x < 0, event.y < 0, 
                event.x >= self.winfo_width(),
                event.y >= self.winfo_height())):
            
            for button in self.all_buttons:
                button[0].configure(text='')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x300")
        self.title ('iconipy/CTk Navbar Demo')

        # grid system config
        self.grid_rowconfigure(0, weight=1)  
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        
        #### configuration of your nav-buttons and commands ####
        # [<icon name>, <button text>, <command when clicked>]
        # 'icon_name' must be a valid name for the icon set -> see iconipy docs for more info
        # set the second value to '' or None if you don't need text in the buttons 
        # in this template each button triggers the same function "button_event"
        nav_button_cfg=[['file-plus-2', 'New file', self.button_event],
                        ['file-up', 'Open file', self.button_event],
                        ['save', 'Save file', self.button_event],
                        ['save-all', 'Save all files', self.button_event],
                        ['circle-user-round', 'Accounts', self.button_event],
                        ['settings', 'Settings', self.button_event],
                        ['info', 'About', self.button_event],
        ]
        
        # the navigation 
        self.navigation = NavFrame(master=self, nav_buttons=nav_button_cfg, button_with_text=True, hover_effect=True, fly_out=False)
        self.navigation.grid(row=0, column=0, padx=1, pady=0, sticky="nws")        

        # a frame where you can put your layout
        # note that the size of this frame changes 
        # dynamically when you activate the flyout effect! 
        self.app_layout = ctk.CTkFrame(master=self, corner_radius=0)
        self.app_layout.grid(row=0, column=1, padx=0, pady=0, sticky="nwse")

        ##### your layout here ####
        
        # Grid system config
        self.app_layout.grid_rowconfigure(0, weight=1)  
        self.app_layout.grid_columnconfigure(0, weight=1)

        self.label = ctk.CTkLabel(master=self.app_layout, text="Your layout here", fg_color="transparent")
        self.label.grid(row=0, column=0, sticky="nwse")
    
    def button_event(self):
        print(f'Button pressed! Do something here')

app = App()
app.mainloop()