iconipy 'Hello world' example for CustomTkinter:

    import customtkinter as ctk
    from iconipy import IconFactory
    
    # Initialize IconFactory (default settings except for a custom icon size of 20 and font color 'white')
    create_icon = IconFactory(icon_size=20, font_color='white')
    
    # Create the main application window
    window = ctk.CTk()
    
    # Generate an icon of a globe
    world_icon = create_icon.asTkPhotoImage('globe')
    
    # Create a button with text and an icon, then add it to the window
    button = ctk.CTkButton(window, text='Hello World!', image=world_icon, compound='left')
    button.grid(row=0, column=0, padx=10, pady=10)
    
    # Run the application's event loop
    window.mainloop()

A bit more complex:

    import customtkinter as ctk
    from iconipy import IconFactory
    
    # Initialize IconFactory with custom settings
    create_icon = IconFactory(icon_set='lucide',       # One of iconipy's supported icon sets 
                              icon_size=28,            # Size in px
                              font_size=16,            # Size in px  
                              font_color=(0, 0, 0, 255), # Black solid in RGBA values
                              outline_color='#ff0000', # Red as hex-string
                              outline_width=3,         # Width in px
                              background_color='white', # Colors can be set as name strings
                              background_radius=14)    # Radius in px
    
    # Create the main application window
    window = ctk.CTk()
    
    # Create icon
    bike_icon = create_icon.asTkPhotoImage('bike')
    
    # Create a button with text and an icon, then add it to the window
    button = ctk.CTkButton(window, text='No Bikes!', image=bike_icon, compound='left')
    button.grid(row=0, column=0, padx=10, pady=10)
    
    # Start the event loop
    window.mainloop()

See the other demo programs for more complex examples like this one:

        # Initialize IconFactory for light mode    
        lightmode_icon = IconFactory(
            font_color = 'white'
        )

        # Initialize IconFactory for dark mode
        darkmode_icon = IconFactory(
            font_color = 'silver'
        )

        # Create a CTkImage that has one image for light mode and one for dark mode
        button_icon = customtkinter.CTkImage(light_image=lightmode_icon.asPil('sticker'),
                      dark_image=darkmode_icon.asPil('sticker'),
                      size=(20,20))
