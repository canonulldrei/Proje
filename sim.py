import pygame as pg 
import sys
import math

#Pygame'i baslatmak
pg.init()

#Degiskenler 
angle =0
weight = 0
mass = 0
started = False

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

# Butona özellik atama
start_btn =Butonlar(850, 150, start_img, 1)
restart_btn =Butonlar(1000, 150, restart_img, 1)

#Ekran olusturma 
boyut = (1200, 700)
ekran = pg.display.set_mode(boyut)
arkaplan = pg.image.load("img/background.png")
pg.display.set_caption("Tork ve Denge Simülasyonu")
pg.display.set_icon(pg.image.load("img/kettlebell_10.png"))

#Tahterevalli tabani
taban = pg.image.load("img/ground.png")

#Tahterevalli
tahterevalli = pg.image.load("img/stick.png")
tahterevalli_rect = tahterevalli.get_rect()
tahterevalli_rect.x = 100
tahterevalli_rect.y = 540

# Agirliklar 
 # Birinci 5 Kg
kg1 = pg.image.load("img/kettlebell_5.png") 
kg1_rect =kg1.get_rect() 
kg1_rect.x = 800
kg1_rect.y = 80
is_clicked_kg1 =False

 # Ikinci 5 Kg
kg2 = pg.image.load("img/kettlebell_5.png") 
kg2_rect =kg2.get_rect() 
kg2_rect.x = 850
kg2_rect.y = 80
is_clicked_kg2 =False

 # Birinci 10 Kg
kg3 = pg.image.load("img/kettlebell_10.png") 
kg3_rect =kg1.get_rect() 
kg3_rect.x = 900
kg3_rect.y = 80
is_clicked_kg3 =False

 # Ikinci 10 Kg
kg4 = pg.image.load("img/kettlebell_10.png") 
kg4_rect =kg4.get_rect() 
kg4_rect.x = 950
kg4_rect.y = 80
is_clicked_kg4 =False

 # Birinci 20 Kg
kg5 = pg.image.load("img/kettlebell_20.png") 
kg5_rect =kg5.get_rect() 
kg5_rect.x = 1000
kg5_rect.y = 80
is_clicked_kg5 =False

 # Ikinci 20 Kg
kg6 = pg.image.load("img/kettlebell_20.png") 
kg6_rect =kg6.get_rect() 
kg6_rect.x = 1050
kg6_rect.y = 80
is_clicked_kg6 =False


collide = False
running = True
while running:

    markers = []
    markers_rect = []

# Tahterevalli üzerinde işaretler oluşturun
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
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
        kg1_rect.x = mouse_pos[0] - kg1_rect.width/2
        kg1_rect.y = mouse_pos[1] - kg1_rect.height/2

# Basıldığında "kg2" hareket ettir
    if is_clicked_kg2:
        mouse_pos = pg.mouse.get_pos()
        kg2_rect.x = mouse_pos[0] - kg2_rect.width/2
        kg2_rect.y = mouse_pos[1] - kg2_rect.height/2

# Basıldığında "kg3" hareket ettir

    if is_clicked_kg3:
        mouse_pos = pg.mouse.get_pos()
        kg3_rect.x = mouse_pos[0] - kg3_rect.width/2
        kg3_rect.y = mouse_pos[1] - kg3_rect.height/2

# Basıldığında "kg4" hareket ettir
    if is_clicked_kg4:
        mouse_pos = pg.mouse.get_pos()
        kg4_rect.x = mouse_pos[0] - kg4_rect.width/2
        kg4_rect.y = mouse_pos[1] - kg4_rect.height/2

# Basıldığında "kg5" hareket ettir
    if is_clicked_kg5:
        mouse_pos = pg.mouse.get_pos()
        kg5_rect.x = mouse_pos[0] - kg5_rect.width/2
        kg5_rect.y = mouse_pos[1] - kg5_rect.height/2

