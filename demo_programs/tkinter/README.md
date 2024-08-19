Hello world example for tkinter:
    import tkinter as tk
    from iconipy import IconFactory

    # Initialize IconFactory with a custom icon size of 20
    create_icon = IconFactory(icon_size=20)

    # Create the main application window
    window = tk.Tk()

    # Generate an icon of a globe
    world_icon = create_icon.asTkPhotoImage('globe')

    # Create a button with text and an icon, then add it to the window
    button = tk.Button(window, text='Hello World!', image=world_icon, compound=tk.LEFT)
    button.grid(padx=10, pady=10)

    # Run the application's event loop
    window.mainloop()
