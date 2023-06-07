'''
-------------------------------------------------------------------------------
Name:  nosedive.py
Purpose: Nosedive is an arcade-style game in which the player controls the diver, a character that has fallen from great heights and must avoid colliding with other objects.
The game provides an exponential challenge that motivates the player to beat their past scores and discover the different perks and zones available throughout the game 


Author:   Xavier Montane Perez & George Mandolfo


Created:  18/04/2023
------------------------------------------------------------------------------
'''

import pygame, sys
from sprite import Jimmy
from sprite import Building
#from classTest import Button

# Define screen resolution
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Nosedive")

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)
SKY_BLUE = (37, 150, 190)
BROWN = (166, 56, 23)
RED = (225, 0, 0)

# —————————————————————————————————————————————————————————————————————————————————————
pygame.init() # Initialize Pygame
current_time = pygame.time.get_ticks()
clock = pygame.time.Clock()

# Set up fonts
pygame.font.init()
title_font = pygame.font.SysFont("Kanit", 50, True, False)
button_font = pygame.font.SysFont("Kanit", 40, True, False)
font = pygame.font.SysFont("Kanit", 30, True, False)

character = Jimmy(30, 87)
all_sprites = pygame.sprite.Group() # Create a list of all sprites
all_sprites.add(character)
running = True # Loop until the user clicks the close button.
