import pygame

class Jimmy(pygame.sprite.Sprite): 
  def __init__(self, x, y):
    super().__init__()
    original_image = pygame.image.load("Jimmy.png").convert_alpha()
    scaled_image = pygame.transform.scale(original_image, (original_image.get_width()*2.5, original_image.get_height()*2.5))
    self.image = scaled_image
    self.rect = self.image.get_rect() # Turn into rect
    self.rect.x = x
    self.rect.y = y
    self.speed = 5

  def move(self, keys):
    if keys[pygame.K_LEFT]:
      self.rect.x -= self.speed
      self.rect.x -= 5
    if keys[pygame.K_RIGHT]:
      self.rect.x += self.speed
      self.rect.x += 5
    if keys[pygame.K_UP or pygame.K_SPACE]:
      self.rect.y -= self.speed
      self.rect.y += 5

class Building(pygame.sprite.Sprite):
  def __init__(self, x, y, width, height):
    super().__init__()
    building = pygame.image.load("BuildingM1.png")
    scaled_image = pygame.transform.scale(building, (building.get_width()*2.5, building.get_height()*2.5))
    self.image = scaled_image
    self.x = x
    self.y = y
    self.width = width
    self.height = height