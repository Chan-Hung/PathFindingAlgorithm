import pygame
from settings import *
from node import Node

class gui:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(TITLE)
        self.font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.algorithm = None
        self.previous_result = []

    def make_grid(self):
        #Make an N x N matrix with each index implemented as a Node
        grid = []
        # 0 -> 41
        for i in range(ROWS):
            grid.append([])
            for j in range (COLS):
                grid[i].append(Node(i,j))
        return grid

    def draw_grid(self):
        for i in range(ROWS + 1):
            pygame.draw.line(self.win, DARK_GREY, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, WIDTH))
            pygame.draw.line(self.win, DARK_GREY, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE))
    
    def buttons(self):

        #A star Algorithm

