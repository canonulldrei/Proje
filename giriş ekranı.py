import pygame as pg
import sys 

# Pygame'i baslatmak
pg.init()

# Ekran boyutunu ayarlama
en , boy = 1200 , 700
ekran = pg.display.set_mode(en, boy)

# Ekran ikonu ve basligi ayarlama 
pg.display.set_caption("Giriş Ekranı")
pg.display.set_icon(pg.image.load("img/kettlebell_10.png"))

# Ana ekranda kullanilacak font 
font = pg.font.Font(None, 32)

# Ana ekranda secenekler 
menu_scnk = ["Simülasyonu Başlat", "Bitir"]

# Arkaplan ve yazi rengi
bg_color = (18 , 102 , 31)
txt_color = (255 , 255 , 255)

# Secenekler secildiginde renk degistirmesi icin
secili_color = (255 , 0 , 0)

# Basligin görseli
baslik_img = pg.image.load("img/title.png")


# Ana döngüsü 
while True:
    # Olayları işle
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN
            # Fare konumunu alma
            mouse_x, mouse_y = pg.mouse.get_pos()
            # Farenin menü seçeneklerinden herhangi birinin üzerinde olup olmadığını kontrol etmek
            for i, item in enumerate(menu_items):
                text = font.render(item, True, text_renk)
                text_rect = text.get_rect()
                text_rect.center = (1200 // 2, 700 // 2 + i * 50)
                if text_rect.collidepoint(mouse_x, mouse_y):
                    # Seçeneği seç
                    if item == 'Simülasyonu Başlat':
                        # oyun başlat
                        # oyun penceresi boyutunu ayarlayın
                        ekran = pg.display.set_mode((1200, 800))
                        # Pencere hacmı ayarla
                        pg.display.set_caption('My Game')
                        # Arka plan resmini yükle
                        background_image = pg.image.load('img/background.png')
                        # Arka plan resmini ayarla
                        ekran.blit(background_image, (0, 0))
                        exec(open("stack ve işaret birleştirme.py").read())
                        # Oyun döngüsü
                        while True:
                            # Olayları işle
                            for event in pg.event.get():
                                if event.type == pg.QUIT:
                                    pg.quit()
                                    sys.exit()
                            # Ekranı güncelle