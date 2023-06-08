import pygame
import sys

# Initialize pygame
pygame.init()

#Buildings?
Building1Import = pygame.image.load("Buildings.png")
Building1 = pygame.transform.scale(Building1Import, (730, 1500))

#Jimmy import
Jimmy1Import = pygame.image.load("Jimmy.png")
Jimmy1 = pygame.transform.scale(Jimmy1Import, (300, 150))




# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Nosedive Main Menu")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up fonts
title_font = pygame.font.Font(None, 80)
button_font = pygame.font.Font(None, 40)

# Set up buttons
button_width = 200
button_height = 50
button_x = (screen_width - button_width) // 2
button_spacing = 20
button_y_start = (screen_height - (button_height + button_spacing) * 3) // 2

buttons = [
    pygame.Rect(button_x, button_y_start, button_width, button_height),
    pygame.Rect(button_x, button_y_start + button_height + button_spacing, button_width, button_height),
    pygame.Rect(button_x, button_y_start + (button_height + button_spacing) * 2, button_width, button_height)
]

button_texts = [
    "Start Game",
    "Options",
    "Quit"
]


# Main game loop
running = True
while running:

  
    # Fill the background
    screen.fill(RED)
    #Insert Image
    screen.blit(Building1, (2, 50))

  
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_pos = pygame.mouse.get_pos()
                for i, button in enumerate(buttons):
                    if button.collidepoint(mouse_pos):
                        # Button action based on index
                        if i == 0:
                            print("Start game")
                        elif i == 1:
                            print("Options")
                        elif i == 2:
                            running = False  # Quit the game

  
  
  # Draw the title
    title_text = title_font.render("Nosedive", True, WHITE)
    title_x = (screen_width - title_text.get_width()) // 2
    title_y = 100
    screen.blit(title_text, (title_x, title_y))

    # Draw the buttons
    for i, button in enumerate(buttons):
        pygame.draw.rect(screen, WHITE, button)
        button_text = button_font.render(button_texts[i], True, BLACK)
        button_text_x = button.x + (button.width - button_text.get_width()) // 2
        button_text_y = button.y + (button.height - button_text.get_height()) // 2
        screen.blit(button_text, (button_text_x, button_text_y))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
sys.exit()
