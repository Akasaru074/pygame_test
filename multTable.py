import math

import pygame as pg
from math import sin, cos, radians
pg.init()
size = (width, height) = 480, 480
disp = pg.display.set_mode(size)
disp.fill("white")


center = width // 2

def do_mult(n, m):
    ang = 360 // n
    k = 0
    for i in range(0, 361, ang):
        start_x = int(cos(radians(i)) * 200) + center
        start_y = int(sin(radians(i)) * 200) + center
        end_x = int(cos(radians(i + () * m * ang)) * 200) + center
        end_y = int(sin(radians(i + () * m * ang)) * 200) + center

        pg.draw.circle(disp, "red", (start_x, start_y), 4)
        pg.draw.line(disp, "red", (start_x, start_y), (end_x, end_y))
        k += 1

run = True
while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
        do_mult(10, 2)

    pg.display.flip()

pg.quit()