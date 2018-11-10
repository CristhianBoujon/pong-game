import os
import pygame
from pygame.time import wait
from pygame.locals import *
from random import randint

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_BACKGROUND = (0, 0, 0)
RECT_WIDTH = 10
RECT_HEIGHT = 10
RECT_X = 0
RECT_Y = 0
RECT_COLOR = (255, 255, 255)
BALL_SPEED = 5
TIME = 60
CURRENT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR_PATH = os.path.join(CURRENT_DIR_PATH, 'assets')
IMAGES_DIR_PATH = os.path.join(ASSETS_DIR_PATH, 'images')
PADDLE_SPEED = 5


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


class Ball:
    def __init__(self, image_path, speed, x, y):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = speed

    def move(self, move_x, move_y):
        self.rect.move_ip(move_x, move_y)


class Paddle:
    def __init__(self, image_path, speed, x, y):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = speed

    def move(self, direction):
        if direction == 'up':
            self.rect.centery -= self.speed
        elif direction == 'down':
            self.rect.centery += self.speed


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    half_height = SCREEN_HEIGHT / 2
    half_width = SCREEN_WIDTH / 2

    ball_image_path = os.path.join(IMAGES_DIR_PATH, "ball.png")
    ball = Ball(ball_image_path, BALL_SPEED, half_width, half_height)

    paddle_image_path = os.path.join(IMAGES_DIR_PATH, "paddle.png")
    paddle_1 = Paddle(paddle_image_path, PADDLE_SPEED, 10, half_height)
    paddle_2 = Paddle(paddle_image_path, PADDLE_SPEED, SCREEN_WIDTH - 10, half_height)

    background_image_path = os.path.join(IMAGES_DIR_PATH, "background.jpg")
    background = pygame.image.load(background_image_path)

    move_x = BALL_SPEED
    move_y = BALL_SPEED
    clock = pygame.time.Clock()
    while True:

        keys = pygame.key.get_pressed()

        if keys[K_UP]:
            paddle_2.move('up')
        elif keys[K_DOWN]:
            paddle_2.move('down')

        if keys[K_w]:
            paddle_1.move('up')
        elif keys[K_s]:
            paddle_1.move('down')

        screen.blit(background, (0, 0))
        screen.blit(ball.image, ball.rect)
        screen.blit(paddle_1.image, paddle_1.rect)
        screen.blit(paddle_2.image, paddle_2.rect)

        if ball.rect.left < 0 or ball.rect.right > SCREEN_WIDTH:
            move_x = -move_x

        if ball.rect.top < 0 or ball.rect.bottom > SCREEN_HEIGHT:
            move_y = -move_y

        ball.move(move_x, move_y)

        pygame.display.flip()
        pygame.event.pump()
        clock.tick(TIME)


if __name__ == '__main__':
    main()
