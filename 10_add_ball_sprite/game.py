import os
import pygame
from pygame.time import wait
from random import randint

SCREEN_WIDTH = 360
SCREEN_HEIGHT = 240
SCREEN_BACKGROUND = (0, 0, 0)
RECT_WIDTH = 10
RECT_HEIGHT = 10
RECT_X = 0
RECT_Y = 0
RECT_COLOR = (255, 255, 255)
RECT_STEP = 20
TIME = 1000
CURRENT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR_PATH = os.path.join(CURRENT_DIR_PATH, 'assets')
IMAGES_DIR_PATH = os.path.join(ASSETS_DIR_PATH, 'images')


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
            return True


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ball_image_path = os.path.join(IMAGES_DIR_PATH, "ball.png")
    ball_img = pygame.image.load(ball_image_path).convert_alpha()
    ball_rect = ball_img.get_rect()

    move_x = RECT_STEP
    move_y = 0
    while True:
        screen.fill(SCREEN_BACKGROUND)
        screen.blit(ball_img, ball_rect)
        wall = draw_wall(100, 300, 0, True, RECT_COLOR, screen)

        if strike(ball_rect, wall):
            move_x = -RECT_STEP
            move_y = RECT_STEP

        ball_rect.move_ip(move_x, move_y)

        pygame.display.flip()
        wait(TIME)


if __name__ == '__main__':
    main()
