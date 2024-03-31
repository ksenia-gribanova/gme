rom pygame import *

window = display.set_mode((700,500))

background = transform.scale(image.load('stol.jpg'),(700,500))


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
        if key_pressed[K_a]:
            self.rect.x += self.speed
        if key_pressed[K_d]:
            self.rect.x -= self.speed

 player1 = Player('rocket.png',500, 432,4)
   
