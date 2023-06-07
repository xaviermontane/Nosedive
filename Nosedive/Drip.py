import pygame, sys
from sprite import Jimmy, Building
import ButtonClass

# Define screen resolution
width, height = 700, 500
screen = pygame.display.set_mode((width, height))
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
building_sprites = pygame.sprite.Group()
building = Building(0, 0) # type: ignore
building_sprites.add(building)
running = True # Loop until the user clicks the close button.

# ————————————— Main Program Loop —————————————
while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

      if event.type == pygame.KEYDOWN:
        menu = False
        if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
          character.move("Up")

      if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()

      if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
          direction = "Stop"
        elif event.key == pygame.K_DOWN:
          direction = "Stop"
        elif event.key == pygame.K_LEFT:
          direction = "Stop"
        elif event.key == pygame.K_RIGHT:
          direction = "Stop"
      
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
          direction = "Up"
        elif event.key == pygame.K_DOWN:
          direction = "Down"
        elif event.key == pygame.K_LEFT:
          direction = "Left"
        elif event.key == pygame.K_RIGHT:
          direction = "Right"
        elif event.key == pygame.K_f:
          print("You payed respects...")
        
      if event.type == pygame.MOUSEBUTTONDOWN:
        print("Click!!")

# ————————————— Game logic should go here
    all_sprites.update()
    building_sprites.update()
# ————————————— Screen-clearing code

    screen.fill(BLACK)
    background = pygame.image.load("BG.jpeg")
    background = pygame.transform.smoothscale(background, (800, 800))
    screen.blit(background, (0, 0))

    # Draw menu
    menu = True
    while menu is True:
      title_text = title_font.render("Nosedive", True, WHITE)
      start_o = font.render("Start", True, BLACK)
      settings_o = font.render("Settings", True, BLACK)
      quit_o = font.render("Quit", True, BLACK)
      screen.blit(title_text, (width, 150)) # Blit game title
      pygame.draw.rect(screen, WHITE, (300, 300, 100, 50)) # Start button
      pygame.draw.rect(screen, WHITE, (300, 350, 100, 50)) # Settings button
      pygame.draw.rect(screen, WHITE, (300, 400, 100, 50)) # Quit button
      screen.blit(start_o, (320, 310)) # Blit start text
      screen.blit(settings_o, (310, 360)) # Blit settings text
      screen.blit(quit_o, (320, 410)) # Blit quit text
    pygame.display.update()

    # --- Drawing code should go here
    all_sprites.draw(screen) # Draw all the sprites
    screen.blit(character.image, character.rect) # Draw the player (Jimmy)
    building.draw(screen) # Draw the building
    pygame.display.update()

# --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(60) # —— 60 FPS

# Close the window and quit.
pygame.quit()
