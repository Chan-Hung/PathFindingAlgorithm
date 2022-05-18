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
        #pygame.draw.rect(surface, color, (x, y, width, height))
        #A star Algorithm buttons
        #Vị trí của button nãy có tọa độ:
        #x = cách left window 1 khoảng = SQUARE_SIZE
        #y = cách top window 1 khoảng = SQUARE_SIZE * 41 + 10, vì grid là ma trận 41 x 41 nên tọa độ y phải ở dưới grid, và cũng đồng thời cách grid 1 khoảng 10
        #width = chiều dài = SQUARE_SIZE * 8 (width có độ rộng = 8 cubes)
        #height = chiều rộng (cao) = SQUARE_SIZE * 2 (height có độ rộng = 2 cubes)
        #Đầu tiên, vẽ button HCN với border thickness = 1
        pygame.draw.rect(self.win, BLACK, (SQUARE_SIZE, SQUARE_SIZE * 41 + 10, SQUARE_SIZE * 8, SQUARE_SIZE *2), 1)
        if self.algorithm == "a_star":    
            #Nếu thuật toán được chọn là A*, fill HCN đó = GREEN        
            pygame.draw.rect(self.win, GREEN, (SQUARE_SIZE + 1, SQUARE_SIZE * 41 + 11, SQUARE_SIZE * 8 - 2, SQUARE_SIZE * 2 - 2), 0)
        else: 
            #Nếu thuật toán được chọn khác A*, fill HCN đó bằng mã màu khác
            pygame.draw.rect(self.win, GREY, (SQUARE_SIZE + 1, SQUARE_SIZE * 41 + 11, SQUARE_SIZE * 8 - 2, SQUARE_SIZE * 2 - 2), 0)
