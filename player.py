import pygame
from config import *

class Player(pygame.sprite.Sprite):
  def __init__(self,pos):
    super().__init__() 
    self.load_images()  
    self.facing2="right"
    self.image = self.standing_frames[0]  
    self.rect = self.image.get_rect(topleft=pos)
    self.current_frame = 0
    self.last_update = pygame.time.get_ticks()
    self.frame_rate = 100
    self.vuruş_sesp1= pygame.mixer.Sound("character/x.mp3")
    
    self.direction=pygame.math.Vector2(0,0)
    self.speed=8
    self.gravity=1
    self.jump_speed=-13
    self.is_jumping = False
    self.facing="stay"
    self.right, self.left=0,0

    self.total_distance = 0
    self.haraket=0

    self.attack_index = 0
    self.attack_counter = 0
    self.is_attacking = False
    self.saldırı = 0
    self.saldırı2 = 0
    self.attack=0
    self.pos = pos
    self.oyun_durdu = 0
    self.e_doldu = 0
    self.e_süre = 0
    self.e_sıfırlama = 0

  def load_images(self):
      self.standing_frames = [pygame.transform.scale(pygame.image.load("character/s1.png").convert_alpha(), (85, 190))]
      self.standing_frames2 = [pygame.transform.scale(pygame.image.load("character/sl1.png").convert_alpha(), (85, 190))]

      self.walk_frames = [
          pygame.transform.scale(pygame.image.load("character/w1.png").convert_alpha(), (145, 190)),
          pygame.transform.scale(pygame.image.load("character/w2.png").convert_alpha(), (140, 190)),
          pygame.transform.scale(pygame.image.load("character/w3.png").convert_alpha(), (150, 190)),
          pygame.transform.scale(pygame.image.load("character/w4.png").convert_alpha(), (170, 190)),
          pygame.transform.scale(pygame.image.load("character/w5.png").convert_alpha(), (125, 190)),
          pygame.transform.scale(pygame.image.load("character/w6.png").convert_alpha(), (140, 190)),
          pygame.transform.scale(pygame.image.load("character/w7.png").convert_alpha(), (150, 190)),
      ]
      self.walk_frames_left = [
          pygame.transform.scale(pygame.image.load("character/wl1.png").convert_alpha(), (145, 190)),
          pygame.transform.scale(pygame.image.load("character/wl2.png").convert_alpha(), (140, 190)),
          pygame.transform.scale(pygame.image.load("character/wl3.png").convert_alpha(), (150, 190)),
          pygame.transform.scale(pygame.image.load("character/wl4.png").convert_alpha(), (170, 190)),
          pygame.transform.scale(pygame.image.load("character/wl5.png").convert_alpha(), (125, 190)),
          pygame.transform.scale(pygame.image.load("character/wl6.png").convert_alpha(), (140, 190)),
          pygame.transform.scale(pygame.image.load("character/wl7.png").convert_alpha(), (150, 190)),
      ]

      self.attack_frames = [
          pygame.transform.scale(pygame.image.load("character/a1.png").convert_alpha(), (180, 190)),
          pygame.transform.scale(pygame.image.load("character/a2.png").convert_alpha(), (240, 190)),
          pygame.transform.scale(pygame.image.load("character/a3.png").convert_alpha(), (165, 190)),
          pygame.transform.scale(pygame.image.load("character/a4.png").convert_alpha(), (185, 190)),
          pygame.transform.scale(pygame.image.load("character/a5.png").convert_alpha(), (305, 190)),
          pygame.transform.scale(pygame.image.load("character/a6.png").convert_alpha(), (270, 190)),
          pygame.transform.scale(pygame.image.load("character/a7.png").convert_alpha(), (205, 190)),
      ]

      self.attack_frames_left = [
          pygame.transform.scale(pygame.image.load("character/al1.png").convert_alpha(), (180, 190)),
          pygame.transform.scale(pygame.image.load("character/al2.png").convert_alpha(), (240, 190)),
          pygame.transform.scale(pygame.image.load("character/al3.png").convert_alpha(), (165, 190)),
          pygame.transform.scale(pygame.image.load("character/al4.png").convert_alpha(), (185, 190)),
          pygame.transform.scale(pygame.image.load("character/al5.png").convert_alpha(), (305, 190)),
          pygame.transform.scale(pygame.image.load("character/al6.png").convert_alpha(), (270, 190)),
          pygame.transform.scale(pygame.image.load("character/al7.png").convert_alpha(), (205, 190)),
      ]

      self.attack_frames2 = [
          pygame.transform.scale(pygame.image.load("character/a21.png").convert_alpha(), (150, 190)),
          pygame.transform.scale(pygame.image.load("character/a22.png").convert_alpha(), (180, 190)),
          pygame.transform.scale(pygame.image.load("character/a23.png").convert_alpha(), (250, 190)),
          pygame.transform.scale(pygame.image.load("character/a24.png").convert_alpha(), (315, 190)),
          pygame.transform.scale(pygame.image.load("character/a25.png").convert_alpha(), (215, 190)),
          pygame.transform.scale(pygame.image.load("character/a26.png").convert_alpha(), (260, 190)),
          pygame.transform.scale(pygame.image.load("character/a27.png").convert_alpha(), (260, 190)),
          pygame.transform.scale(pygame.image.load("character/a28.png").convert_alpha(), (270, 190)),
          pygame.transform.scale(pygame.image.load("character/a29.png").convert_alpha(), (205, 190)),
          pygame.transform.scale(pygame.image.load("character/a210.png").convert_alpha(), (175, 190)),
          pygame.transform.scale(pygame.image.load("character/a211.png").convert_alpha(), (230, 190)),
          pygame.transform.scale(pygame.image.load("character/a212.png").convert_alpha(), (200, 190)),
          pygame.transform.scale(pygame.image.load("character/a213.png").convert_alpha(), (90, 190)),
      ]

      self.attack_frames2_left = [
          pygame.transform.scale(pygame.image.load("character/a2l1.png").convert_alpha(), (150, 190)),
          pygame.transform.scale(pygame.image.load("character/a2l3.png").convert_alpha(), (250, 190)),
          pygame.transform.scale(pygame.image.load("character/a2l4.png").convert_alpha(), (315, 190)),
          pygame.transform.scale(pygame.image.load("character/a2l5.png").convert_alpha(), (215, 190)),
          pygame.transform.scale(pygame.image.load("character/a2l6.png").convert_alpha(), (260, 190)),
          pygame.transform.scale(pygame.image.load("character/a2l7.png").convert_alpha(), (260, 190)),
          pygame.transform.scale(pygame.image.load("character/a2l8.png").convert_alpha(), (270, 190)),
          pygame.transform.scale(pygame.image.load("character/a2l9.png").convert_alpha(), (205, 190)),
          pygame.transform.scale(pygame.image.load("character/a2l10.png").convert_alpha(), (175, 190)),
          pygame.transform.scale(pygame.image.load("character/a2l11.png").convert_alpha(), (230, 190)),
          pygame.transform.scale(pygame.image.load("character/a2l12.png").convert_alpha(), (200, 190)),
          pygame.transform.scale(pygame.image.load("character/a2l13.png").convert_alpha(), (90, 190)),
      ]

  def animate(self):
      now = pygame.time.get_ticks()
      if self.facing=="right" and self.haraket==1:
        if now - self.last_update > self.frame_rate:
          self.last_update = now
          self.current_frame = (self.current_frame + 1) % len(self.walk_frames)
          self.image = self.walk_frames[self.current_frame]
      elif self.facing=="left" and self.haraket==1:
        if now - self.last_update > self.frame_rate:
          self.last_update = now
          self.current_frame = (self.current_frame + 1) % len(self.walk_frames_left)
          self.image = self.walk_frames_left[self.current_frame]
      elif self.facing=="attack" and self.facing2=="right":
        if now - self.last_update > self.frame_rate:
          self.last_update = now
          self.current_frame = (self.current_frame + 1) % len(self.attack_frames)
          self.image = self.attack_frames[self.current_frame]
          self.rect = self.image.get_rect(topleft=self.rect.topleft) 
      elif self.facing=="attack" and self.facing2=="left":
        if now - self.last_update > self.frame_rate:
          self.last_update = now
          self.current_frame = (self.current_frame + 1) % len(self.attack_frames_left)
          self.image = self.attack_frames_left[self.current_frame]
          self.rect = self.image.get_rect(topleft=self.rect.topleft) 
      elif self.facing=="attack2" and self.facing2=="right":
        if now - self.last_update > self.frame_rate:
          self.last_update = now
          self.current_frame = (self.current_frame + 1) % len(self.attack_frames2)
          self.image = self.attack_frames2[self.current_frame]
          self.rect = self.image.get_rect(topleft=self.rect.topleft) 
      elif self.facing=="attack2" and self.facing2=="left":
        if now - self.last_update > self.frame_rate:
          self.last_update = now
          self.current_frame = (self.current_frame + 1) % len(self.attack_frames2_left)
          self.image = self.attack_frames2_left[self.current_frame]
          self.rect = self.image.get_rect(topleft=self.rect.topleft) 
      elif self.facing=="stay" and self.facing2=="right":
        if now - self.last_update > self.frame_rate:
          self.last_update = now
          self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
          self.image = self.standing_frames[self.current_frame]
          self.rect = self.image.get_rect(topleft=self.rect.topleft)

  def get_input(self):
    keys = pygame.key.get_pressed()
    if self.oyun_durdu == 0:
      if keys[pygame.K_SPACE]:
          print("space ye basıldı")
          self.haraket = 1
          self.saldırı = 1
          self.facing = "attack"
          self.direction.x = 0  # Hareketi durdur
      elif keys[pygame.K_e]:
          if self.e_doldu>=150:
            print("e ye basıldı")
            self.attack = 1
            self.saldırı2 = 1
            self.facing = "attack2"
            self.e_sıfırlama=1
            self.direction.x = 0  # Hareketi durdur
            if self.e_sıfırlama==1:
               self.e_süre+=0.5
      elif keys[pygame.K_d]:
          self.direction.x = 0.4
          self.facing = "right"
          self.facing2 = "right"
          self.haraket = 1
      elif keys[pygame.K_a]:
          self.direction.x = -0.4
          self.facing = "left"
          self.facing2 = "left"
          self.haraket = 1
      else:
          self.direction.x = 0
          self.facing = "stay"
          self.haraket = 0
          if self.facing2=="right":
            self.image = self.standing_frames[0]
          if self.facing2=="left":
            self.image = self.standing_frames2[0]
          self.rect = self.image.get_rect(topleft=self.rect.topleft)
          self.saldırı = 0
          self.saldırı2 = 0

    if keys[pygame.K_w] and not self.is_jumping:
          self.jump()
      
    if self.rect.left < 0:
        self.rect.left = 0
    if self.rect.right > en:
        self.rect.right = en
    if self.rect.top < 0:
        self.rect.top = 0
    if self.rect.bottom > boy:
        self.rect.bottom = boy

  def apply_gravity(self):
    self.direction.y+=self.gravity
    self.rect.y+=self.direction.y
  
  def jump(self):
    self.direction.y=self.jump_speed
    self.is_jumping = True
    
  def update(self):
    self.e_doldu+=0.3
    if self.e_süre>=30:
      self.e_doldu=0
      self.e_süre=0

    self.get_input()
    if self.haraket == 1 or self.attack == 1:
        self.animate()
    self.image.set_colorkey((255, 255, 255))

