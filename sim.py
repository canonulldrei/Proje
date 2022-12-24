import pygame as pg 
import sys
pg.init()
clock = pg.time.Clock()

en , boy = 1200 , 800 #Ekran Büyüklügü

#Renkler
siyah =  0 , 0 , 0
beyaz = 255 , 255 , 255
gri = 125 , 125 , 125
yesil = 61 , 252 , 3
k_mavi = 5 , 7 , 54
sari = 209 , 209 , 46

#Boyut ve arkaplan
ekran = pg.display.set_mode( (en , boy ) )
pg.display.set_caption("Tork ve Denge Simülasyonu")
arkaplan = bg = pg.image.load("background.jpg")
#Tahterevalli
stick = st = pg.image.load("stick.png")
taban =tb =pg.image.load("taban.png")
#Agirliklar
kettlebell_5 = kb_5 =pg.image.load("kettlebell_5.png")
kettlebell_10 = kb_10 =pg.image.load("kettlebell_10.png")
kettlebell_20 = kb_20 =pg.image.load("kettlebell_20.png")

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT :
            pg.quit()
            sys.exit();
#Ekranda cikacak ögeler
    ekran.blit(pg.transform.scale (bg, (1200,800)), (0,0))
    ekran.blit( st, (124,540) )
    ekran.blit( tb, (480,570) )
    ekran.blit(pg.transform.scale (kb_5,(38,51)), (950,80))
    ekran.blit(pg.transform.scale (kb_5,(38,51)), (1000,80))
    ekran.blit(pg.transform.scale (kb_10,(38,51)), (1050,80))
    ekran.blit(pg.transform.scale (kb_20,(38,51)), (1100,80))

### Tüm Oyun Mantığı Buranın Altına Yazılacak

#Tork hesaplama







#Buraya da Ekrandaki Çizimler Girilecek









    pg.display.flip()
    clock.tick(20) #Fps ayarlamak için