import pygame
from config import *

class Tile(pygame.sprite.Sprite):

  def __init__(self, pos, size):
    super().__init__()
    self.image = pygame.Surface((size, size))
    self.image.fill((147,142,35))
    self.image = pygame.transform.scale(self.image, (32, 32)) 
    self.rect = self.image.get_rect(topleft=pos) 

class Map(pygame.sprite.Sprite):

  def __init__(self, pos, size):
    super().__init__()
    self.image=pygame.Surface((size,size))
   # self.image.fill("grey")
    self.image = pygame.image.load("f_g_i/g_map1.png").convert_alpha()
    self.image = pygame.transform.scale(self.image, (2240,2240)) 
    self.rect = self.image.get_rect(topleft=pos)