import pygame
import random

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (155, 155, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def reset(self):
        self.color = WHITE

    def set_color(self, c):
        self.color = c

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_naighbour(self, grid):
        self.neighbors = []

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)

    return grid

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
    for i in range(rows):
        pygame.draw.line(win, GREY, (i * gap, 0), (i * gap, width))

def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(win)
    draw_grid(win, rows, width)

    pygame.display.update()

def gen_rend_color():
    return [random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)]

def gen_art(win, grid):
    color = gen_rend_color()
    # color = [255, 0,0]
    for row in grid:
        for spot in row:
            for i, _ in enumerate(color):
                if color[i] > 0:
                    color[i] -= 1
            # if color[0] > 0:
            #     color = [color[0] - 1, 0, 0]
            spot.set_color(tuple(color))



def main(win, width):
    ROWS = 50
    run = True
    grid = make_grid(ROWS, width)
    gen_art(win, grid)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    gen_art(win, grid)


        draw(win, grid, ROWS, width)
    
    pygame.quit()

main(WIN, WIDTH)