class Player2(pygame.sprite.Sprite):
  def __init__(self,pos):
    super().__init__() 
    self.facing2="left"
    self.load_images()  
    self.image = self.standing_frames[0]  
    self.rect = self.image.get_rect(topleft=pos)
    self.current_frame = 0
    self.last_update = pygame.time.get_ticks()
    self.frame_rate = 100
    self.vuruş_ses= pygame.mixer.Sound("character/vuruş5.mp3")
    
    self.direction=pygame.math.Vector2(0,0)
    self.speed=8
    self.gravity=1
    self.jump_speed=-13
    self.is_jumping = False
    self.facing="stay"
    self.right, self.left=0,0
    self.haraket=0
    self.p_doldu=False
    self.saldırı2 = 1
    self.saldırı = 0

    self.total_distance = 0

    self.attack_index = 0
    self.attack_counter = 0
    self.is_attacking=False
    self.attack=0
    self.pos = pos
    self.oyun_durdu=0
    self.p_doldu = 0
    self.p_süre = 0
    self.p_sıfırlama = 0

  def load_images(self):
      self.standing_frames = [pygame.transform.scale(pygame.image.load("character/2s1.png").convert_alpha(), (95, 180))]
      self.standing_frames2 = [pygame.transform.scale(pygame.image.load("character/2sr1.png").convert_alpha(), (95, 180))]
      self.walk_frames = [
          pygame.transform.scale(pygame.image.load("character/2w1.png").convert_alpha(), (105, 200)),
          pygame.transform.scale(pygame.image.load("character/2w2.png").convert_alpha(), (105, 200)),
          pygame.transform.scale(pygame.image.load("character/2w3.png").convert_alpha(), (110, 200)),
          pygame.transform.scale(pygame.image.load("character/2w4.png").convert_alpha(), (115, 200)),
          pygame.transform.scale(pygame.image.load("character/2w5.png").convert_alpha(), (105, 200)),
          pygame.transform.scale(pygame.image.load("character/2w6.png").convert_alpha(), (105, 200)),
          pygame.transform.scale(pygame.image.load("character/2w7.png").convert_alpha(), (110, 200)),
          pygame.transform.scale(pygame.image.load("character/2w8.png").convert_alpha(), (115, 200)),
      ]
      self.walk_frames_left = [
          pygame.transform.scale(pygame.image.load("character/2wl1.png").convert_alpha(), (105, 200)),
          pygame.transform.scale(pygame.image.load("character/2wl2.png").convert_alpha(), (105, 200)),
          pygame.transform.scale(pygame.image.load("character/2wl3.png").convert_alpha(), (110, 200)),
          pygame.transform.scale(pygame.image.load("character/2wl4.png").convert_alpha(), (115, 200)),
          pygame.transform.scale(pygame.image.load("character/2wl5.png").convert_alpha(), (105, 200)),
          pygame.transform.scale(pygame.image.load("character/2wl6.png").convert_alpha(), (105, 200)),
          pygame.transform.scale(pygame.image.load("character/2wl7.png").convert_alpha(), (110, 200)),
          pygame.transform.scale(pygame.image.load("character/2wl8.png").convert_alpha(), (115, 200)),
      ]

      self.attack_frames = [
          pygame.transform.scale(pygame.image.load("character/2a1.png").convert_alpha(), (185, 180)),
          pygame.transform.scale(pygame.image.load("character/2a2.png").convert_alpha(), (220, 180)),
          pygame.transform.scale(pygame.image.load("character/2a3.png").convert_alpha(), (166, 180)),
          pygame.transform.scale(pygame.image.load("character/2a4.png").convert_alpha(), (165, 180)),
          pygame.transform.scale(pygame.image.load("character/2a5.png").convert_alpha(), (160, 180)),
          pygame.transform.scale(pygame.image.load("character/2a6.png").convert_alpha(), (110, 180)),
      ]
      self.attack_frames_left = [
          pygame.transform.scale(pygame.image.load("character/2al1.png").convert_alpha(), (185, 180)),
          pygame.transform.scale(pygame.image.load("character/2al2.png").convert_alpha(), (220, 180)),
          pygame.transform.scale(pygame.image.load("character/2al3.png").convert_alpha(), (166, 180)),
          pygame.transform.scale(pygame.image.load("character/2al4.png").convert_alpha(), (165, 180)),
          pygame.transform.scale(pygame.image.load("character/2al5.png").convert_alpha(), (160, 180)),
          pygame.transform.scale(pygame.image.load("character/2al6.png").convert_alpha(), (110, 180)),
      ]
      self.attack_frames2 = [
          pygame.transform.scale(pygame.image.load("character/2a21.png").convert_alpha(), (175, 180)),
          pygame.transform.scale(pygame.image.load("character/2a22.png").convert_alpha(), (185, 180)),
          pygame.transform.scale(pygame.image.load("character/2a23.png").convert_alpha(), (245, 180)),
          pygame.transform.scale(pygame.image.load("character/2a24.png").convert_alpha(), (195, 180)),
          pygame.transform.scale(pygame.image.load("character/2a25.png").convert_alpha(), (190, 180)),]
      self.attack_frames2_left = [
          pygame.transform.scale(pygame.image.load("character/2a2l1.png").convert_alpha(), (175, 180)),
          pygame.transform.scale(pygame.image.load("character/2a2l2.png").convert_alpha(), (185, 180)),
          pygame.transform.scale(pygame.image.load("character/2a2l3.png").convert_alpha(), (245, 180)),
          pygame.transform.scale(pygame.image.load("character/2a2l4.png").convert_alpha(), (195, 180)),
          pygame.transform.scale(pygame.image.load("character/2a2l5.png").convert_alpha(), (190, 180)),]

  def animate(self):
      now = pygame.time.get_ticks()
      if self.facing=="right":
        if now - self.last_update > self.frame_rate:
          self.last_update = now
          self.current_frame = (self.current_frame + 1) % len(self.walk_frames)
          self.image = self.walk_frames[self.current_frame]
      elif self.facing=="left":
        if now - self.last_update > self.frame_rate:
          self.last_update = now
          self.current_frame = (self.current_frame + 1) % len(self.walk_frames_left)
          self.image = self.walk_frames_left[self.current_frame]
      elif self.facing=="attack" and self.facing2=="right":
        if now - self.last_update > self.frame_rate:
          self.last_update = now
          self.current_frame = (self.current_frame + 1) % len(self.attack_frames)
          self.image = self.attack_frames[self.current_frame]
          self.rect = self.image.get_rect(topleft=self.rect.topleft) 
      elif self.facing=="attack" and self.facing2=="left":
        if now - self.last_update > self.frame_rate:
          self.last_update = now
          self.current_frame = (self.current_frame + 1) % len(self.attack_frames_left)
          self.image = self.attack_frames_left[self.current_frame]
          self.rect = self.image.get_rect(topleft=self.rect.topleft) 
      elif self.facing=="attack2" and self.facing2=="left":
        if now - self.last_update > self.frame_rate:
          self.last_update = now
          self.current_frame = (self.current_frame + 1) % len(self.attack_frames2_left)
          self.image = self.attack_frames2_left[self.current_frame]
          self.rect = self.image.get_rect(topleft=self.rect.topleft) 
      elif self.facing=="attack2" and self.facing2=="right":
        if now - self.last_update > self.frame_rate:
          self.last_update = now
          self.current_frame = (self.current_frame + 1) % len(self.attack_frames2)
          self.image = self.attack_frames2[self.current_frame]
          self.rect = self.image.get_rect(topleft=self.rect.topleft) 
      elif self.facing=="stay" and self.facing2=="left":
        if now - self.last_update > self.frame_rate:
          self.last_update = now
          self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
          self.image = self.standing_frames[self.current_frame]
          self.rect = self.image.get_rect(topleft=self.rect.topleft)

  def get_input(self):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RETURN]:
        self.haraket = 1
        self.saldırı = 1
        self.facing = "attack"
        self.direction.x = 0  # Hareketi durdur
    elif keys[pygame.K_p]:
          if self.p_doldu>=150:
            print("e ye basıldı")
            self.attack = 1
            self.saldırı2 = 1
            self.facing = "attack2"
            self.p_sıfırlama=1
            self.direction.x = 0 
            if self.p_sıfırlama==1:
               self.p_süre+=0.5
    elif keys[pygame.K_RIGHT]:
        self.direction.x = 0.4
        self.facing = "right"
        self.facing2 = "right"
        self.haraket = 1
    elif keys[pygame.K_LEFT]:
        self.direction.x = -0.4
        self.facing = "left"
        self.facing2 = "left"
        self.haraket = 1
    else:
        self.direction.x = 0
        self.facing = "stay"
        self.haraket = 0
        if self.facing2=="left":
          self.image = self.standing_frames[0]
        elif self.facing2=="right":
          self.image = self.standing_frames2[0]
        self.rect = self.image.get_rect(topleft=self.rect.topleft)
        self.saldırı = 0
        self.saldırı2 = 0

    if keys[pygame.K_UP] and not self.is_jumping:
        self.jump()
  
    # Ekran sınırlarını kontrol et
    if self.rect.left < 0:
        self.rect.left = 0
    if self.rect.right > en:
        self.rect.right = en
    if self.rect.top < 0:
        self.rect.top = 0
    if self.rect.bottom > boy:
        self.rect.bottom = boy

  def apply_gravity(self):
    self.direction.y+=self.gravity
    self.rect.y+=self.direction.y
  
  def jump(self):
    self.direction.y=self.jump_speed
    self.is_jumping = True
    
  def update(self):
    self.p_doldu+=0.3
    if self.p_süre>=30:
      self.p_doldu=0
      self.p_süre=0

    self.get_input()
    if self.haraket==1 or self.attack==1:
      self.animate()
    self.image.set_colorkey((255, 255, 255))