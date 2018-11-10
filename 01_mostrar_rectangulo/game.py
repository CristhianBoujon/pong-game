import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((320, 240))
    rect = pygame.Rect(0, 0, 10, 10)
    pygame.draw.rect(screen, (255, 255, 255), rect)
    pygame.display.flip()


if __name__ == '__main__':
    main()
