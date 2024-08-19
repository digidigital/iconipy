#!/usr/bin/env python3
import tkinter as tk
import customtkinter as ctk
from iconipy import IconFactory

class NavFrame(ctk.CTkFrame):
    '''Creates a vertical nav frame'''
    def __init__(self, 
                master, 
                default_icon_size = 21,         
                font_color_light  = 'dimgrey',
                font_color_dark   = 'lightgrey',
                hover_color_dark  = 'dimgrey',
                hover_color_light = 'lightgrey',
                button_with_text  = True, 
                hover_effect      = True,
                nav_buttons=[],
                toggle_command = None,
                **kwargs):
        super().__init__(master, **kwargs)

        self.configure(corner_radius=0)
            
        hover_color = None if not hover_color_light or not hover_color_dark else (hover_color_light, hover_color_dark)

        self.all_buttons=[]
        # add buttons to the nav bar        
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

            nav_button.grid(row=row, column=0, padx=0, pady=0, sticky='ew')

        for button in self.all_buttons:
            button[0].bind("<Enter>", toggle_command)
            button[0].bind("<Leave>", toggle_command)           

class NavFrames():
    '''Creates two frames that will be used to build the vertical navigation'''
    def __init__(self,   
            masters, 
            icon_set = 'lucide', 
            default_icon_size = 21,         
            font_color_light  = 'dimgrey',
            font_color_dark   = 'lightgrey',
            hover_color_dark  = 'dimgrey',
            hover_color_light = 'lightgrey', 
            hover_effect      = True, 
            nav_buttons=[],
            toggle_command = None,
            **kwargs):

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
        
        nav_kwargs ={
            'default_icon_size':default_icon_size ,         
            'font_color_light':font_color_light,
            'font_color_dark':font_color_dark,
            'hover_color_dark':hover_color_dark,
            'hover_color_light':hover_color_light, 
            'hover_effect':hover_effect,
            'nav_buttons':nav_buttons,
            'toggle_command':toggle_command,
        }

        self.collapsed = NavFrame(
                                  master = masters[0],  
                                  button_with_text=False,  # no text
                                  **nav_kwargs,
                                  **kwargs
                                ) 

        self.expanded = NavFrame(
                                  master = masters[1], 
                                  button_with_text=True,  # no text
                                  **nav_kwargs,
                                  **kwargs
                                )  

        self.expanded.bind("<Leave>", toggle_command) 
        masters[1].bind("<Leave>", toggle_command) 


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Main window
        self.geometry("600x300")
        self.title ('iconipy/CTk Navbar Demo')
        
        # Grid system config
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Main frame that fills the app dimensions
        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.grid(row=0, column=0, sticky="nsew")
 
        # Grid system config
        self.main_frame.grid_rowconfigure(0, weight=0)  
        self.main_frame.grid_columnconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(0, weight=1)  
        self.main_frame.grid_columnconfigure(1, weight=1)

        # Overlay frame for the expanded navigation
        self.overlay_frame = ctk.CTkFrame(self, corner_radius=0, )
        self.overlay_frame.grid(row=0, column=0, sticky="nsw")
        self.overlay_frame.grid_remove() # initially hide the overlay frame

        # Grid system config
        self.overlay_frame.rowconfigure(0, weight=1)

        #### configuration of your nav-buttons and commands ####
        # [<icon name>, <button text>, <command when clicked>]
        # 'icon_name' must be  valid name for the icon set -> see iconipy docs for more info
        # set the second value to '' or None if you don't need text in the buttons 
        # in this demo each button triggers the same function "button_event"
        ########################################################
        nav_button_cfg=[['file-plus-2', 'New file', self.button_event],
                        ['file-up', 'Open file', self.button_event],
                        ['save', 'Save file', self.button_event],
                        ['save-all', 'Save all files', self.button_event],
                        ['circle-user-round', 'Accounts', self.button_event],
                        ['settings', 'Settings', self.button_event],
                        ['info', 'About', self.button_event],
        ]

        self.navigation = NavFrames((self.main_frame, self.overlay_frame), nav_buttons=nav_button_cfg, toggle_command=self.toggle_nav_frames)
        self.navigation.collapsed.grid(row=0, column=0, padx=(0,1), sticky="wns") # child of self.main_frame
        self.navigation.expanded.grid(row=0, column=0, padx=(0,1), sticky="wns") # child of self.overlay_frame
        
        # put your layout in self.app_layout 
        self.app_layout = ctk.CTkFrame(self.main_frame, corner_radius=0)
        self.app_layout.grid(row=0, column=1, sticky='nsew')
        
        # Grid system config

        # app_layout widgets(or create classes derived from CTkFrame)
        self.label = ctk.CTkLabel(master=self.app_layout, text="Your layout here")
        self.label.grid(row=0, column=0, sticky="nwse")

    def toggle_nav_frames(self, event):
        '''Checks if the overlay is visible. If it's not display the overlay. If it is > Check if mouse pointer is outside of the overlay -> Close overlay if it is.'''
        if self.overlay_frame.winfo_ismapped():
            # get mouse pointer coordinates
            x, y = event.x_root, event.y_root
            
            # find the widget under the mouse pointer
            widget = self.winfo_containing(x, y)
            close_widget=True
            
            # check if one of the parents is the overlay frame
            # and don´t close the overlay if it is
            while widget:
                if widget.nametowidget(widget) == self.overlay_frame:
                    close_widget=False
                    break     
                parent_name = widget.winfo_parent()
                widget = widget.nametowidget(parent_name) if parent_name else None
            
            if close_widget:
                self.overlay_frame.grid_remove()          
        else:
            self.overlay_frame.grid()
    
    def button_event(self):
        '''Just a simple "placeholder" for commands that will be triggered by clicking the nav buttons'''
        print(f'Button pressed! Do something here')

app = App()
app.mainloop()