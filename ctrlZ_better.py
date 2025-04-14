import pygame as pg

pg.init()
size = W, H = 720, 480
disp = pg.display.set_mode(size)
pg.display.set_caption("Rectangle Drawing App")

run = True
drawing = False
ctrl_pressed = False
start_x, start_y, w, h = 0, 0, 0, 0
# Create a base surface for our drawing history
drawing_surface = pg.Surface(size, pg.SRCALPHA)
drawing_surface.fill((0, 0, 0, 0))  # Transparent background
history = [drawing_surface.copy()]  # Start with one empty surface in history

while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False

        # Handle mouse button down - start drawing
        if e.type == pg.MOUSEBUTTONDOWN:
            drawing = True
            start_x, start_y = e.pos

        # Handle mouse button up - finish drawing
        if e.type == pg.MOUSEBUTTONUP and drawing:
            drawing = False
            # Create a new layer just for this rectangle
            rect_surface = pg.Surface(size, pg.SRCALPHA)
            rect_surface.fill((0, 0, 0, 0))  # Transparent
            rect = pg.Rect(
                start_x + (w if w < 0 else 0),
                start_y + (h if h < 0 else 0),
                abs(w), abs(h)
            )
            pg.draw.rect(rect_surface, "#2bb3fc", rect, 5)

            # Add the new rectangle to the drawing surface
            drawing_surface.blit(rect_surface, (0, 0))
            # Save to history
            history.append(drawing_surface.copy())

            # Reset rectangle parameters
            start_x = start_y = w = h = 0

        # Track mouse motion while drawing
        if drawing and e.type == pg.MOUSEMOTION:
            w, h = e.pos[0] - start_x, e.pos[1] - start_y

        # Handle Ctrl key
        if e.type == pg.KEYDOWN and e.key == pg.K_LCTRL:
            ctrl_pressed = True
        if e.type == pg.KEYUP and e.key == pg.K_LCTRL:
            ctrl_pressed = False

        # Handle Ctrl+Z for undo
        if e.type == pg.KEYDOWN and ctrl_pressed and e.key == pg.K_z:
            if len(history) > 1:  # Keep at least one empty state
                history.pop()  # Remove the latest state
                drawing_surface = history[-1].copy()  # Set current drawing to previous state

    # Draw everything
    disp.fill("black")
    disp.blit(drawing_surface, (0, 0))  # Draw all previous rectangles

    # Draw the rectangle being currently created
    if drawing:
        rect = pg.Rect(
            start_x + (w if w < 0 else 0),
            start_y + (h if h < 0 else 0),
            abs(w), abs(h)
        )
        pg.draw.rect(disp, "#2bb3fc", rect, 5)

    pg.display.flip()

pg.quit()