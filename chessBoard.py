import pygame as pg
pg.init()

W, N = [int(i) for i in input().split()]
if W % N != 0:
    pg.quit()
    raise ValueError("W is not dividable by N")

disp = pg.display.set_mode((W, W))

black = False
for i in range(N):
    black = not black
    for j in range(N):
        if not black:
            rect = pg.rect.Rect(j * (W // N), i * (W // N), W // N, W // N)
            pg.draw.rect(disp, "white", rect)
        black = not black


pg.display.flip()
run = True
while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False

pg.quit()