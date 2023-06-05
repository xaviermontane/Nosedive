import pygame

class Button:
    def __init__(self, x, y, width, height, active_color, inactive_color, font_size, text):
        self.rect = pygame.Rect()
        self.rect.x = self.rect
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.font = pygame.font.SysFont("Kanit", font_size, True, False)
        self.text = text
        self.rendered_text = self.font.render(self.text, True, self.inactive_color)
        
    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos
        if self.rect.collidepoint(mouse_pos):
            color = self.active_color
        else:
            color = self.inactive_color
            pygame.draw.rect(surface, color, self.rect)
            text_rect = self.rendered_text.get_rect(center=self.rect.center)
            surface.blit(self.rendered_text, text_rect)