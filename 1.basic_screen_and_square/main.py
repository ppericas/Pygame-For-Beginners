"""
Activity 1: Create a Python program that draws a square on a window.
The square must have a side length of 100 pixels and should be centered in the window.
"""
#----------------------------------------------------------------------------------------------------------------------
# imports
import pygame

pygame.init()

#----------------------------------------------------------------------------------------------------------------------
# constants
## window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("1.Pantalla_básica_y_cuadrado")

## colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

## sizes
SQUARE_SIZE = 100
SQUARE_X = (WIDTH - SQUARE_SIZE) // 2
SQUARE_Y = (HEIGHT - SQUARE_SIZE) // 2

## others
FPS = 60

#----------------------------------------------------------------------------------------------------------------------
# classes & functions
def draw_window(square):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, square)
    pygame.display.update()

#----------------------------------------------------------------------------------------------------------------------
# main function
def main():
    square = pygame.Rect(SQUARE_X, SQUARE_Y, SQUARE_SIZE, SQUARE_SIZE)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        draw_window(square)

    pygame.quit()

if __name__ == "__main__":
    main()