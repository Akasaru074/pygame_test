import pygame as pg
pg.init()
size = W, H = 720, 480
disp = pg.display.set_mode(size)

run = True
drawing = False
ctrl_pressed = False
start_x, start_y, w, h = 0, 0, 0, 0
surf = pg.surface.Surface(size)
surfs = []
rect = pg.rect.Rect(0,0,0,0)

while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
        if e.type == pg.MOUSEBUTTONDOWN:
            drawing = True
            start_x, start_y = e.pos
        if e.type == pg.MOUSEBUTTONUP:
            drawing = False
            surf.blit(disp, (0, 0))
            surfs.append(surf.copy())
            start_x = start_y = w = h = 0
        if drawing and e.type == pg.MOUSEMOTION:
            disp.fill("black")
            if len(surfs): disp.blit(surf, (0, 0))
            w, h = e.pos[0] - start_x, e.pos[1] - start_y
        if (e.type == pg.KEYDOWN or e.type == pg.KEYUP) and e.key == pg.K_LCTRL:
            ctrl_pressed = not ctrl_pressed
        if e.type == pg.KEYUP and ctrl_pressed and e.key == pg.K_z and len(surfs) > 0:
            surfs.pop()
            disp.fill("black")
            if len(surfs): disp.blit(surfs[-1], (0, 0))
            pg.display.flip()
    if drawing:
        rect = pg.rect.Rect(start_x + (w if w < 0 else 0), start_y + (h if h < 0 else 0), abs(w), abs(h))
        pg.draw.rect(disp, "#2bb3fc", rect, 5)
        pg.display.flip()


pg.quit()
