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

#Ekran ölcüleri
en , boy = 1200 , 800

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





#Boyut ve arkaplan
ekran = pg.display.set_mode( (en , boy) )
pg.display.set_caption("Tork ve Denge Simülasyonu")
bg = pg.image.load("img/background.png")

#Tahterevalli
st = pg.image.load("img/stick.png")

#####################################################
stick_rect = st.get_rect()
#çubuğun orta noktasını belirlemek için
stick_rect.centerx = ekran.get_rect().centerx
stick_rect.bottom = ekran.get_rect().bottom
####################################################
st.convert()

taban =tb =pg.image.load("img/ground.png")
tb.convert()
#Agirliklar
kettlebell_5 = kb_5 =pg.image.load("img/kettlebell_5.png")
kb_5.convert()
kettlebell_10 = kb_10 =pg.image.load("img/kettlebell_10.png")
kb_10.convert()
kettlebell_20 = kb_20 =pg.image.load("img/kettlebell_20.png")
kb_20.convert()

#Oyun Döngüsü
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT :
            run=False
            pg.quit()
            sys.exit();


#Ekranda cikacak ögeler
    ekran.blit(pg.transform.scale (bg, (1200,800)), (0,0))
    ekran.blit( st, (100,540) )
    ekran.blit( tb, (520,565) )
    ekran.blit(pg.transform.scale (kb_5,(38,51)), (900,80))
    ekran.blit(pg.transform.scale (kb_5,(38,51)), (950,80))
    ekran.blit(pg.transform.scale (kb_10,(38,51)), (1000,80))
    ekran.blit(pg.transform.scale (kb_10,(38,51)), (1050,80))
    ekran.blit(pg.transform.scale (kb_20,(38,51)), (1100,80))
    ekran.blit(pg.transform.scale (kb_20,(38,51)), (1150,80))

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
