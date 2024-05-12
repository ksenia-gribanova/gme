from pygame import *
from random import randint

clock = time.Clock()
window = display.set_mode ((500,500))
background = transform.scale(image.load('phon.jpg'),(700,500))

left = 0
right =0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_w, player_h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_w,player_h))
        self.speed = player_speed
        self.speedX = player_speed
        self.speedY = player_speed
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
        global left
        global right
        self.rect.x += self.speedX
        self.rect.y += self.speedY
        if sprite.collide_rect(self, player1):
            self.speedX *= -1
        if sprite.collide_rect(self, player2):
            self.speedX *= -1
        if self.rect.y >= 450 or self.rect.y <= 0:
            self.speedY *= -1
        if self.rect.x >= 500:
            left +=1
            self.rect.x = 250
        if self.rect.x <= 0:
            right +=1
            self.rect.x = 250
        
    
        



player1 = Player('raketka1.png',0, 150, 3, 50, 50)
player2 = Player2('raketka1.png', 450, 100, 3, 50, 50)
mach = Enemy('vach1.png',250,250, 2, 30, 30)


game = True
while game:
    window.blit(background, (0, 0))
    player1.reset()
    player2.reset()
    player1.update()
    player2.update()
    mach.reset()
    mach.update()
    font.init()
    font2 = font.Font (None, 70)
    scoreText = font2.render(str(left) + ':' + str(right), True, (255,215,0))
    window.blit(scoreText, (220, 0))


    for e in event.get():
        if e.type == QUIT:
            game = False
        
    display.update()
    clock.tick(60)



