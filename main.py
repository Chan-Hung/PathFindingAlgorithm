import pygame
from gui import Gui


def start_main():
    win = Gui()
    grid = win.make_grid()
    start = None
    end = NotImplemented

    run = True
    while run:
        win.draw(grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
