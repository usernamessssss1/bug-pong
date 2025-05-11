from pygame import *


back =(200,255,255)
window = display.set_mode((600,500))
window.fill(back)
clock = time.Clock()
FPS = 60

game = True

finish = False



while game:
    for i in event.get():
        if i.type == QUIT:

            game = False

    display.update()
    clock.tick(FPS)