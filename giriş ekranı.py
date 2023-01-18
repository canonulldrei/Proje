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

