from tkinter import filedialog
import tkinter as tk
from settings import ROWS, COLS
from node import Node

def open_map():
    
        start = None
        end = None
        
        # hidden Tkinter window
        root = tk.Tk()
        root.withdraw() 


        #get file name
        fileName = filedialog.askopenfilename()
        
        #open file
        f = open(fileName)
        
        #get data and convert it to matrix
        map_data= []
        map_data = [ line.split() for line in f]
        
        
        #Make an N x N matrix with each index implemented as a Node
        grid = []
        # 0 -> 41
        for i in range(ROWS):
            grid.append([])
            for j in range (COLS):
                grid[i].append(Node(i,j))
                if map_data[i][j] == '1':
                    grid[i][j].place_wall()
                elif map_data[i][j] == '2':
                    grid[i][j].place_start()
                    start = grid[i][j]
                elif map_data[i][j] == '3':
                    grid[i][j].place_end()
                    end = grid[i][j]
        
        f.close()
        
        return grid, start, end

def save_map(grid):
    
    # hidden Tkinter window
    root = tk.Tk()
    root.withdraw()
    
    #open save file dialog
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    
    
    for i in range(ROWS):
        for j in range (COLS):
            if grid[i][j].is_wall():
                f.write('1 ')
            elif grid[i][j].is_start():
                f.write('2 ')
            elif grid[i][j].is_end():
                f.write('3 ')
            else:
                f.write('0 ')
        f.write('\n')
    
    f.close()
    