# Basıldığında "kg6" hareket ettir
    if is_clicked_kg6:
        mouse_pos = pg.mouse.get_pos()
        kg6_rect.x = mouse_pos[0] - kg6_rect.width/2
        kg6_rect.y = mouse_pos[1] - kg6_rect.height/2

# ekran temizle
    ekran.fill((255, 255, 255))
# Arkaplan ekleme
    ekran.blit(arkaplan, (0,0))
    ekran.blit(taban,(520,560))
# "Tahterevalli" resimleri çiz
    copy = pg.transform.rotate(tahterevalli, angle)
    ekran.blit(copy, (600 - int(copy.get_width() / 2), 
                551 - int(copy.get_height()/2)))

# Çarpışma algılama sürecini kolaylaştırmak için tüm ağırlıkları tek bir diziye eklemek
    allrects = []
    allrects.append(kg1_rect)            
    allrects.append(kg2_rect)
    allrects.append(kg3_rect)
    allrects.append(kg4_rect)
    allrects.append(kg5_rect)
    allrects.append(kg6_rect)
    
    weights = [0,0,0,0,0,0]

    for i in range(9):
        marker = pg.Surface((5, 24))
        marker.fill((0, 0, 0))
        marker_rect_sol = marker.get_rect()
        marker_rect_sag = marker.get_rect()

# Çubuk boyunca işaretçi hareketlerinin hesaplanması

        marker_rect_sol.centerx = tahterevalli_rect.centerx + (i - 9) * 50
        marker_rect_sol.centery = tahterevalli_rect.centery + angle*9.4 - ((i + 1) * angle)
        marker_rect_sag.centerx = tahterevalli_rect.centerx + (i + 1) * 50
        marker_rect_sag.centery = tahterevalli_rect.centery - ((i + 1) * angle) +angle*0.7
        markers.append((marker, marker_rect_sol))
        markers.append((marker, marker_rect_sag))
        markers_rect.append(marker.get_rect())

# Her işaretleyicide çarpışma kontrolü

    for marker, marker_rect in markers:
        index = marker_rect.collidelist(allrects)

        thisrect = allrects[index]
        if index >= 0:
            thisrect.x = marker_rect.x - 17
            thisrect.y = marker_rect.y - 50

            thisrect.y += 1

# Bu formülü kullanarak denge işleminin hesaplanması : "tork= uzaklık(orta noktaya göre)*kuvvet (ağırlıklarla)"
            
            if index == 0 or index == 1:
                mass = 5
            elif index == 2 or index == 3:
                mass = 10
            else:
                mass = 20

            weights[index] += (581 - thisrect.x) * mass

            marker.fill((255, 0, 0))

        else:
            marker.fill((0, 0, 0))
# Çubuğu döndürmek
        if angle > (weight/700):
            angle -= 0.005
        elif angle < (weight/700):
            angle += 0.005

        ekran.blit(marker, marker_rect)
    
    if started :
        weight = weights[0] + weights[1] + weights[2] + weights[3] + weights[4] + weights[5]

# Ağırlık
    ekran.blit(kg1, kg1_rect)
    ekran.blit(kg2, kg2_rect)
    ekran.blit(kg3, kg3_rect)
    ekran.blit(kg4, kg4_rect)
    ekran.blit(kg5, kg5_rect)
    ekran.blit(kg6, kg6_rect)

# Yeniden başlat düğmesine basıldığında oyunun yeniden başlatılması

    if start_btn.draw() == True :
        started = True
    if restart_btn.draw() == True :
        kg1_rect.x = 800
        kg1_rect.y = 80

        kg2_rect.x = 850
        kg2_rect.y = 80

        kg3_rect.x = 900
        kg3_rect.y = 80

        kg4_rect.x = 950
        kg4_rect.y = 80

        kg5_rect.x = 1000
        kg5_rect.y = 80

        kg6_rect.x = 1050
        kg6_rect.y = 80

        started = False
        weight = 0
    
    pg.display.update()

# Ekranı güncelle

    pg.display.flip()