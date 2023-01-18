import pygame as pg 
import sys
import math

#Pygame'i baslatmak
pg.init()
clock = pg.time.Clock()

#Degiskenler 
aci =0
agirlik = 0
kütle = 0
basladi = False

#FPS ayari
FPS = 30

#Renkler
siyah =  0 , 0 , 0
beyaz = 255 , 255 , 255
gri = 125 , 125 , 125
yesil = 61 , 252 , 3
k_mavi = 5 , 7 , 54
sari = 209 , 209 , 46
bej = 191, 149, 113
a_mavi = 00 , 100 , 100  #degistirilecek

#Baslama ve restart butonu
start_img = pg.image.load("img/start.png") 
restart_img = pg.image.load("img/restart.png") 

#Butonlari class ile tanimlama 
class Butonlar():
    def __init__(self, x, y, img, oran):
        en  = img.get_width()
        boy = img.get_height()
        self.img = pg.transform.scale(img, (int(en*oran), int(boy*oran)))
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        pozisyon =pg.mouse.get_pos()

        if self.rect.collidepoint(pozisyon):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pg.mouse.get_pressed()[0] == 1:
            self.clicked = False 

# Butonlari ekrana cizdirme
        ekran.blit(self.img, (self.rect.x, self.rect.y))
        return action,




    collide = False
    running = True
    while running:

        markers = []
        markers_rect = []

# Tahterevalli üzerinde işaretler oluşturun
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            # Fare konumunu al
            mouse_pos = pg.mouse.get_pos()
            # kg1 tıklanma kontrol
            if kg1_rect.collidepoint(mouse_pos):
                is_clicked_kg1 = True
            # kg2 tıklanma kontrol
            if kg2_rect.collidepoint(mouse_pos):
                is_clicked_kg2 = True
            # kg3 tıklanma kontrol
            if kg3_rect.collidepoint(mouse_pos):
                is_clicked_kg3 = True
            # kg4 tıklanma kontrol
            if kg4_rect.collidepoint(mouse_pos):
                is_clicked_kg4 = True
            # kg5 tıklanma kontrol
            if kg5_rect.collidepoint(mouse_pos):
                is_clicked_kg5 = True
            # kg6 tıklanma kontrol
            if kg6_rect.collidepoint(mouse_pos):
                is_clicked_kg6 = True
        elif event.type == pg.MOUSEBUTTONUP:
            is_clicked_kg1 = False
            is_clicked_kg2 = False
            is_clicked_kg3 = False
            is_clicked_kg4 = False
            is_clicked_kg5 = False
            is_clicked_kg6 = False 
    
    # Basıldığında "kg1" hareket ettir

    if is_clicked_kg1:
        mouse_pos = pg.mouse.get_pos()
        kg1_rect.x = mouse_pos[0] - kg1_rect.en/2
        kg1_rect.y = mouse_pos[1] - kg1_rect.boy/2

    # Basıldığında "kg2" hareket ettir

     if is_clicked_kg2:
            mouse_pos = pg.mouse.get_pos()
        kg2_rect.x = mouse_pos[0] - kg2_rect.en/2
        kg2_rect.y = mouse_pos[1] - kg2_rect.boy/2

    # Basıldığında "kg3" hareket ettir

     if is_clicked_kg3:
            mouse_pos = pg.mouse.get_pos()
        kg3_rect.x = mouse_pos[0] - kg3_rect.en/2
        kg3_rect.y = mouse_pos[1] - kg3_rect.boy/2
                            
    # Basıldığında "kg4" hareket ettir

     if is_clicked_kg4:
            mouse_pos = pg.mouse.get_pos()
        kg4_rect.x = mouse_pos[0] - kg4_rect.en/2
        kg4_rect.y = mouse_pos[1] - kg4_rect.boy/2

    # Basıldığında "kg5" hareket ettir

     if is_clicked_kg5:
            mouse_pos = pg.mouse.get_pos()
        kg5_rect.x = mouse_pos[0] - kg5_rect.en/2
        kg5_rect.y = mouse_pos[1] - kg5_rect.boy/2

    # Basıldığında "kg6" hareket ettir

     if is_clicked_kg6:
            mouse_pos = pg.mouse.get_pos()
        kg6_rect.x = mouse_pos[0] - kg6_rect.en/2
        kg6_rect.y = mouse_pos[1] - kg6_rect.boy/2
 






   































clock.tick(FPS)
pg.display.flip()