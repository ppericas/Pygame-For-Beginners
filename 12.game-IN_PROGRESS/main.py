#IN PROGRESS
"""
Activity 12: Create a -Player- object that is controlled with the arrow keys. Create other objects that will be on the
screen randomly. Implement logic so that when the Player object touches any other object on the screen, the game ends.
"""
#----------------------------------------------------------------------------------------------------------------------
# imports
import pygame
from random import randint
import os

pygame.init()

#----------------------------------------------------------------------------------------------------------------------
# constants
## window
WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('11.Shooter')

## colors
WHITE = (255, 255, 255)
GREY = (128, 128, 128)

ENEMY_SIZE = 50
PLAYER_SIZE = 100

## assets
PLAYER_IMAGE = pygame.image.load(
    os.path.join('assets', 'player.png'))
PLAYER = pygame.transform.scale(PLAYER_IMAGE, (PLAYER_SIZE, PLAYER_SIZE))

HYENA_IMAGE = pygame.image.load(
    os.path.join('assets','enemies', 'Hyena.png'))
HYENA = pygame.transform.scale(HYENA_IMAGE, (ENEMY_SIZE, ENEMY_SIZE))

SCORPIO_IMAGE = pygame.image.load(
    os.path.join('assets','enemies', 'Scorpio.png'))
SCORPIO = pygame.transform.scale(SCORPIO_IMAGE, (ENEMY_SIZE, ENEMY_SIZE))

SNAKE_IMAGE = pygame.image.load(
    os.path.join('assets','enemies', 'Snake.png'))
SNAKE = pygame.transform.scale(SNAKE_IMAGE, (ENEMY_SIZE, ENEMY_SIZE))

VULTURE_IMAGE = pygame.image.load(
    os.path.join('assets','enemies', 'Vulture.png'))
VULTURE = pygame.transform.scale(VULTURE_IMAGE, (ENEMY_SIZE, ENEMY_SIZE))

## others
FPS = 60

#----------------------------------------------------------------------------------------------------------------------
# class & functions
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 5

    def draw(self):
        WIN.blit(PLAYER, (self.x, self.y))

def draw_window(player):
    WIN.fill(WHITE)
    player.draw()
    pygame.display.update()

def random_coordinate():
    return randint(WIDTH - ENEMY_SIZE, HEIGHT - ENEMY_SIZE)

#----------------------------------------------------------------------------------------------------------------------
# main function
def main():
    clock = pygame.time.Clock()
    run = True
    player = Player(WIDTH//2 - PLAYER_SIZE//2, HEIGHT//2 - PLAYER_SIZE//2)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pass

        draw_window(player)

    pygame.quit()


if __name__ == "__main__":
    main()