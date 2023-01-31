import pygame as pg, sys
from const import WIDTH, HEIGHT
from bullet import Bullet
from nlo import Nlo
import time


def events(screen,gun, bullets): #евенты оружия
    for event in pg.event.get():
        if event.type == pg.QUIT: #exit
            sys.exit()
        elif event.type==pg.KEYDOWN: 
            if event.key==pg.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
            if event.key==pg.K_a: #left
                gun.mlt=True
            if event.key==pg.K_d: #right
                gun.mrt=True
        elif event.type ==pg.KEYUP:
            if event.key==pg.K_a: #left
                gun.mlt=False
            if event.key==pg.K_d: #right
                gun.mrt=False

def update_screen(color, screen, gun, nlos, bullets):
        screen.fill(color)
        for blt in bullets.sprites():
            blt.draw_blt()
        gun.output()
        nlos.draw(screen)
        pg.display.flip()

def update_blt(screen, nlos, bullets):
    bullets.update()
    for blt in bullets.copy():
        if blt.rect.bottom <= 0:
            bullets.remove(blt)
    collisions = pg.sprite.groupcollide(bullets, nlos, True, True)
    if len(nlos) ==0:
        bullets.empty()
        create_enemy(screen, nlos)


def create_enemy(screen, nlos):
    nlo = Nlo(screen)
    nlo_width = nlo.rect.width
    count_nlo_x = int((WIDTH - 2*nlo_width)/nlo_width)
    nlo_height = nlo.rect.height
    count_nlo_y = int((HEIGHT - 100 - 2*nlo_height)/nlo_height)

    for row in range(count_nlo_y):
        for nlo_ones in range(count_nlo_x):
            nlo = Nlo(screen)
            nlo.x = nlo_width + nlo_width * nlo_ones
            nlo.y = nlo_height +  nlo_height * row
            nlo.rect.x = nlo.x
            nlo.rect.y = nlo.rect.height + nlo.rect.height*row
            nlos.add(nlo)


def update_nlo(stats, screen,gun, nlos,bullets):
    nlos.update()
    if pg.sprite.spritecollideany(gun, nlos):
        gun_kill(stats, screen,gun, nlos,bullets)
    nlos_check(stats, screen, gun, nlos, bullets)


def gun_kill(stats, screen, gun, nlos, bullets):
    stats.gun_left -=1
    nlos.empty()
    bullets.empty()
    create_enemy(screen, nlos)
    gun.create_gun()
    time.sleep(2)


def nlos_check(stats, screen, gun, nlos, bullets):

    screen_rect = screen.get_rect()
    for nlo in nlos.sprites():
        if nlo.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, gun, nlos, bullets)
            break