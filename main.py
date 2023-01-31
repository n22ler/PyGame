import pygame as pg
from const import *
from gun import Gun
from random import randint
from controls import events, update_screen, update_blt, create_enemy, update_nlo
from pygame.sprite import Group
from stats import Stats




def run():

    pg.init()
    sc= pg.display.set_mode((WIDTH,HEIGHT))
    pg.display.set_caption("Егорка в танке")
    gun = Gun(sc)
    bullets= Group()
    nlos = Group()
    create_enemy(sc, nlos)
    stats = Stats()



    while True:
        
        events(sc,gun, bullets)
        gun.update_position()
        update_screen(WHITE, sc, gun, nlos, bullets)
        update_blt(sc,nlos,bullets)
        update_nlo(stats, sc, gun, nlos, bullets)

run()