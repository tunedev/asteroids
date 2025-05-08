# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    y = SCREEN_HEIGHT / 2
    x = SCREEN_WIDTH / 2
    player = Player(x, y)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        time_passed = clock.tick(60)
        dt = time_passed / 1000
if __name__ == "__main__":
    main()
