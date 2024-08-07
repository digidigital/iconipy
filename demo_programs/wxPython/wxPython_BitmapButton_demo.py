#!/usr/bin/env python3

##################################################
# Copyright (c) 2024 Björn Seipel, digidigital   #
# This program is released under the MIT license.#
# Details can be found in the LICENSE file or at:#
# https://opensource.org/licenses/MIT            #
##################################################

import wx
from random import choice
from iconipy import IconFactory

class CustomButtonApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title="Custom Image Buttons", size=(120, 140))
        panel = wx.Panel(frame)

       # Initialize IconFactory for a simple icon with transparent background
        create_icon = IconFactory(icon_set = 'lucide', 
                        icon_size = 32, 
                        font_color = 'grey') # (reg, green, blue. alpha)

        # Initialize another IconFactory with a more complex configuration
        create_button_icon = IconFactory(icon_set = 'lucide', 
                        icon_size = 32, 
                        font_size = 24,  
                        font_color = (125,0,0,125), # (reg, green, blue, alpha)
                        background_color = (0,255,255,255), # (reg, green, blue, alpha)
                        background_radius=10,
                        outline_color='dimgrey',
                        outline_width=2)

        # Create icons and convert them to wx.Image    
        simple_icon1 = self.pil_image_to_wx_image(create_icon.asPil(choice(create_icon.icon_names)))
        simple_icon2 = self.pil_image_to_wx_image(create_icon.asPil(choice(create_icon.icon_names)))
        
        icon1 = self.pil_image_to_wx_image(create_button_icon.asPil(choice(create_button_icon.icon_names)))
        icon2 = self.pil_image_to_wx_image(create_button_icon.asPil('door-open'))
        
        # Convert wx.Image to wx.Bitmap
        simple_bitmap1 = wx.Bitmap(simple_icon1)
        simple_bitmap2 = wx.Bitmap(simple_icon2)
        bitmap1 = wx.Bitmap(icon1)
        bitmap2 = wx.Bitmap(icon2)
        
        # Create buttons with bitmap icons
        simple_button1 = wx.BitmapButton(panel, bitmap=simple_bitmap1)
        simple_button2 = wx.BitmapButton(panel, bitmap=simple_bitmap2)
        
        button1 = wx.BitmapButton(panel, bitmap=bitmap1)
        button2 = wx.BitmapButton(panel, bitmap=bitmap2)

        # Arrange buttons in a grid (2 rows, 2 columns)
        sizer = wx.GridSizer(rows=2, cols=2, vgap=10, hgap=10)
        
        for button in (simple_button1, simple_button2, button1, button2):
            sizer.Add(button, 0, wx.EXPAND)

        # Bind the close event to button2
        button2.Bind(wx.EVT_BUTTON, self.OnClose)

        panel.SetSizer(sizer)
        frame.Show()
        return True

    def pil_image_to_wx_image(self, pil_image):
        '''Converts a Pil Image object to wx.Image object'''
        # Ensure the image has an alpha channel
        if pil_image.mode != 'RGBA':
            pil_image = pil_image.convert('RGBA')
        
        # Create a wx.Image object
        wx_image = wx.Image(pil_image.size[0], pil_image.size[1])
        
        # Set the RGB data
        wx_image.SetData(pil_image.convert('RGB').tobytes())
        
        # Set the alpha data
        wx_image.SetAlpha(pil_image.tobytes()[3::4])
        
        return wx_image
        
    def OnClose(self, event):
        # Destroy the application
        self.Destroy()

if __name__ == "__main__":
    app = CustomButtonApp()
    app.MainLoop()
