#!/usr/bin/env python3

import wx
from iconipy import IconFactory

app = wx.App()
frame = wx.Frame(None, -1, 'wxPython Hello World! Button')
frame.SetDimensions(0, 0, 200, 70)
panel = wx.Panel(frame, wx.ID_ANY)

# Initialize IconFactory for a simple icon with transparent background
create_icon = IconFactory(icon_set = 'lucide', 
                icon_size = 18, 
                font_color = 'grey') # (reg, green, blue. alpha)

# Create the icon as temp file an load it 
# Yo can replace 'globe' with any valid icon name for the icon set
bmp = wx.Bitmap(create_icon.asTempFile('globe'), wx.BITMAP_TYPE_ANY)

# Create a BitmapButton with the loaded image
button = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=bmp, size=(64, 32))

frame.Show()
app.MainLoop()