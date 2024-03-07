"""
Activity 3: Modify the program from the previous activity so that the square moves from right to left without exiting
the screen."
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
pygame.display.set_caption("3.Mover_cuadrado_sin_parar_y_sin_salirse")

## colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

## sizes
SQUARE_SIZE = 100
SQUARE_X = (WIDTH - SQUARE_SIZE) // 2
SQUARE_Y = (HEIGHT - SQUARE_SIZE) // 2

## others
FPS = 60
SPEED = 60

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
    direction = 1
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        square.x += SPEED / FPS * direction

        if square.left <= 0:
            direction = 1

        elif square.right >= WIDTH:
            direction = -1

        draw_window(square)

    pygame.quit()


if __name__ == "__main__":
    main()