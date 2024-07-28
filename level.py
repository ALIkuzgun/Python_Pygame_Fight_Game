import pygame, random
from config import *
from player import *
from tiles import *

level_width = 900 
level_height = 540 

class Level(pygame.sprite.Sprite):
  def __init__(self, level_data, surface):
      self.display_surface = surface
      self.setup_level(level_data)
      # Variables
      self.world_shift = 0
      self.saldırı = 0
      self.saldırı2 = 0
      self.menu_durum = "0"
      self.player_score = 0
      self.player2_score = 0
      self.sound = 0
      self.players_died = 0
      self.player_gösterme=0
      self.player_r_doldu=0
      self.buton2_text_color = (255,255,255)
      self.buton3_text_color = (255,255,255)
      self.buton4_text_color = (255,255,255)
      self.buton5_text_color = (255,255,255)
      self.buton6_text_color = (255,255,255)
      self.buton7_text_color = (255,255,255)
      self.buton8_text_color = (255,255,255)
      self.buton9_text_color = (255,255,255)
      self.buton10_text_color = (255,255,255)
      # Health ile ilgili değişkenler
      self.health = 350
      self.max_health = 350  
      self.health_bar_width = 350
      self.health_bar_height = 15

      self.health2 = 350
      self.max_health2 = 350  
      self.health_bar_width2 = 350
      self.health_bar_height2 = 15
      # Ulti ile ilgili değişkenler
      self.r = 0
      self.max_r = 150  
      self.r_bar_width = 150
      self.r_bar_height = 10

      self.r2 = 0
      self.max_r2 = 150  
      self.r_bar_width2 = 150
      self.r_bar_height2 = 10
      # butonlar
      self.draw_button_rect2 = pygame.Rect(399, 229, 90, 48) # play
      self.draw_button_rect3 = pygame.Rect(374, 319, 140, 48) # score
      self.draw_button_rect4 = pygame.Rect(384, 408, 120, 49) # sound
      self.draw_button_rect5 = pygame.Rect(399, 429, 90, 48) # menu
      self.draw_button_rect6 = pygame.Rect(438, 310, 50, 48) # on
      self.draw_button_rect7 = pygame.Rect(514, 309, 60, 48) # off
      self.draw_button_rect8 = pygame.Rect(759, 444, 90, 48) # menu
      self.draw_button_rect9 = pygame.Rect(396, 106, 108, 54) # menu
      self.draw_button_rect10 = pygame.Rect(324, 306, 252, 54) # play again
# Draw health bar
  def draw_health_bar(self, surface):
      health_bar_rect = pygame.Rect(30, 18, self.health_bar_width, self.health_bar_height)
      pygame.draw.rect(surface, (255, 0, 0), health_bar_rect)
  def update_health_bar(self):
      self.health_bar_width = int((self.health / self.max_health) * 350)
  def draw_health_bar2(self, surface):
      health_bar_rect2 = pygame.Rect(530, 18, self.health_bar_width2, self.health_bar_height2)
      pygame.draw.rect(surface, (255, 0, 0), health_bar_rect2)
  def update_health_bar2(self):
      self.health_bar_width2 = int((self.health2 / self.max_health2) * 350)
# Draw Ulti 
  def draw_r_bar(self, surface):
      r_bar_rect = pygame.Rect(30, 48, self.r_bar_width, self.r_bar_height)
      pygame.draw.rect(surface, (0, 255, 255), r_bar_rect)
  def update_r_bar(self):
      player = self.player.sprite
      self.r_bar_width = int((player.e_doldu / self.max_r) * 150)
  def draw_r_bar2(self, surface):
      r_bar_rect2 = pygame.Rect(730, 48, self.r_bar_width2, self.r_bar_height2)
      pygame.draw.rect(surface, (0, 255, 255), r_bar_rect2)
  def update_r_bar2(self):
      player2 = self.player2.sprite
      self.r_bar_width2 = int((player2.p_doldu / self.max_r2) * 150)
# Setup level
  def setup_level(self, layout):
    self.tiles = pygame.sprite.Group()
    self.player = pygame.sprite.GroupSingle()
    self.player2 = pygame.sprite.GroupSingle()
    self.map = pygame.sprite.Group()
    self.all_sprites = pygame.sprite.Group()
    self.all_sprites2 = pygame.sprite.Group()
    for row_index, row in enumerate(layout):
        for col_index, cell in enumerate(row):
            x = col_index * tile_size
            y = row_index * tile_size
            if cell == "X":
                tile = Tile((x, y + 8), tile_size)
                self.tiles.add(tile)
                self.all_sprites2.add(tile)
            elif cell == "1":
                map = Map((x, y), tile_size)
                self.map.add(map)
                self.all_sprites.add(map)
            elif cell == "P":
                player_sprite = Player((x, y))
                self.player.add(player_sprite)
                self.all_sprites.add(player_sprite)
            elif cell == "p":
                player2_sprite = Player2((x, y))
                self.player2.add(player2_sprite)
                self.all_sprites.add(player2_sprite)
