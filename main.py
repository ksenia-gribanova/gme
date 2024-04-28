from pygame import *
from random import randint

window = display.set_mode ((500,500))
background = transform.scale(image.load('phon.jpg'),(700,500))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 


class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w]:
            self.rect.y -= self.speed
        if key_pressed[K_s]:
            self.rect.y += self.speed


class Player2(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_i]:
            self.rect.y -= self.speed
        if key_pressed[K_k]:
            self.rect.y += self.speed


class Enemy(GameSprite):
    def update (self): 
        




player1 = Player('raketka.png',0, 150, 0.5)
player2 = Player2('raketka.png', 450, 100, 1)

game = True
while game:
    window.blit(background, (0, 0))
    player1.reset()
    player2.reset()
    player1.update()
    player2.update()

    for e in event.get():
        if e.type == QUIT:
            game = False
        
    display.update()

