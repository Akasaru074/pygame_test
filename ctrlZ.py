import pygame as pg
pg.init()
size = W, H = 720, 480
disp = pg.display.set_mode(size)

run = True
drawing = False
start_x, start_y, w, h = 0, 0, 0, 0
surf = pg.surface.Surface(size)
surfs = []
rect = pg.rect.Rect(0,0,0,0)

def rerender():
    disp.fill("black")
    for surf in surfs:
        disp.blit(surf, (0, 0))
        pg.display.flip()
        print(f"rerendered {len(surfs)} figs")
    pg.display.flip()


while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
        if e.type == pg.MOUSEBUTTONDOWN:
            drawing = True
            start_x, start_y = e.pos
        if e.type == pg.MOUSEBUTTONUP:
            drawing = False
            surfs.append(surf.copy())
            print(surfs)
            start_x = start_y = w = h = 0
        if drawing and e.type == pg.MOUSEMOTION:
            w, h = e.pos[0] - start_x, e.pos[1] - start_y
            # rect = pg.rect.Rect(start_x, start_y, e.pos[0] - start_x, e.pos[1] - start_y)
            # pg.draw.rect(surf, "#2bb3fc", rect)
            # disp.blit(surf, (0, 0))
            # pg.display.flip()
        if e.type == pg.KEYUP and e.key == pg.K_z and len(surfs) > 0:
            surfs.pop()
            surf.fill("black")
            print(surfs)
            rerender()
    if drawing:
        rect = pg.rect.Rect(start_x, start_y, w, h)
        pg.draw.rect(surf, "#2bb3fc", rect)
        disp.blit(surf, (0, 0))
        pg.display.flip()


pg.quit()
