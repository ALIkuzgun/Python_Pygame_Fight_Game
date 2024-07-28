import pygame,time
import sys
from config import *
from level import *

pygame.init()

ekran = pygame.display.set_mode((en, boy))
clock = pygame.time.Clock()

pygame.display.set_caption("Fighting Game")

bg = pygame.image.load("character/bg.png").convert_alpha()
bg = pygame.transform.scale(bg, (en, boy))

süre = 0
click_ses= pygame.mixer.Sound("character/click.wav")

level = Level(level_map, ekran)

while True:
    mouse_pos = pygame.mouse.get_pos()
    if level.draw_button_rect2.collidepoint(mouse_pos):
        level.buton2_text_color = (23,23,23)
    else:
        level.buton2_text_color = (255,255,255)

    if level.draw_button_rect3.collidepoint(mouse_pos):
        level.buton3_text_color = (23,23,23)
    else:
        level.buton3_text_color = (255,255,255)

    if level.draw_button_rect4.collidepoint(mouse_pos):
        level.buton4_text_color = (23,23,23)
    else:
        level.buton4_text_color = (255,255,255)

    if level.draw_button_rect5.collidepoint(mouse_pos):
        level.buton5_text_color = (23,23,23)
    else:
        level.buton5_text_color = (255,255,255)

    if level.draw_button_rect6.collidepoint(mouse_pos):
        level.buton6_text_color = (23,23,23)
    else:
        level.buton6_text_color = (255,255,255)

    if level.draw_button_rect7.collidepoint(mouse_pos):
        level.buton7_text_color = (23,23,23)
    else:
        level.buton7_text_color = (255,255,255)

    if level.draw_button_rect8.collidepoint(mouse_pos):
        level.buton8_text_color = (23,23,23)
    else:
        level.buton8_text_color = (255,255,255)

    if level.draw_button_rect9.collidepoint(mouse_pos):
        level.buton9_text_color = (23,23,23)
    else:
        level.buton9_text_color = (255,255,255)

    if level.draw_button_rect10.collidepoint(mouse_pos):
        level.buton10_text_color = (23,23,23)
    else:
        level.buton10_text_color = (255,255,255)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()      
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
              # menu
              if level.menu_durum=="0":
                if level.draw_button_rect2.collidepoint(event.pos):
                    print("play")
                    level.menu_durum = "play"
                    click_ses.play()
                if level.draw_button_rect3.collidepoint(event.pos):
                    print("score")
                    level.menu_durum = "score"
                    click_ses.play()
                if level.draw_button_rect4.collidepoint(event.pos):
                    print("sound")
                    level.menu_durum = "sound"
                    click_ses.play()
              # scores       
              if level.menu_durum=="score":
                if level.draw_button_rect5.collidepoint(event.pos):
                    print("menu")
                    level.menu_durum="0"
                    click_ses.play()
              elif level.menu_durum=="sound":
                if level.draw_button_rect8.collidepoint(event.pos):
                    print("menu")
                    click_ses.play()
                    level.menu_durum="0"
                if level.draw_button_rect6.collidepoint(event.pos):
                    level.sound = 0
                    click_ses.play()
                if level.draw_button_rect7.collidepoint(event.pos):
                    level.sound = 0
                    click_ses.play()

              if level.players_died==1:
                if level.draw_button_rect9.collidepoint(event.pos):
                    click_ses.play()
                    level.menu_durum="0"
                    level.players_died=0
                    level.reset()
                if level.draw_button_rect10.collidepoint(event.pos):
                    click_ses.play()
                    level.menu_durum="play"
                    level.players_died=0
                    level.reset()
# 9002.3.2.fox
    ekran.fill((0, 245, 245))
    ekran.blit(bg, (0, 0))
    if level.health<=0:
        süre+=1
        if süre>30:
            level.health=0
            level.players_died=1
            if level.health==0 and level.player_gösterme==0:
              level.player2_score+=1
            level.player_gösterme=1
            level.players_died_menu()
    if level.health2<=0:
        süre+=1
        if süre>30:
            level.health2=0
            level.players_died=1
            if level.health2==0 and level.player_gösterme==0:
              level.player_score+=1
            level.player_gösterme=1
            level.players_died_menu()

    if level.menu_durum=="sound":
        level.sound_menu()
    if level.menu_durum=="score":
        level.score()
    if level.menu_durum=="0":
        level.menu()
    if level.menu_durum=="play" and level.players_died==0:
        pygame.draw.rect(ekran, (255, 255, 255), (27, 15, 356, 21))
        pygame.draw.rect(ekran, (255, 255, 255), (527, 15, 356, 21))
        pygame.draw.rect(ekran, (255, 255, 255), (27, 45, 156, 16))
        pygame.draw.rect(ekran, (255, 255, 255), (726, 45, 156, 16))
        level.run()
        font = pygame.font.Font("character/SHPinscher-Regular.otf", 30)
        text = font.render("P1", True, (255, 0, 0))
        ekran.blit(text, (360, 40))
        text2 = font.render("P2", True, (255, 0, 0))
        ekran.blit(text2, (525, 40))
    pygame.display.update()
    clock.tick(90)