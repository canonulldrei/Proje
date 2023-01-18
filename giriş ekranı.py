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

#Buradan sonra ana döngü gelecek