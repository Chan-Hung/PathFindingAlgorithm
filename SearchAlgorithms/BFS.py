import pygame
import time

def algorithm(start, end, draw, win):
    #BFS sử dụng cấu trúc queue

    start_time = time.time()

    #Biến frontier là hàng đợi các nút đnag được xét
    frontier = [start]

    #Theo dõi đường đi
    path = {}

    #Tập hợp các nút đã visited
    visited = {start}

    #Khi frontier vẫn có đường đi khả this
    while frontier:
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

         # At the start of every iteration, pop the first element from the queue (dequeue)
         #Trước mỗi vòng lặp, lấy ra phần tử đầu tiên khỏi hàng đợi
        current_node= frontier.pop(0)

        # If we found the solution, draw the path
        if current_node == end:
            time_taken = float(round(time.time() - start_time, 2))
            cost = win.solution(start, end, path, draw)
            win.previous_results = [
                "   Kết quả thuật toán BFS", 
                "Thời gian: " + str(time_taken) + "s",
                "Chi phí: " + str(cost), 
                "Nút đã duyệt: " + str(len(visited))]
            return True

        for neighbour in current_node.neighbours:

            # Make sure not to add duplicate nodes into the frontier and path
            if neighbour not in visited:
                path[neighbour] = current_node
                visited.add(neighbour)
                frontier.append(neighbour)
                neighbour.draw_open()

        # Close off the current node because we will not need to look at it again
        if current_node not in (start, end):
            current_node.draw_visited()
        
    return False
