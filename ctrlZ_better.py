import pygame as pg
pg.init()
size = W, H = 720, 480
disp = pg.display.set_mode(size)

run = True
drawing = False
ctrl_pressed = False
start_x, start_y, w, h = 0, 0, 0, 0
drawing_surf = pg.Surface(size, pg.SRCALPHA)
drawing_surf.fill((0,0,0,0))
history = [drawing_surf.copy()]

while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
        if e.type == pg.MOUSEBUTTONDOWN:
            drawing = True
            start_x, start_y = e.pos
        if e.type == pg.MOUSEBUTTONUP and drawing:
            drawing = False
            rect_surf = pg.Surface(size, pg.SRCALPHA)
            rect_surf.fill((0,0,0,0))
            rect = pg.rect.Rect(start_x + (w if w < 0 else 0), start_y + (h if h < 0 else 0), abs(w), abs(h))
            pg.draw.rect(rect_surf, "#2bb3fc", rect, 5)
            drawing_surf.blit(rect_surf, (0,0))
            history.append(drawing_surf.copy())
            start_x = start_y = w = h = 0
        if drawing and e.type == pg.MOUSEMOTION:
            w, h = e.pos[0] - start_x, e.pos[1] - start_y
        if e.type == pg.KEYDOWN and e.key == pg.K_LCTRL:
            ctrl_pressed = True
        if e.type == pg.KEYUP and e.key == pg.K_LCTRL:
            ctrl_pressed = False
        if e.type == pg.KEYDOWN and ctrl_pressed and e.key == pg.K_z and len(history) > 1:
            history.pop()
            drawing_surf = history[-1].copy()

        disp.fill("black")
        disp.blit(drawing_surf, (0, 0))

    if drawing:
        rect = pg.rect.Rect(start_x + (w if w < 0 else 0), start_y + (h if h < 0 else 0), abs(w), abs(h))
        pg.draw.rect(disp, "#2bb3fc", rect, 5)
    pg.display.flip()


pg.quit()
