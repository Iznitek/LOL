import pygame
import random

running = True
Window = pygame.display.set_mode((800, 800))
size = 50
Orange = (249, 160, 0)
Black = (0, 0, 0)

def minecraft():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def squar_cursor(Window, side):
    color = minecraft()
    position = pygame.mouse.get_pos()
    x = position[0]
    y = position[1]

    pygame.draw.rect(Window, color, (x-15, y-15, side, side))
    pygame.display.update()

while running:

    squar_cursor(Window, size)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
