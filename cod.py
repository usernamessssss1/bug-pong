from pygame import *
from random import *

back =(200,255,255)
window = display.set_mode((600,500))
window.fill(back)
clock = time.Clock()
FPS = 60

game = True

finish = False



class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        #- поменяй на +у скорости
        if keys[K_DOWN] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_UP] and self.rect.y < 450:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 450:
            self.rect.y += self.speed




game = True
Finish = False



speed_x = randint(1,2)
if speed_x ==1:
    speed_x = 3
else:
    speed_x = -3
    speed_y = -3
speed_x = 3
speed_y = 3
#перемещения мяча

#создаем спрайты
raсket1 = Player('синий амонг.png',30,200,5,50,500)#120=400
racket2 = Player('фиол амонг (1).png',525,200,5,50,50)#120=400
ball = GameSprite('мяч черный.png',200,250,3,50,50)#50=100

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        raсket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y<0 or ball.rect.y>450:
            speed_y *=-1.1
        if sprite.collide_rect(raсket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x *=-1

    ball.reset()
    racket2.reset()
    raсket1.reset()
    display.update()
    clock.tick(FPS)


