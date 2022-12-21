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
arkaplan = bg = pg.image.load("background.jpg")

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT :
            pg.quit()
            sys.exit();
    #ekran.fill(beyaz)
    ekran.blit(pg.transform.scale (bg, (1200,800)), (0,0))

### Tüm Oyun Mantığı Buranın Altına Yazılacak









#Buraya da Ekrandaki Çizimler Girilecek
    #pg.draw.rect(ekran, k_mavi, (250, 550, 500, 12), 6)              #Denge Cubugu








    pg.display.flip()
    clock.tick(20) #Fps ayarlamak için