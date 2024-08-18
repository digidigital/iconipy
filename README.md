# iconipy
Say goodbye to the tedious hassle of graphic programs! Now you can create stunning icons directly from your code. With the look and feel defined right in the code, adjustments are a breeze. Plus, the included icon sets can easily be expanded with your own sets based on font files. 🎨✨

🔧 **Installation**

    pip install iconipy

👷 **Usage**

First you initialize an "IconFactory" with an icon set and look-and-feel settings like this:

    from iconipy import IconFactory 
    
    create_button_icon = IconFactory(
                            icon_set = 'lucide', 
                            icon_size = 64, 
                            font_size = 38,  
                            font_color = (0, 0, 0, 255), # black solid
                            outline_color = 'dimgrey', 
                            outline_width = 6,
                            background_color = 'silver', 
                            background_radius = 10
    ) 
    
🖌 Then you create your icons:  

    icon_home = create_button_icon.asPil('house') # used with CustomTkinter, wxPython, and NiceGUI 
    icon_save = create_button_icon.asBytes('save') # used with PySimpleGUI and FreeSimpleGUI
    icon_files = create_button_icon.asTkPhotoImage('files') # used with tkinter, ttk, and ttkbootstrap 
    icon_folder = create_button_icon.asTkBitmapImage('folder') # used with tkinter, ttk, and ttkbootstrap
    icon_reload = create_button_icon.asQPixmap('refresh-cw') # used with PyQt and PySide
    icon_exit_app = create_button_icon.asRawList('log-out') # used with DearPyGUI
    icon_sticker = create_button_icon.asTempFile('sticker') # used with Kivy and all the rest... 😜

Depending on your GUI toolkit's whims, you can create PIL Image Objects, BytesIO Objects, Byte-Strings, Raw Pixel Lists, TkPhotoImage Objects, QImage Objects, save to file, and more.

📽 You need to preview an icon? Here we go:

    create_button_icon.show('house')

The icon sets you can choose from include: lucide, boxicons, lineicons, material_icons_regular, material_icons_round_regular, material_icons_sharp_regular, and material_icons_outlined_regular.

💾 Feeling adventurous? Dump all the icons to your hard drive and explore:

    create_button_icon.saveAll(<path to target directory>)

🕵 You need a hand? Check what the icon set has to offer: 

    print(create_button_icon.search('hand'))

📃 Just want a list with all icon names? No problem: 

    print(create_button_icon.icon_names)
        
💁 **More info** 
    
Check out the [demo programs](https://github.com/digidigital/iconipy/tree/main/demo_programs) and https://iconipy.digidigital.de for sample code for the most popular GUI toolkits and detailed documentation. 🧘
