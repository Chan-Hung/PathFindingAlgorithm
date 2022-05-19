import pygame
from settings import *

class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = row * SQUARE_SIZE
        self.y = col * SQUARE_SIZE
        self.color = GREY
        self.weight = 1
        self.neighbours = []

    def get_position(self):
        return self.row, self.col
    
    def is_wall(self):
        return self.color == BLACK
    
    def is_default(self):
        return self.color == GREY

    def is_path(self):
        return self.color == PURPLE
    
    def reset_color(self):
        self.color = GREY
    
    def reset_weight(self):
        self.weight = 1

    #First click
    def place_start(self):
        self.color = GREEN
    
    #Second click
    def place_end(self):
        self.color = RED

    #Barrier
    def place_wall(self):
        self.color = BLACK
    
    def place_weight(self):
        self.weight = 9


    def draw_open(self):
        self.color = BLUE
    
    def draw_visited(self):
        self.color = PINK
    
    def draw_path(self):
        self.color = PURPLE

    def add_neighbors(self, grid):
        self.neighbours = []

        #Ma trận có tọa độ grid = WIDTH x WIDTH

        #Move up
        #Cột đang xét phải là cột thứ 2 tính từ trên xuống
        #Và ở trên dòng đnag xét không phải là vật cản
        if self.row > 0 and not grid[self.row - 1][self.col].is_wall():
                self.neighbours.append(grid[self.row - 1][self.col])
        
        #Move left
        #Cột đang xét phải là cột thứ 2 tính từ biên trái
        #Và bên trái cột đang xét không phải là nút vật cản
        if self.col > 0 and not grid[self.row][self.col - 1].is_wall():
                self.neighbours.append(grid[self.row][self.col - 1])

        #Move Right
        #Cột đang xét phải là cột thứ 2 tính từ biên phải
        #và bên phải cột đang xét không là nút vật cản
        if self.col < WIDTH // SQUARE_SIZE - 1 and not grid[self.row][self.col + 1].is_wall():
            self.neighbours.append(grid[self.row][self.col + 1])

        #Move down
        #Cột đang xét phải là cột thứ 2 tính từ dưới lên
        #Và dòng bên dưới dòng đang xét không là vật cản
        if self.col < WIDTH // SQUARE_SIZE - 1 and not grid[self.row + 1][self.col].is_wall():
            self.neighbours.append(grid[self.row + 1][self.col])

        
    #draw a cube in grid
    #Vẽ từng khối (tượng trưng cho 1 node) trên lưới ma trận
    #Kích thước là 1 square: hình vuông có kích thước (SQUARE_SIZE * SQUARE_SIZE)
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, SQUARE_SIZE, SQUARE_SIZE))

