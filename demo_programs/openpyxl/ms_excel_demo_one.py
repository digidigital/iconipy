import random
from iconipy import IconFactory
import openpyxl
from openpyxl.drawing.image import Image
from openpyxl.styles import Alignment

# Generate four icons with specific properties
create_trend_icon = IconFactory(
                        icon_set='lucide', 
                        icon_size=(24,20), 
                        font_size=16,  
                        font_color=(0, 0, 0, 255),  # Solid black
                        outline_color='white', # A white outline is used to create a margin
                        outline_width=2,
                        background_color='silver', 
                        background_radius=5
)

trend_header_icon = create_trend_icon.asTempFile('chart-no-axes-combined')
trend_up_icon = create_trend_icon.asTempFile('arrow-up')
trend_down_icon = create_trend_icon.asTempFile('arrow-down')
trend_neutral_icon = create_trend_icon.asTempFile('arrow-right')

# Create a list of 60 random numbers
random_numbers = [random.randint(1, 100) for _ in range(60)]

# Create an Excel workbook
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "iconipy-table"

# Create table headers
header_image = Image(trend_header_icon)
sheet.add_image(header_image, 'A1')
sheet.cell(row=1, column=2, value="Units sold")

# Center-align both columns
for col in range(1, 3):
    for row in range(1, len(random_numbers) + 2):  # Include header and data rows
        sheet.cell(row=row, column=col).alignment = Alignment(horizontal="center", vertical="center")

# Insert icons and values based on random numbers
for i, number in enumerate(random_numbers, start=2):  # Start at row 2
    # Assign appropriate icon based on the number
    if number > 66:  # Large number -> "up" icon
        icon = trend_up_icon
    elif number < 33:  # Small number -> "down" icon
        icon = trend_down_icon
    else:  # Medium number -> "neutral" icon
        icon = trend_neutral_icon

    # Insert the icon in the first column
    img = Image(icon)
    cell = f"A{i}"
    sheet.add_image(img, cell)
    
    # Adjust column width
    sheet.column_dimensions['A'].width = 3  # Width to fit the icons; adjust if necessary
    
    # Insert the value in the second column
    sheet.cell(row=i, column=2, value=number)

# Save the Excel file
wb.save("iconipy-demo.xlsx")
