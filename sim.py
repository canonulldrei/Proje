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
        return action

# Butonlari atama
start_btn = Butonlar(950, 150, start_img, 1)
restart_btn = Butonlar(1050, 150, restart_img, 1)

#Boyut ve arkaplan
en , boy = 1200 , 700
ekran = pg.display.set_mode( (en , boy) )
pg.display.set_caption("Tork ve Denge Simülasyonu")
pg.display.set_icon(pg.image.load("img/kettlebell_5.png"))
arkaplan = pg.image.load("img/background.png")
taban = pg.image.load("img/ground.png")

#Tahterevalli
tahterevalli = pg.image.load("img/stick.png").convert_alpha()
tahterevalli_rect = tahterevalli.get_rect()
tahterevalli_rect.x = 100
tahterevalli_rect.y = 540



 #Agirliklar
  # Birinci 5 Kg
kg1 = pg.image.load("img/kettlebell_5.png")
kg1_rect = kg1.get_rect()
kg1_rect.x = 800
kg1_rect.y = 80
is_clicked_kg1 = False

  # Ikinci 5 Kg
kg2 = pg.image.load("img/kettlebell_5.png")
kg2_rect = kg2.get_rect()
kg2_rect.x = 850
kg2_rect.y = 80
is_clicked_kg2 = False

  # Birinci 10 Kg
kg3 = pg.image.load("img/kettlebell_10.png")
kg3_rect = kg3.get_rect()
kg3_rect.y = 900
kg3_rect.y = 80
is_clicked_kg3 = False

  # Ikinci 10 Kg
kg4 = pg.image.load("img/kettelebell_10.png")
kg4_rect = kg4.get_rect()
kg4_rect.x = 950
kg4_rect.y = 80
is_clicked_kg4 = False

  # Birinci 20 Kg
kg5 = pg.image.load("img/kettlebell_20.png")
kg5_rect = kg5.get_rect()
kg5_rect.x = 1000
kg5_rect.y = 80
is_clicked_kg5 = False

  # Ikinci 20 Kg
kg6 = pg.image.load("img/kettlebell_20.png")
kg6_rect = kg6.get_rect()
kg6_rect.x = 1050
kg6_rect.y = 80
is_clicked_kg6 = False


#Oyun Döngüsü
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT :
            run=False
            pg.quit()
            sys.exit();


#Ekranda cikacak ögeler
    ekran.blit(tahterevalli, tahterevalli_rect)
    ekran.blit(taban, (520,565) )
    # ekran.blit(pg.transform.scale (kb_5,(38,51)), (900,80))
    # ekran.blit(pg.transform.scale (kb_5,(38,51)), (950,80))
    # ekran.blit(pg.transform.scale (kb_10,(38,51)), (1000,80))
    # ekran.blit(pg.transform.scale (kb_10,(38,51)), (1050,80))
    # ekran.blit(pg.transform.scale (kb_20,(38,51)), (1100,80))
    # ekran.blit(pg.transform.scale (kb_20,(38,51)), (1150,80))

    #En asagida olacak
    pg.display.update()

### Tüm Oyun Mantığı Buranın Altına Yazılacak ###




#Tork hesaplama
#Tahterevalliyi orta noktasindan hareket ettirme ve üzerinde belli uzakliklar tanimlayabilme
#Agirliklari mouse ile sürükleme
#Tahterevalliyi üzerine binen agirliklara göre hareket ettirme
# #Agirliklari tahterevalli üzerinde yerlestirme ve isleme alma





    clock.tick(FPS)
    pg.display.flip()
