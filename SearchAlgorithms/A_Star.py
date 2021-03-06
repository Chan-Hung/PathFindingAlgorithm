import pygame
import time
from queue import PriorityQueue


def h(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)

def algorithm(start, end, grid, draw, win):
    start_time = time.time()

    #Vị trí: sử dụng trong trường hợp 2 nút đang xét có chung f
    position = 0

    #PriorityQueue sử dung để đẩy nút hiện đang xét tốt nhất (nút với f_score nhỏ nhất)
    #Biến frontier là hàng đợi các nút đang được xem xét
    frontier = PriorityQueue()
    frontier.put((0, position, start))
 
    #Theo dõi các đường đi bằng cách lưu vị trí nút nào đến từ đâu
    path = {}

    #Một set các node đã visited
    visited = {start}

    #g_score là khoảng cách (số lượng các nút) giữa nút hiện tại và nút bắt đầu
    #DÙng dictionary để ánh xạ 1 nút đến g_score tương ứng của nó ở các nút trên lưới
    g_score = {Node: float("inf") for row in grid for Node in row}
    g_score[start] = 0

    #f_score = g_score + h_score
    #h_score là hàm heuristic (khoảng cách Manhattan)
    f_score = {Node: float("inf") for row in grid for Node in row}
    f_score[start] = h(start.get_position(), end.get_position())

    #Khi vẫn còn đường để xét
    while not frontier.empty():
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
       #Trước mỗi lần lặp, pop nút có f_score thấp nhất ra khỏi hàng đợi
        current_node = frontier.get()[2]

        # If we found the solution, draw the path
        if current_node == end:
            #Tính thời gian chạy thuật toán, làm tròn 2 chữ số (đơn vị giây)
            time_taken = float(round(time.time() - start_time, 2))
            #Tính chi phí quãng đường
            cost = win.solution(start, end, path, draw)
            #Chứa kết quả vào mảng 
            win.previous_results = [
                "   Kết quả thuật toán A*", 
                "Thời gian: " + str(time_taken) + "s",
                "Chi phí: " + str(cost), 
                "Nút đã duyệt: " + str(len(visited))]
            return True

        # This will be the next g score for any neighbours with lower costs
        next_g_score = g_score[current_node] + current_node.weight

        for neighbour in current_node.neighbours:
            
            #Nếu ta thấy 1 nút lân cận có chi phí thấp hơn để đến nút đích
            #Ta update lại quãng đường đi và theo dõi nó
            if next_g_score < g_score[neighbour]:
                g_score[neighbour] = next_g_score

                #f = h + g 
                f_score[neighbour] = next_g_score + h(neighbour.get_position(), end.get_position())

                # Make sure not to add duplicate nodes into the frontier and path
                if neighbour not in visited:
                    path[neighbour] = current_node
                    visited.add(neighbour)
                    neighbour.draw_open()

                    # Increment position in queue
                    position += 1
                    frontier.put((f_score[neighbour], position, neighbour))

        #Tô màu nút đang xét để không xét lại
        if current_node not in (start, end):
            current_node.draw_visited()
        
    return False

