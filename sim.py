import pygame as pg 
import sys
import pyautogui #mouse hareketlei icin kütüphane

#Pygame'i baslatmak
pg.init()
clock = pg.time.Clock()

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

#Boyut ve arkaplan
ekran = pg.display.set_mode( (en , boy ) )
pg.display.set_caption("Tork ve Denge Simülasyonu")
arkaplan = bg = pg.image.load("img/background.jpg")

#Tahterevalli
stick = st = pg.image.load("img/stick.png")
st.convert()
taban =tb =pg.image.load("img/taban.png")
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
    ekran.blit( st, (124,540) )
    ekran.blit( tb, (480,570) )
    ekran.blit(pg.transform.scale (kb_5,(38,51)), (900,80))
    ekran.blit(pg.transform.scale (kb_5,(38,51)), (950,80))
    ekran.blit(pg.transform.scale (kb_10,(38,51)), (1000,80))
    ekran.blit(pg.transform.scale (kb_10,(38,51)), (1050,80))
    ekran.blit(pg.transform.scale (kb_20,(38,51)), (1100,80))
    ekran.blit(pg.transform.scale (kb_20,(38,51)), (1150,80))
    pg.display.update()

### Tüm Oyun Mantığı Buranın Altına Yazılacak ###

#Tork hesaplama
#def torque():   #Burada temel hesaplamamiz icin tork = kuvvet*kuvvet kolu  bagintisi girilmeli



#Tahterevalliyi orta noktasindan hareket ettirme ve üzerinde belli uzakliklar tanimlayabilme





######Agirliklari mouse ile sürükleme



#Tahterevalliyi üzerine binen agirliklara göre hareket ettirme



#Agirliklari tahterevalli üzerinde yerlestirme ve isleme alma




####Buraya da Ekrandaki Çizimler Girilecek

abdo

clock.tick(FPS)
pg.display.flip()