# menu
  def menu(self):
    font = pygame.font.Font("character/SHPinscher-Regular.otf", 128)
    button_rect1 = pygame.Rect(440, 100, 20, 18) 
    text_surface1 = font.render("MENU", True, (255,255,255))
    text_rect1 = text_surface1.get_rect(center=button_rect1.center)
    self.display_surface.blit(text_surface1,text_rect1)

    font = pygame.font.Font("character/SHPinscher-Regular.otf", 58)

    button_rect2 = pygame.Rect(399, 229, 90, 48) 
    text_surface2 = font.render("PLAY", True, self.buton2_text_color)
    text_rect2 = text_surface2.get_rect(center=(444, 250))
    self.display_surface.blit(text_surface2,text_rect2)

    button_rect3 = pygame.Rect(374, 319, 140, 48) 
    text_surface3 = font.render("SCORES", True, self.buton3_text_color)
    text_rect3 = text_surface3.get_rect(center=(444, 340))
    self.display_surface.blit(text_surface3,text_rect3)

    button_rect4 = pygame.Rect(384, 408, 120, 49) 
    text_surface4 = font.render("SOUND", True, self.buton4_text_color)
    text_rect4 = text_surface4.get_rect(center=(444, 430))
    self.display_surface.blit(text_surface4,text_rect4)
# score
  def score(self):
    font = pygame.font.Font("character/SHPinscher-Regular.otf", 128)
    button_rect1 = pygame.Rect(440, 100, 20, 18) 
    text_surface1 = font.render("SCORES", True, (255, 255, 255))
    text_rect1 = text_surface1.get_rect(center=button_rect1.center)
    self.display_surface.blit(text_surface1,text_rect1)

    font = pygame.font.Font("character/SHPinscher-Regular.otf", 58)

    button_rect5 = pygame.Rect(399, 429, 90, 48) 
    text_surface2 = font.render("MENU", True, self.buton5_text_color)
    text_rect2 = text_surface2.get_rect(center=(444, 470))
    self.display_surface.blit(text_surface2,text_rect2)

    text_surface3 = font.render("PLAYER 1", True, (255, 255, 255))
    text_rect3 = text_surface3.get_rect(center=(244, 250))
    self.display_surface.blit(text_surface3,text_rect3)

    text_surface4 = font.render("PLAYER 2", True, (255, 255, 255))
    text_rect4 = text_surface4.get_rect(center=(644, 250))
    self.display_surface.blit(text_surface4,text_rect4)

    text_surface3 = font.render(f"{self.player_score}", True, (255, 255, 255))
    text_rect3 = text_surface3.get_rect(center=(244, 320))
    self.display_surface.blit(text_surface3,text_rect3)

    text_surface4 = font.render(f"{self.player2_score}", True, (255, 255, 255))
    text_rect4 = text_surface4.get_rect(center=(644, 320))
    self.display_surface.blit(text_surface4,text_rect4)
# sound
  def sound_menu(self):
    font = pygame.font.Font("character/SHPinscher-Regular.otf", 128)
    button_rect1 = pygame.Rect(440, 100, 20, 18) 
    text_surface1 = font.render("SOUND MENU", True, (255, 255, 255))
    text_rect1 = text_surface1.get_rect(center=button_rect1.center)
    self.display_surface.blit(text_surface1,text_rect1)

    font = pygame.font.Font("character/SHPinscher-Regular.otf", 58)

    button_rect8 = pygame.Rect(759, 444, 90, 48) 
    text_surface2 = font.render("MENU", True, self.buton8_text_color)
    text_rect2 = text_surface2.get_rect(center=(804, 470))
    self.display_surface.blit(text_surface2,text_rect2)

    text_surface3 = font.render("SOUND:", True, (255, 255, 255))
    text_rect3 = text_surface3.get_rect(center=(354, 330))
    self.display_surface.blit(text_surface3,text_rect3)

    button_rect6 = pygame.Rect(436, 310, 50, 48) 
    text_surface3 = font.render("ON", True, self.buton6_text_color)
    text_rect3 = text_surface3.get_rect(center=(472, 330))
    self.display_surface.blit(text_surface3,text_rect3)


    text_surface5 = font.render("/", True, (255, 255, 255))
    text_rect5 = text_surface5.get_rect(center=(504, 330))
    self.display_surface.blit(text_surface5,text_rect5)

    button_rect7 = pygame.Rect(514, 309, 60, 48) 
    text_surface4 = font.render("OFF", True, self.buton7_text_color)
    text_rect4 = text_surface4.get_rect(center=(544, 330))
    self.display_surface.blit(text_surface4,text_rect4)
