'''
-------------------------------------------------------------------------------
Name:  nosedive.py
Purpose: Nosedive is an arcade-style game in which the player controls the diver, a character that has fallen from great heights and must avoid colliding with other objects.
The game provides an exponential challenge that motivates the player to beat their past scores and discover the different perks and zones available throughout the game 


Author:   Xavier Montane Perez & George Mandolfo


Created:  18/04/2023
------------------------------------------------------------------------------
'''
import pygame
# from pygame.locals import *
import sys
from sprite import Jimmy
from classTest import Button

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)
SKY_BLUE = (37, 150, 190)
BROWN = (166, 56, 23)

slide_x = 1
slide_y = 1

button_change_x =+ 1
button_change_y =+ 1

# —————————————————————————————————————————————————————————————————————————————————————
current_time = pygame.time.get_ticks()
def idle():
  if current_time > 5000 and not event.type == pygame.MOUSEMOTION:
    Button.draw(screen)
    global count
    while count > 5:
      Button(+10, +10)
      count += 1
    while count < 5 and count < 0: # This is just an example
      Button(-10, -10)
      count -= 1

def three_things(slide_x, slide_y):
  rect = pygame.draw.rect(screen, WHITE, [slide_x+ 270, slide_y+ 150, button_change_x + 120, button_change_y + 35])
  print(rect)
  screen.blit(start_o, [slide_x+ 299, slide_y+ 160])
  pygame.draw.rect(screen, WHITE, [slide_x+ 270, slide_y+ 250, button_change_x + 120, button_change_y + 35])
  screen.blit(settings_o, [slide_x+ 281, slide_y+ 260])
  pygame.draw.rect(screen, WHITE, [slide_x+ 270, slide_y+ 350, button_change_x + 120, button_change_y + 35])
  screen.blit(quit_o, [300, 360])
# —————————————————————————————————————————————————————————————————————————————————————
idle()

def intro():
  # Buildings
  pygame.draw.line(screen, WHITE, (0, 150), (150, 150), 3)
  pygame.draw.rect(screen, BROWN, [0, 152, 150, 350])
  pygame.draw.line(screen, WHITE, (150, 150), (150, 500), 3)
  pygame.draw.line(screen, WHITE, (700, 150), (550, 150), 3)
  pygame.draw.rect(screen, BROWN, [550, 152, 250, 350])
  pygame.draw.line(screen, WHITE, (550, 150), (550, 500), 3)
  pygame.draw.rect(screen, BROWN, [700, 500, 40, 40])
  
# —————————————————————————————————————————————————————————————————————————————————————

pygame.init() # Initialize Pygame

# Define screen resolution
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Nosedive")

character = Jimmy(30, 87)
all_sprites = pygame.sprite.Group() # Create a list of all sprites
all_sprites.add(character)
mouse_pos = pygame.mouse.get_pos()

done = False
clock = pygame.time.Clock()
# ————————————— Main Program Loop —————————————
while not done:
  # ————————————— Main event loop —————————————
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
# ————————————— Game logic should go here
  keys = pygame.key.get_pressed()
  character.move(keys)
  all_sprites.update()
# ————————————— Screen-clearing code
  screen.fill(BLACK) # Here, we clear the screen to black. Don't put drawing commands above
  background = pygame.image.load("BG.jpeg")
  background = pygame.transform.smoothscale(background, (800, 800))
  screen.blit(background, (0, 0))
  all_sprites.draw(screen) # Draw all the sprites
  pygame.display.update()
  screen.blit(character.image, character.rect) # Draw the player

  title_font = pygame.font.SysFont("Kanit", 50, True, False)
  game_title = title_font.render("Nosedive", True, WHITE) # Render the title
  screen.blit(game_title, [243, 65])
  
  start = True
  menu = True

  while menu is True:
    pygame.font.init()
    font = pygame.font.SysFont("Kanit", 30, True, False)  #
    start_o = font.render("Start", True, BLACK)
    settings_o = font.render("Settings", True, BLACK)
    quit_o = font.render("Quit", True, BLACK)

    """
    Button(x, y, width, height, active_color, inactive_color, font_size, text)
    """
    
    #var = Button(0, 100, 10, 70, 80, WHITE, 0, "start")
    idle()
    
    """
    if start == True:
      three_things(50, 10) # Prints option boxes
    """

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
          if mouse_pos in self.rect: # Incorrect
            print(True)
            menu = False
            start = False
      elif middle:
        print("Click — M")
        menu = True
        start = True

    # --- Drawing code should go here
    
    # Buildings are drawn
    pygame.draw.line(screen, WHITE, (0, 150), (150, 150), 3)
    pygame.draw.rect(screen, BLACK, [0, 152, 150, 350])
    pygame.draw.line(screen, WHITE, (150, 150), (150, 500), 3)
    pygame.draw.line(screen, WHITE, (700, 150), (550, 150), 3)
    pygame.draw.rect(screen, BLACK, [550, 152, 250, 350])
    pygame.draw.line(screen, WHITE, (550, 150), (550, 500), 3)
    pygame.display.flip()

  while menu is False:
    intro()
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