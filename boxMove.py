import pygame as pg

pg.init()

size = width, height = 300, 300
disp = pg.display.set_mode(size)

rect = pg.rect.Rect(0, 0, 100, 100)
color = "#2bb3fc"
pg.draw.rect(disp, color, rect)

run = True
dragging = False
rel_m_pos = ()
while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
        elif e.type == pg.MOUSEBUTTONDOWN:
            rel_m_pos = pg.mouse.get_pos()
            if rect.left < rel_m_pos[0] < rect.right and rect.top < rel_m_pos[1] < rect.bottom:
                dragging = True
        elif e.type == pg.MOUSEBUTTONUP:
            dragging = False
        elif dragging and e.type == pg.MOUSEMOTION:
            disp.fill("black")
            mouse_pos = pg.mouse.get_pos()
            rect.x += mouse_pos[0] - rel_m_pos[0]
            rect.y += mouse_pos[1] - rel_m_pos[1]
            rel_m_pos = mouse_pos
            pg.draw.rect(disp, color, rect, 0)

    pg.display.flip()



pg.quit()