# players ölümü
  def players_died_menu(self):
    font = pygame.font.Font("character/SHPinscher-Regular.otf", 68)

    button_rect9 = pygame.Rect(396, 106, 108, 54) 
    text_surface2 = font.render("MENU", True, self.buton9_text_color)
    text_rect2 = text_surface2.get_rect(center=(level_width//2, 130))
    self.display_surface.blit(text_surface2,text_rect2)

    button_rect10 = pygame.Rect(324, 306, 252, 54) 
    text_surface3 = font.render("PLAY AGAİN", True, self.buton10_text_color)
    text_rect3 = text_surface3.get_rect(center=(level_width//2, 330))
    self.display_surface.blit(text_surface3,text_rect3)
# reset
  def reset(self):
      # Variables
      self.setup_level(level_map)
      self.world_shift = 0
      self.saldırı = 0
      self.saldırı2 = 0
      self.players_died = 0
      self.player_gösterme=0
      self.buton2_text_color = (255,255,255)
      self.buton3_text_color = (255,255,255)
      self.buton4_text_color = (255,255,255)
      self.buton5_text_color = (255,255,255)
      self.buton6_text_color = (255,255,255)
      self.buton7_text_color = (255,255,255)
      self.buton8_text_color = (255,255,255)
      # Health ile ilgili değişkenler
      self.health = 350
      self.max_health = 350  
      self.health_bar_width = 350
      self.health_bar_height = 15

      self.health2 = 350
      self.max_health2 = 350  
      self.health_bar_width2 = 350
      self.health_bar_height2 = 15

      self.r=0
      self.r2=0
# temaslar
  def collision(self):
      player = self.player.sprite
      player.rect.x += player.direction.x * player.speed

      for sprite in self.tiles.sprites():
          if sprite.rect.colliderect(player.rect):
              if player.direction.x > 0:
                  player.rect.right = sprite.rect.left
              elif player.direction.x < 0:
                  player.rect.left = sprite.rect.right

      player2 = self.player2.sprite
      player2.rect.x += player2.direction.x * player2.speed

      for sprite in self.tiles.sprites():
          if sprite.rect.colliderect(player2.rect):
              if player2.direction.x > 0:
                  player2.rect.right = sprite.rect.left
              elif player2.direction.x < 0:
                  player2.rect.left = sprite.rect.right

      player2_group = pygame.sprite.Group(player2)
      hit = pygame.sprite.spritecollide(player, player2_group, False)
      if hit:
          if player.saldırı == 1:
              self.health2 -= 1
              self.r += 0.9
          if player.saldırı2 == 1:
              self.health2 -= 1.5
          if player2.saldırı == 1:
              self.health -= 1
              self.r2 += 0.9
          if player2.saldırı2 == 1:
              self.health -= 1.5
        
      if self.r2>=150:
         self.player2.saldırı2=1

      if self.r>=150:
         pass

   #   if player2.saldırı==1 and self.sound==1: 
  #      player2.vuruş_ses.play()

   #   if player.saldırı==1 and self.sound==1: 
    #    player.vuruş_sesp1.play()

  def collision_y(self):
      player = self.player.sprite
      player.apply_gravity()

      for sprite in self.tiles.sprites():
          if sprite.rect.colliderect(player.rect):
              if player.direction.y > 0:
                  player.is_jumping = False
                  player.rect.bottom = sprite.rect.top
                  player.direction.y = 0
              elif player.direction.y < 0:
                  player.rect.top = sprite.rect.bottom
                  player.direction.y = 0

      player2 = self.player2.sprite
      player2.apply_gravity()

      for sprite in self.tiles.sprites():
          if sprite.rect.colliderect(player2.rect):
              if player2.direction.y > 0:
                  player2.is_jumping = False
                  player2.rect.bottom = sprite.rect.top
                  player2.direction.y = 0
              elif player2.direction.y < 0:
                  player2.rect.top = sprite.rect.bottom
                  player2.direction.y = 0# Fox.1082
# çizdir
  def run(self):
      player = self.player.sprite
      player2 = self.player2.sprite
      self.all_sprites.draw(self.display_surface)
      self.player.draw(self.display_surface)
      self.player.update()
      self.player2.draw(self.display_surface)
      self.player2.update()
      if player.e_doldu>=150:
          player.e_doldu=150
      if player2.p_doldu>=150:
          player2.p_doldu=150
      self.collision()
      self.collision_y()
      self.update_health_bar()
      self.update_health_bar2()
      self.update_r_bar()
      self.update_r_bar2()
      self.draw_health_bar(self.display_surface)
      self.draw_health_bar2(self.display_surface)
      self.draw_r_bar(self.display_surface)
      self.draw_r_bar2(self.display_surface)

  def run2(self):
      self.all_sprites2.draw(self.display_surface)
      self.map.draw(self.display_surface)