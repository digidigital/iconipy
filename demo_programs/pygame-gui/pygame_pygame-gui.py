#!/usr/bin/env python3
import pygame
import pygame_gui
from random import choice
from iconipy import IconFactory

# Create IconFactory for generating icons / images
my_icon_factory = IconFactory(
    icon_set='lucide',
    icon_size=(64, 64),
    font_size=30,
    font_color=(255, 0, 0, 255),  # red
    outline_color='dimgrey',
    outline_width=5,
    background_color='silver',
    background_radius=12
)

# Create IconFactory for generating icons for use with buttons
button_icon_factory = IconFactory(
    icon_set='lucide',
    icon_size=(24, 24),
    font_size=16,
    outline_color='red',
    outline_width=3,
    background_color='white',
    background_radius=14
)

# Initialize Pygame
pygame.init()

# Set up the screen and UI manager
screen = pygame.display.set_mode((300, 250))
pygame.display.set_caption("Image Display")
manager = pygame_gui.UIManager((300, 250))

# Function to create a random image
def random_image():
    random_icon_name = choice(my_icon_factory.icon_names)
    new_image = my_icon_factory.asBytesIo(random_icon_name)
    return pygame.image.load(new_image)

# Load the initial image
current_image = random_image()

# Load the button icon
button_icon = pygame.image.load(button_icon_factory.asBytesIo('refresh-cw'))

# Create widgets
refresh_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((100, 150), (100, 40)),
    text='',
    manager=manager
)

# Function to render icon on button
def render_icon_on_button(button_surface, icon_surface):
    icon_rect = icon_surface.get_rect(center=button_surface.get_rect().center)
    button_surface.blit(icon_surface, icon_rect)

# Main loop
clock = pygame.time.Clock()
running = True

while running:
    time_delta = clock.tick(30) / 1000.0  # Convert milliseconds to seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:  # Updated per deprecation warning
            if event.ui_element == refresh_button:
                current_image = random_image()

        manager.process_events(event)

    # Refresh and update display
    screen.fill((200, 150, 200))
    if current_image:
        screen.blit(current_image, (118, 50))  # Draw the current image centered in the display area
    manager.update(time_delta)
    manager.draw_ui(screen)

    # Draw the icon onto the button
    render_icon_on_button(refresh_button.image, button_icon)

    pygame.display.flip()

pygame.quit()
