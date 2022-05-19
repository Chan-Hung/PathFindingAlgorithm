import pygame
from settings import *
from node import Node

class Gui:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(TITLE)
        self.font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.algorithm = None
        self.previous_results = []

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
            
    def get_mouse_position(self, pos):
        row = pos[0] // SQUARE_SIZE
        col = pos[1] // SQUARE_SIZE
        return row, col

    def buttons(self):
        #pygame.draw.rect(surface, color, (x, y, width, height))
        
        #Vị trí của button nãy có tọa độ:
        #x = cách left window 1 khoảng = SQUARE_SIZE
        #y = cách top window 1 khoảng = SQUARE_SIZE * 41 + 10, vì grid là ma trận 41 x 41 nên tọa độ y phải ở dưới grid, và cũng đồng thời cách grid 1 khoảng 10
        #width = chiều dài = SQUARE_SIZE * 8 (width có độ rộng = 8 cubes)
        #height = chiều rộng (cao) = SQUARE_SIZE * 2 (height có độ rộng = 2 cubes)
        
        #A star Algorithm buttons

        #Đầu tiên, vẽ button HCN với border thickness = 1
        pygame.draw.rect(self.win, BLACK, (SQUARE_SIZE, SQUARE_SIZE * 41 + 10, SQUARE_SIZE * 8, SQUARE_SIZE *2), 1)
        if self.algorithm == "a_star":    
            #Nếu thuật toán được chọn là A*, fill HCN đó = GREEN        
            pygame.draw.rect(self.win, GREEN, (SQUARE_SIZE + 1, SQUARE_SIZE * 41 + 11, SQUARE_SIZE * 8 - 2, SQUARE_SIZE * 2 - 2), 0)
        else: 
            #Nếu thuật toán được chọn khác A*, fill HCN đó bằng mã màu mặc định (GREY)
            pygame.draw.rect(self.win, GREY, (SQUARE_SIZE + 1, SQUARE_SIZE * 41 + 11, SQUARE_SIZE * 8 - 2, SQUARE_SIZE * 2 - 2), 0)

        # In pygame, text cannot be written directly to the screen. 
        # The first step is to create a Font object with a given font size. 
        # The second step is to render the text into an image with a given color.
        # The third step is to blit the image to the screen
        #Tham số True giúp cho font chữ trở nên mượt hơn
        text = self.font.render("A* Search", True, BLACK)
        #self.blit draw a source surface onto this surface
        #Màu của text sẽ đè lên
        self.win.blit(text, (SQUARE_SIZE * 2, SQUARE_SIZE * 42 + 2))



        #Breath First Search (Thuật toán BFS)

        #x = Cách left window 1 khoảng = SQUARE_SIZE * 10 (tọa độ x sẽ chỉ định button BFS nằm bên phải button A*, vốn đã chiếm width = 8, như vậy, độ dài 2 SQUARE_SIZE còn lại = khoảng cách button A* cách left window + khoảng cách button BFS cách button A*)
        #Các tham số y, width, height như button A* để tạo sự đồng nhất về kích thước
        pygame.draw.rect(self.win, BLACK, (SQUARE_SIZE * 10, SQUARE_SIZE * 41 + 10, SQUARE_SIZE * 8, SQUARE_SIZE * 2), 1)
        if self.algorithm == "bfs":    
            #Nếu thuật toán được chọn là bfs, fill HCN đó = GREEN        
            pygame.draw.rect(self.win, GREEN, (SQUARE_SIZE * 10 + 1, SQUARE_SIZE * 41 + 11, SQUARE_SIZE * 8 - 2, SQUARE_SIZE * 2 - 2), 0)
        else: 
            #Nếu thuật toán được chọn khác bfs, fill HCN đó bằng mã màu mặc định
            pygame.draw.rect(self.win, GREY, (SQUARE_SIZE * 10 + 1, SQUARE_SIZE * 41 + 11, SQUARE_SIZE * 8 - 2, SQUARE_SIZE * 2 - 2), 0)
        text = self.font.render("BFS", True, BLACK)
        self.win.blit(text, (SQUARE_SIZE * 12 + 12, SQUARE_SIZE * 42 + 2))


        #Depth First Search (Thuật toán DFS)
        #Tọa độ x lúc này = SQUARE_SIZE * 19 + 1
        pygame.draw.rect(self.win, BLACK, (SQUARE_SIZE * 19, SQUARE_SIZE * 41 + 10, SQUARE_SIZE * 8, SQUARE_SIZE * 2), 1)
        if self.algorithm == "dfs":    
            #Nếu thuật toán được chọn là dfs, fill HCN đó = GREEN        
            pygame.draw.rect(self.win, GREEN, (SQUARE_SIZE * 19 + 1, SQUARE_SIZE * 41 + 11, SQUARE_SIZE * 8 - 2, SQUARE_SIZE * 2 - 2), 0)
        else: 
            #Nếu thuật toán được chọn khác dfs, fill HCN đó bằng mã màu mặc định
            pygame.draw.rect(self.win, GREY, (SQUARE_SIZE * 19 + 1, SQUARE_SIZE * 41 + 11, SQUARE_SIZE * 8 - 2, SQUARE_SIZE * 2 - 2), 0)
        text = self.font.render("DFS", True, BLACK)
        self.win.blit(text, (SQUARE_SIZE * 21 + 12, SQUARE_SIZE * 42 + 2))

    #IN kết quả
    def results(self):
        if self.previous_results:
            for i in range(len(self.previous_results)):
                text = self.font.render(self.previous_results[i], True, BLACK)
                self.win.blit(text, (SQUARE_SIZE * 27 + 10, SQUARE_SIZE * (41 + i) + 10))

    #Tính chi phí
    def solution(self, start, end, path, draw):
        #Tổng chỉ phí
        cost = 0
        end.place_end()

        #Truy bết từ nút kết thúc -> nút bắt đầu và vẽ đường đi
        current = end

        #Khi nút đang xét vẫn trong đường đi
        while current in path:
            #Nút khác 2 nút đầu và cuối
            if current not in (start, end):
                #Chi phí + chi phí hiện tại
                cost += current.weight
            current = path[current]
            current.draw_path()
            draw()
            pygame.time.wait(30)

        start.place_start()
        return cost

    def draw(self, grid):
        #Fill background với màu xám
        self.win.fill(GREY)

        for row in grid: 
            for node in row:
                node.draw(self.win)
            
        #Vẽ lưới ma trận
        self.draw_grid()

        #Vẽ nút điều khiển
        self.buttons()

        #Vẽ kết quả (khung bên phải nút điều khiển)
        self.results()

        pygame.display.update()


