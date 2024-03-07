"""
Activity 5: Modify the program from the previous activity so that the square can move left, right, up, and down using
the arrow keys on the keyboard.
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
pygame.display.set_caption("5.Controlar_el_movimiento_del_cuadrado_con_teclas")

## colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

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
    if keys_pressed[pygame.K_RIGHT]:
        square.x += SPEED
    if keys_pressed[pygame.K_LEFT]:
        square.x -= SPEED
    if keys_pressed[pygame.K_UP]:
        square.y -= SPEED
    if keys_pressed[pygame.K_DOWN]:
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