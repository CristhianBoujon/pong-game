import pygame
from pygame.time import wait

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


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    rect = pygame.Rect(RECT_X, RECT_Y, RECT_WIDTH, RECT_HEIGHT)

    while True:
        screen.fill(SCREEN_BACKGROUND)
        pygame.draw.rect(screen, RECT_COLOR, rect)
        rect.right += RECT_STEP
        pygame.display.flip()
        wait(TIME)

if __name__ == '__main__':
    main()
