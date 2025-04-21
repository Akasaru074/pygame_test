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
click_grid = []
font = pg.font.Font(pg.font.get_default_font(), 24)
text = font.render("", 1, "#FFFFFF")
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
            if (i, j) not in grid and (i, j) not in click_grid:
                s = 0
                for a in [-1, 0, 1]:
                    for b in [-1, 0, 1]:
                        if (i + a, j + b) in grid:
                            s += 1
                text.fill("black")
                text = font.render(f"{s}", 1, "#FFFFFF")
                textRect = text.get_rect()
                x = OFFSET // 2 + (ACTUAL_WIDTH // N) * j + (ACTUAL_WIDTH // N // 2)
                y = OFFSET // 2 + (ACTUAL_WIDTH // N) * i + (ACTUAL_WIDTH // N // 2)
                textRect.center = (x, y)
                disp.blit(text, textRect)
                pg.display.flip()
                click_grid.append((i, j))
                # print(s)

pg.quit()