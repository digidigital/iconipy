iconipy code example for guizero:

```python
from guizero import App, PushButton, Text
from iconipy import IconFactory

# Define a function for the button action
def button_action():
    label_below.value = "Hello World!"  # Update the label's text below the button

# Create the main application window
app = App(title="Hello World!", width=200, height=80)

# Initialize IconFactory (with a custom icon size of 20)
create_icon = IconFactory(icon_size=20)

# Generate an icon of a globe
globe_icon = create_icon.asTkPhotoImage('globe')

# Add a label above the button
label_above = Text(app, text="Push the button!", size=14)

# Add a button with text and the generated icon
button = PushButton(
    app,
    image=globe_icon,  # Add the generated icon
    command=button_action
)
button.text_size = 14
button.bg = "white"

# Add a label below the button to display the text
label_below = Text(app, text="", size=14)  # Initially empty

# Display the application window
app.display()
```
