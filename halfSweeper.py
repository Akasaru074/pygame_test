from random import random
import pygame as pg
pg.init()
SIZE = WIDTH, HEIGHT = 700, 700
disp = pg.display.set_mode(SIZE)

N = 10
OFFSET = 100

assert WIDTH % N == 0

ACTUAL_WIDTH = WIDTH - OFFSET

grid = []
for i in range(N):
    for j in range(N):
        rect_color = "red" if random() <= 0.1 else "white"
        rect = pg.rect.Rect(OFFSET // 2 + j * (ACTUAL_WIDTH // N), OFFSET // 2 + i * (ACTUAL_WIDTH // N), (ACTUAL_WIDTH // N), (ACTUAL_WIDTH // N))
        if rect_color == "red":
            pg.draw.rect(disp, rect_color, rect)
            grid.append((i, j))
        pg.draw.rect(disp, rect_color, rect, 1)

pg.display.flip()

run = True
while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
        if e.type == pg.MOUSEBUTTONDOWN:
            if e.pos[1] < OFFSET // 2 or e.pos[0] < OFFSET // 2:
                continue
            elif WIDTH - e.pos[1] < OFFSET // 2 or WIDTH - e.pos[0] < OFFSET // 2:
                continue

            i = (e.pos[1] - OFFSET // 2) // (ACTUAL_WIDTH // N)
            j = (e.pos[0] - OFFSET // 2) // (ACTUAL_WIDTH // N)
            if (i, j) in grid:
                print("BOMB!")
            else:
                s = 0
                for a in [-1, 0, 1]:
                    for b in [-1, 0, 1]:
                        if (i + a, j + b) in grid:
                            s += 1
                print(s)

pg.quit()