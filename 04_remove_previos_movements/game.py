import pygame
from pygame.time import wait


def main():
    pygame.init()
    screen = pygame.display.set_mode((320, 240))
    rect = pygame.Rect(0, 0, 10, 10)

    while True:
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), rect)
        rect.right += 20
        pygame.display.flip()
        wait(1000)

if __name__ == '__main__':
    main()
