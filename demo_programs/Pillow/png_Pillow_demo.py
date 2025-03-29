#!/usr/bin/env python3
from iconipy import IconFactory
from PIL import Image, ImageDraw, ImageFont
from concurrent.futures import ThreadPoolExecutor

# Function to render icons and names into a PNG image
def render_table_to_image(icon_set_name):

    print(f"Processing icon set: {icon_set_name}")

    # Create an IconFactory instance - play with parameter values for icon customization
    display_icon = IconFactory(
        icon_set=icon_set_name,
        icon_size=24, 
        font_size=16,
        font_color=(0, 0, 0, 255),
        outline_color='red',
        outline_width=3,
        background_color='white',
        background_radius=12
    )

    if not display_icon.icon_names:
        print(f"No icons found for icon set: {icon_set_name}")
        return

    icons_per_row = 20  # Number of icons per row
    margin = 10  # Margin around the table
    spacing = 10  # Spacing between rows and cells

    # Calculate image dimensions
    rows = (len(display_icon.icon_names) + icons_per_row - 1) // icons_per_row
    cell_width = 120  # Width of each cell
    cell_height = 50  # Height of each cell
    image_width = margin * 2 + icons_per_row * (cell_width + spacing)
    image_height = margin * 2 + rows * (cell_height + spacing)

    # Create a blank white image
    image = Image.new("RGBA", (image_width, image_height), "white")
    draw = ImageDraw.Draw(image)

    # Font for text
    font = ImageFont.load_default()

    # Draw table content
    for i, icon_name in enumerate(display_icon.icon_names):
        row, col = divmod(i, icons_per_row)
        x = margin + col * (cell_width + spacing)
        y = margin + row * (cell_height + spacing)

        # Render the icon
        img = display_icon.asPil(icon_name)  # Generate the icon as a Pil object

        # Create a white background for the icon
        icon_with_background = Image.new("RGBA", img.size, "white")  # Solid white background
        icon_with_background.paste(img, (0, 0), mask=img)  # Paste the icon using its transparency as a mask

        # Paste the icon with the white background onto the table image
        image.paste(icon_with_background, (x, y))

        # Render the name below the icon
        text_bbox = font.getbbox(icon_name)  # Get text bounding box using ImageFont.getbbox()
        text_width = text_bbox[2] - text_bbox[0]  # Calculate text width
        text_x = x + (img.width // 2) - (text_width // 2)
        text_y = y + img.height + 10
        draw.text((text_x, text_y), icon_name, fill="black", font=font)

    # Save the image for this icon set
    output_path = f"./{icon_set_name}_icons.png"  # Save as a PNG image
    image.save(output_path)
    print(f'Icon set "{icon_set_name}" has been saved as a PNG image.')

# Main script to render images for each icon set in parallel
if __name__ == '__main__':
    icon_sets = IconFactory().icon_sets_available
    with ThreadPoolExecutor() as executor:
        executor.map(render_table_to_image, icon_sets)

