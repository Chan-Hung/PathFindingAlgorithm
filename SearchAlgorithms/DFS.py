import time
import pygame


def algorithm(start, end, draw, win):

    start_time = time.time()

    # Frontier is the stack of nodes that are currently being considered
    frontier = [start]

    # A set of all nodes that were visited
    visited = {start}

    # Keeps track of the paths by saving references to where each node came from
    path = {}

    current_node = start
    # While there is still a possible path
    while frontier:
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

           
        if current_node not in (start, end):
            current_node.draw_open()

        # At the start of every iteration, pop the top element from the stack
        current_node = frontier.pop()

        # If we found the end node, draw the path
        if current_node == end:
            time_taken = float(round(time.time() - start_time, 2))
            cost = win.solution(start, end, path, draw)
            win.previous_results = [
                "Kết quả thuật toán DFS", 
                "Thời gian " + str(time_taken) + "s",
                "Chi phí: " + str(cost), 
                "Nút đã duyệt: " + str(len(visited))]
            return True

        if current_node not in visited:
            visited.add(current_node)

        for neighbour in current_node.neighbours:
            # Make sure not to add duplicate nodes into the frontier and path
            if neighbour not in visited:
                path[neighbour] = current_node
                frontier.append(neighbour)
        
        # Close off the current node because we will not need to look at it again
        if current_node not in (start, end):
            current_node.draw_visited()
    
    return False
