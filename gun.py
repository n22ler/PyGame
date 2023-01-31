import pygame as pg

class Gun():
    def __init__(self, screen):        
        self.screen = screen
        self.image = pg.image.load("assets/images/gun.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.mrt = False
        self.mlt = False
        self.center = float(self.rect.centerx)

    def output(self):
        self.screen.blit(self.image, self.rect)

    def update_position(self):
        if self.mrt and self.rect.right < self.screen_rect.right:
            self.center +=1.5
        elif self.mlt and self.rect.left > self.screen_rect.left:
            self.center -=1.5


        self.rect.centerx = self.center


    def create_gun(self):
        self.center = self.screen_rect.centerx