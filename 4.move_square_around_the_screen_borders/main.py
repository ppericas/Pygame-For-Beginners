"""
Activity 4: Modify the program from the previous activity so that the square moves around the four borders of the
window continuously.
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
pygame.display.set_caption("4.Mover_cuadrado_por_los_bordes_de_la_pantalla")

## colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

## sizes
SQUARE_SIZE = 100
SQUARE_X = 0
SQUARE_Y = 0

## others
FPS = 60
SPEED = 240

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
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_index = 0
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        direction_x, direction_y = directions[direction_index]
        square.x += SPEED / FPS * direction_x
        square.y += SPEED / FPS * direction_y

        if square.right >= WIDTH or square.bottom >= HEIGHT or square.left <= 0 or square.top <= 0:
            direction_index = (direction_index + 1) % 4
        draw_window(square)

    pygame.quit()


if __name__ == "__main__":
    main()