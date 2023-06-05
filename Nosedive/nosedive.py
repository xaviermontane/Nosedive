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

# ————————————— Main Program Loop —————————————
while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
        jump = True
      Jimmy.move(character, event.key)

    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse_pos = pygame.mouse.get_pos()
    '''
          for i, buttons in enumerate(buttons):
              if button.collidepoint(mouse_pos):
                #Button action based on Index
                if i == 0:
                  print("Start is working")
                elif i == 1:
                  print("Options work!")
                elif i == 2:
                  done = True #Quits the game
          '''
# ————————————— Game logic should go here
    all_sprites.update()
# ————————————— Screen-clearing code
    screen.fill(BLACK)

    background = pygame.image.load("BG.jpeg")
    background = pygame.transform.smoothscale(background, (800, 800))
    screen.blit(background, (0, 0))

    # Draw buildings and text
    menu = True
    while menu is True:
      start_o = font.render("Start", True, BLACK)
      settings_o = font.render("Settings", True, BLACK)
      quit_o = font.render("Quit", True, BLACK)
      title_text = title_font.render("Nosedive", True, BLACK)
      title_x = 350
      title_y = 250
      screen.blit(title_text, (title_x, title_y)) # Blit the title

    all_sprites.draw(screen) # Draw all the sprites
    screen.blit(character.image, character.rect) # Draw the player

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
    left, middle, right = pygame.mouse.get_pressed()
    for event in pygame.event.get():
      if event.type == quit:
        pygame.quit()
        sys.exit()
      elif left:
        slide_x = slide_x + 0.1
        slide_y = slide_y + 0.1
        
      elif event.type == pygame.mouse.get_pressed():
          mouse_pos = pygame.mouse.get_pos(screen)
          print("Click !!")
          """
          if mouse_pos in self.rect: # Incorrect
            print(True)
            menu = False
            start = False
          """
      elif middle:
        print("Click — M")
        menu = True
        start = True

    # --- Drawing code should go here

    pygame.display.flip()

    while menu is False:
      #intro()
      pygame.draw.line(screen, WHITE, (0, 150), (150, 150), 3)
      pygame.draw.rect(screen, BROWN, [0, 152, 150, 350])
      pygame.draw.line(screen, WHITE, (150, 150), (150, 500), 3)
      pygame.draw.line(screen, WHITE, (700, 150), (550, 150), 3)
      pygame.draw.rect(screen, BROWN, [550, 152, 250, 350])
      pygame.draw.line(screen, WHITE, (550, 150), (550, 500), 3)
      pygame.draw.rect(screen, BROWN, [700, 500, 40, 40])
      pygame.display.flip()

# --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(60) # —— 60 FPS
# Close the window and quit.
pygame.quit()
