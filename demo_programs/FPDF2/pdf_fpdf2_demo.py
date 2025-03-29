import random  
from iconipy import IconFactory  
from fpdf import FPDF

# This script generates a PDF containing a table for each icon set.
# Each table displays all available icons from the icon set along with their names.
# Icons are created with random visual parameters to ensure they are visually distinct when viewed.

# Custom class to initialize and manage the PDF creation process
class MyPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=10) 
        self.set_font('Helvetica', size=10)

# Function to generate a random RGB color
def generate_random_color():
    return tuple(random.randint(0, 255) for _ in range(3))

# Function to add icons and their names to the PDF in a table format
def add_table_w_images_to_pdf(pdf, icon_set_name='lucide'):
    random_color = generate_random_color()  # Generate a random color for iconoutline and table borders

    # Create an IconFactory instance with random parameters for icon customization
    display_icon = IconFactory(
        icon_set=icon_set_name,  # Specify the name of the icon set
        icon_size=(random.randint(40, 60), 40),  # Set icon dimensions (random width, fixed height)
        font_size=32,  # Set font size for the text inside the icon
        font_color=(0, 0, 0, 255),  # Use solid black as font color
        outline_color=random_color,  # Use the generated random color for the icon's outline
        outline_width=random.randint(0, 5),  # Randomize the width of the icon's outline
        background_color='silver',  # Set background color for the icon to silver
        background_radius=random.randint(0, 20)  # Randomize background corner radius for variation
    )
    
    pdf.add_page()
    pdf.start_section(f'{icon_set_name}') 
    pdf.write_html(f'<h2>A table displaying all icons from the "{icon_set_name}" set</h2>')

    # Set the border color of the table to a random color
    pdf.set_draw_color(*random_color)

    # Create a table and populate it with icons and their respective names
    with pdf.table(first_row_as_headings=False, col_widths=(5, 25, 5, 25), padding=1) as table:    
        icons_per_row = 2  
        for i in range(0, len(display_icon.icon_names), icons_per_row):
            row = table.row()  # Add a new row to the table
            for icon_name in display_icon.icon_names[i:i+icons_per_row]:    
                icon = display_icon.asPil(icon_name)  # Generate the icon as a PIL image
                row.cell(img=icon)  # Add the icon image to the cell
                row.cell(icon_name)  # Add the icon's name as text to the cell
        
    return pdf  # Return the updated PDF

# Main script to create and populate the PDF
pdf = MyPDF()  
for icon_set_name in IconFactory().icon_sets_available:
    print(f'Adding icon set "{icon_set_name}" to the PDF file')  
    pdf = add_table_w_images_to_pdf(pdf, icon_set_name) 
pdf.output("./all_iconipy_icons.pdf")


