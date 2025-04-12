#!/usr/bin/env python3

### ATTENTION ### 
# You need to run this script with:
# python -m pgzero ./pygame_pgzero.py
#################

import random
from iconipy import IconFactory
import pygame

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

button_icon_factory = IconFactory(
    icon_set='lucide',
    icon_size=(24, 24),
    font_size=16,
    outline_color='red',
    outline_width=3,
    background_color='white',
    background_radius=14
)

WIDTH = 300
HEIGHT = 250

# Function to create a random image
def random_image():
    random_icon_name = random.choice(my_icon_factory.icon_names)
    new_image = my_icon_factory.asBytesIo(random_icon_name)
    return pygame.image.load(new_image)

# Load the initial image and button icon
current_image = random_image()
button_icon = pygame.image.load(button_icon_factory.asBytesIo('refresh-cw'))

# Create a button surface
button_surface = pygame.Surface((100, 40))
button_surface.fill((255, 255, 255))  # Button background
pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 100, 40), 2)  # Button outline

# Render the icon onto the button surface
icon_rect = button_icon.get_rect(center=button_surface.get_rect().center)
button_surface.blit(button_icon, icon_rect)

def draw():
    screen.fill((200, 150, 200))  # Background color
    if current_image:
        screen.blit(current_image, (118, 50))  # Draw the current image centered

    # Draw button onto the screen
    screen.blit(button_surface, (100, 150))

def on_mouse_down(pos):
    if 100 <= pos[0] <= 200 and 150 <= pos[1] <= 190:  # Button click area
        global current_image
        current_image = random_image()