import pygame
from pygame.time import wait
from random import randint

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 240
SCREEN_BACKGROUND = (0, 0, 0)
RECT_WIDTH = 10
RECT_HEIGHT = 10
RECT_X = 0
RECT_Y = 0
RECT_COLOR = (255, 255, 255)
RECT_STEP = 20
TIME = 1000


def random_color():
    """
    Return a tuple of three random integers between 0 and 255
    representing RGB color.
    """
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


def draw_wall(amount, initial_x, initial_y, vertical, color, screen):
    x = initial_x
    y = initial_y
    rectagles = []
    for i in range(amount):
        rectangle = pygame.Rect(x, y, RECT_WIDTH, RECT_HEIGHT)
        pygame.draw.rect(screen, RECT_COLOR, rectangle)

        rectagles.append(rectangle)

        if vertical:
            y += RECT_HEIGHT
        else:
            x += RECT_WIDTH

    return rectagles


def strike(rect, wall):
    for brik in wall:
        if rect.colliderect(brik):
            print('BOOOOOOOOOOOOOOOM!')

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    rect = pygame.Rect(RECT_X, RECT_Y, RECT_WIDTH, RECT_HEIGHT)

    while True:
        color = random_color()
        screen.fill(SCREEN_BACKGROUND)
        pygame.draw.rect(screen, color, rect)
        wall = draw_wall(100, 300, 0, True, RECT_COLOR, screen)
        strike(rect, wall)

        rect.right += RECT_STEP

        pygame.display.flip()
        wait(TIME)


if __name__ == '__main__':
    main()
