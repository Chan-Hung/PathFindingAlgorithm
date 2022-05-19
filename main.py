import pygame
from gui import Gui
from SearchAlgorithms import A_Star, BFS, DFS

def start_main():
    win = Gui()
    grid = win.make_grid()
    start = None
    end = None

    run = True
    while run:
        win.draw(grid)
        #Bắt sự kiện
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            #Click trong ma trận grid
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = win.get_mouse_position(pos)

                #Nếu tọa độ chuột được click trong lưới ma trận 41 x 41 (chưa ra ngoài biên đến các nút chức năng)
                if 0 <= row <= 40 and 0 <= col <= 40:
                    node = grid[row][col]

                    #Nếu không có nút start + user không được click vào nút end
                    if not start and node != end:
                        start = node
                        start.place_start()

                    #Nếu không có nút end + ngăn user không được click vào nút start 
                    elif not end and node != start:
                        end = node
                        end.place_end()
                    
                    #Nút bấm khác start node và end node => nút vật cản
                    elif node != start and node != end:
                        node.place_wall()
                #Select algorithms outside the grid
                elif 625 <= pos[1] <= 655:

                    #A* button
                    if 15 <= pos[0] <= 135:
                        win.algorithm = "a_star"
                    #BFS button
                    elif 150 <= pos[0] <= 270:
                        win.algorithm = "bfs"
                    #DFS button
                    elif 285 <= pos[0] <= 405:
                        win.algorithm = "dfs"

                #Reset trạng thái 
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = win.get_mouse_position(pos)
                if 0 <= row <= 41 and 0 <= col <= 41:
                    node = grid[row][col]
                    node.reset_color()
                    #Set start node = non (reset default color)
                    if node == start:
                        start = None
                    elif node == end:
                        end = None

            #Kích hoạt trò chơi
            if event.type == pygame.KEYDOWN:
                #Nếu node start và end đã được tạo, run thuật toán
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            if node != start and node != end and not node.is_wall():
                                node.reset_color()
                            node.add_neighbors(grid)
                    if win.algorithm:
                        if win.algorithm == "a_star":
                            A_Star.algorithm(start, end, grid, lambda: win.draw(grid), win)
                        elif win.algorithm == "bfs":
                            BFS.algorithm(start, end, lambda: win.draw(grid), win)
                        elif win.algorithm == "dfs":
                            DFS.algorithm(start, end, lambda: win.draw(grid), win)

                # Xóa màn hình vẫn giữ lại nút bắt đầu, kết thúc
                #Bấm nút d (delete)
                if event.key == pygame.K_d:
                    for row in grid:
                        for node in row:
                            if not node.is_wall() and not node.is_start() and not node.is_end():
                                node.reset_color()

                #Xóa toàn bộ màn hình
                #Bấm nút c (clear)
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    for row in grid:
                        for node in row:
                                node.reset_color()
    pygame.quit()

if __name__ == "__main__":
    start_main()
