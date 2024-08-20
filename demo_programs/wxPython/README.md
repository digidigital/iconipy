iconipy 'Hello world' example for wxPython:

```python
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

# Create the icon as temp file and load it 
# You can replace 'globe' with any valid icon name for the icon set
bmp = wx.Bitmap(create_icon.asTempFile('globe'), wx.BITMAP_TYPE_ANY)

# Create a BitmapButton with the loaded image
button = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=bmp, size=(64, 32))

frame.Show()
app.MainLoop()
```

If you prefer PIL Image Objects over temp files:

```python
import wx
from random import choice
from iconipy import IconFactory

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)
        
        # Create a panel
        panel = wx.Panel(self)

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
        simple_button1 = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=simple_bitmap1, pos=(35, 10))
        simple_button2 = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=simple_bitmap2, pos=(110, 10))
        
        button1 = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=bitmap1, pos=(35, 65))
        button2 = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=bitmap2, pos=(110, 65))
       
        # Bind the close event to button2
        button2.Bind(wx.EVT_BUTTON, self.on_close)
        
        # Set the frame size
        self.SetSize(250, 205) 
        self.SetTitle('wxPython Bitmap Buttons')
        self.Centre()

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
        
    def on_close(self, event):
        self.Close(True)

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None)
        frame.Show(True)
        return True

if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
```
