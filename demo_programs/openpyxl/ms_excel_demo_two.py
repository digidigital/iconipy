import random
from iconipy import IconFactory
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from PIL import Image as PILImage
import io

# Function to generate a random RGB color (for demonstration purposes; Excel doesn't support cell borders with RGB)
def generate_random_color():
    return tuple(random.randint(0, 255) for _ in range(3))

# Function to create a worksheet for an icon set
def add_icon_set_to_worksheet(workbook, icon_set_name='lucide'):
    # Create a new sheet for the icon set
    sheet = workbook.create_sheet(title=icon_set_name)
    sheet.append(["Icon", "Name"])  # Add a header row

    # Create an IconFactory instance
    display_icon = IconFactory(
        icon_set=icon_set_name,  # Specify the name of the icon set
        icon_size=(20, 20),  # Set a fixed size for the icons
        font_size=16,  # Set font size for text inside the icon
        font_color=(0, 0, 0, 255),  # Use solid black as font color
        outline_color=generate_random_color(),  # Use a random color for the icon's outline
        outline_width=2,  # Set a fixed width for the icon's outline
        background_color='silver',  # Set background color to silver
        background_radius=4  # Set corner radius for variation
    )

    # Add icons and their names to the worksheet
    for icon_name in display_icon.icon_names:
        icon = display_icon.asBytesIo(icon_name)  # Generate the icon as a PIL image

        # Convert the image to a format compatible with openpyxl
        img = Image(icon)

        # Add a new row for each icon
        row = sheet.max_row + 1
        sheet.row_dimensions[row].height = 15  # Adjust row height for icons
        sheet.add_image(img, f"A{row}")  # Place the icon in column A of the new row
        sheet.cell(row=row, column=2, value=icon_name)  # Add icon name in column B

# Main script to create and populate the Excel workbook
workbook = Workbook()
workbook.remove(workbook.active)  # Remove the default sheet

# Iterate over all available icon sets and add them to the workbook
for icon_set_name in IconFactory().icon_sets_available:
    print(f'Adding icon set "{icon_set_name}" to the Excel workbook')
    add_icon_set_to_worksheet(workbook, icon_set_name)

# Save the workbook
workbook.save("./all_iconipy_icons.xlsx")
