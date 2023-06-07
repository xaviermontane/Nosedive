import pygame
#import sys
from sprite import Jimmy, Building
from ButtonClass import Button

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

# ————————————— Main Program Loop —————————————

while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
        jump = True
      #Jimmy.move(character, event.key)

    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse_pos = pygame.mouse.get_pos()

# ————————————— Game logic should go here
    
    all_sprites.update()

# ————————————— Screen-clearing code

    screen.fill(BLACK)
    background = pygame.image.load("BG.jpeg")
    background = pygame.transform.smoothscale(background, (800, 800))
    screen.blit(background, (0, 0))

    # Draw menu
    menu = True
    while menu is True:
      title_text = title_font.render("Nosedive", True, BLACK)
      start_o = font.render("Start", True, BLACK)
      settings_o = font.render("Settings", True, BLACK)
      quit_o = font.render("Quit", True, BLACK)
      title_x = 350
      title_y = 250
      screen.blit(title_text, (title_x, title_y)) # Blit game title
    
      Building(0, 0, 0 ,0)

    all_sprites.draw(screen) # Draw all the sprites
    screen.blit(character.image, character.rect) # Draw the player (Jimmy)

    pygame.display.update()

    # Keyboard inputs
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_UP:
        character = "Stop"
      elif event.key == pygame.K_DOWN:
        character = "Stop"
      elif event.key == pygame.K_LEFT:
        character = "Stop"
      elif event.key == pygame.K_RIGHT:
        character = "Stop"
    
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
        character = "Up"
      elif event.key == pygame.K_DOWN:
        character = "Down"
      elif event.key == pygame.K_LEFT:
        character = "Left"
      elif event.key == pygame.K_RIGHT:
        character = "Right"
      elif event.key == pygame.K_f:
        print("You payed respects...")

    # Mouse inputs
    if event.type == pygame.MOUSEBUTTONDOWN:
      print("Click!!")

    # --- Drawing code should go here

# --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(60) # —— 60 FPS

# Close the window and quit.
pygame.quit()
