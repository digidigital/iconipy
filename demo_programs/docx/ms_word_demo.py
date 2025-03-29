#!/usr/bin/env python3

import random
from iconipy import IconFactory
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from concurrent.futures import ThreadPoolExecutor

# Function to add icons and their names to the Word document
def add_table_w_images_to_doc(icon_set_name):
    doc = Document()
    
    # Create an IconFactory instance - play with parameter values for icon customization
    display_icon = IconFactory(
        icon_set=icon_set_name,
        icon_size=20,
        font_size=16,
        font_color=(0, 0, 0, 255),
        outline_color='grey',
        outline_width=3,
        background_color='silver',
        background_radius=4
    )

    # Add a heading for the icon set
    doc.add_heading(f'A table displaying all icons from the "{icon_set_name}" set', level=2)

    icons_per_row = 3  # Number of icons per row

    # Create a table without any initial rows
    table = doc.add_table(rows=0, cols=icons_per_row)  # Three columns per row
    table.style = 'Table Grid'

    # Populate the table with icons and their respective names
    
    for i in range(0, len(display_icon.icon_names), icons_per_row):
        row = table.add_row().cells
        for j, icon_name in enumerate(display_icon.icon_names[i:i+icons_per_row]):
            img_stream = display_icon.asBytesIo(icon_name)  # Generate the icon as a Bytes IO Object

            # Center the image and icon name in the cell
            paragraph = row[j].add_paragraph()
            run = paragraph.add_run()
            run.add_picture(img_stream)
            paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

            # Add the icon's name below the image, also centered
            paragraph = row[j].add_paragraph(icon_name)
            paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            paragraph.style.font.size = Pt(10)

    # Save the document for this icon set
    doc.save(f"./{icon_set_name}_icons.docx")
    print(f'Icon set "{icon_set_name}" has been saved.')

# Main script to create and populate Word documents in parallel
if __name__ == '__main__':
    icon_sets = IconFactory().icon_sets_available
    with ThreadPoolExecutor() as executor:
        executor.map(add_table_w_images_to_doc, icon_sets)
