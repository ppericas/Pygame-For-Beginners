"""
Activity 8: Modify the program from the previous activity so that the square appears where we click instead of moving.
"""
#----------------------------------------------------------------------------------------------------------------------
#imports
import pygame

pygame.init()

#----------------------------------------------------------------------------------------------------------------------
# constants
## window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("7.Controlar_el_movimiento_del_cuadrado_con_el_ratón_1")

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
SPEED = 1

#----------------------------------------------------------------------------------------------------------------------
# classes & functions
def draw_window(square):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, square)
    pygame.display.update()

def move_square(x_click, y_click, square):
    target_x = x_click - SQUARE_SIZE // 2
    target_y = y_click - SQUARE_SIZE // 2
    square.x = target_x
    square.y = target_y

    square.x = max(0, min(square.x, WIDTH - SQUARE_SIZE))
    square.y = max(0, min(square.y, HEIGHT - SQUARE_SIZE))

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == True:
                    click_pos = pygame.mouse.get_pos()
                    x_click, y_click = click_pos
                    move_square(x_click, y_click, square)

        draw_window(square)

    pygame.quit()


if __name__ == "__main__":
    main()