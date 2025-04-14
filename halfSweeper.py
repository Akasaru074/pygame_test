import pygame as pg
pg.init()
SIZE = WIDTH, HEIGHT = 720, 480
disp = pg.display.set_mode(SIZE)


run = True
while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False

pg.quit()