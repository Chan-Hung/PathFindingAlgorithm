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

    def add_neighbours(self, grid):
        self.neighbours = []

        #WIDTH // SQUARE_SIZE = total rows in grid
        # Up
        if self.row > 0:
            neighbour = grid[self.row - 1][self.col]
            if not neighbour.is_wall(): 
                self.neighbours.append(neighbour)
        
        # Right
        if self.col < WIDTH // SQUARE_SIZE - 1:
            neighbour = grid[self.row][self.col + 1]
            if not neighbour.is_wall():
                self.neighbours.append(neighbour)
            
        # Down
        if self.row < WIDTH // SQUARE_SIZE - 1:
            neighbour = grid[self.row + 1][self.col]
            if not neighbour.is_wall():
                self.neighbours.append(neighbour)

        # Left
        if self.col > 0:
            neighbour = grid[self.row][self.col - 1]
            if not neighbour.is_wall():
                self.neighbours.append(neighbour)

    #draw a cube in grid
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, SQUARE_SIZE, SQUARE_SIZE))

