"""
Activity 6: Modify the program from the previous activity so that the square, when colliding with the edge of the
window, cannot continue moving in that direction.
"""
#----------------------------------------------------------------------------------------------------------------------
# imports
import pygame

pygame.init()

#----------------------------------------------------------------------------------------------------------------------
# constants
## sizes
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("6.Respetar_bordes_de_pantalla.py")

## colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

## sizes
SQUARE_SIZE = 100
SQUARE_X = (WIDTH - SQUARE_SIZE) // 2
SQUARE_Y = (HEIGHT - SQUARE_SIZE) // 2

## others
FPS = 60
SPEED = 5

#----------------------------------------------------------------------------------------------------------------------
# classes & functions
def draw_window(square):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, square)
    pygame.display.update()

def move_square(keys_pressed, square):
    if keys_pressed[pygame.K_RIGHT] and square.right <= WIDTH:
        square.x += SPEED
    if keys_pressed[pygame.K_LEFT] and square.left >= 0:
        square.x -= SPEED
    if keys_pressed[pygame.K_UP] and square.top >= 0:
        square.y -= SPEED
    if keys_pressed[pygame.K_DOWN] and square.bottom <= HEIGHT:
        square.y += SPEED

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

        keys_pressed = pygame.key.get_pressed()
        move_square(keys_pressed, square)
        draw_window(square)

    pygame.quit()


if __name__ == "__main__":
    main()