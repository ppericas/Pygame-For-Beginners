"""
Activity 10: Display the text "Name" in the center of the screen. Allow this text to be modified and show these changes
in real-time. In other words, allow for the addition or deletion of characters to be visible as they occur.
"""
#----------------------------------------------------------------------------------------------------------------------
# imports
import pygame
from pygame.locals import *

pygame.init()

#----------------------------------------------------------------------------------------------------------------------
# constants
## window
pygame.display.set_caption('10.Modificar_texto')
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

## colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

## text
font = pygame.font.SysFont('Arial', 48)
text = "Nombre"
text_surface = font.render(text, True, BLACK)
text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//2))

## others
FPS = 60

#----------------------------------------------------------------------------------------------------------------------
# class & functions
def draw_window():
    WIN.fill(WHITE)
    WIN.blit(text_surface, text_rect)
    pygame.display.update()

#----------------------------------------------------------------------------------------------------------------------
# main function
def main():
    global text_surface
    clock = pygame.time.Clock()
    text = "Nombre"
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                
                if event.key == K_BACKSPACE:
                    text = text[:-1]
                elif event.key == K_SPACE:
                    text += " "
                elif event.key == K_a:
                    text += "a"
                elif event.key == pygame.K_b:
                    text += "b"
                elif event.key == pygame.K_c:
                    text += "c"
                elif event.key == pygame.K_d:
                    text += "d"
                elif event.key == pygame.K_e:
                    text += "e"
                elif event.key == pygame.K_f:
                    text += "f"
                elif event.key == pygame.K_g:
                    text += "g"
                elif event.key == pygame.K_h:
                    text += "h"
                elif event.key == pygame.K_i:
                    text += "i"
                elif event.key == pygame.K_j:
                    text += "j"
                elif event.key == pygame.K_k:
                    text += "k"
                elif event.key == pygame.K_l:
                    text += "l"
                elif event.key == pygame.K_m:
                    text += "m"
                elif event.key == pygame.K_n:
                    text += "n"
                elif event.key == pygame.K_o:
                    text += "o"
                elif event.key == pygame.K_p:
                    text += "p"
                elif event.key == pygame.K_q:
                    text += "q"
                elif event.key == pygame.K_r:
                    text += "r"
                elif event.key == pygame.K_s:
                    text += "s"
                elif event.key == pygame.K_t:
                    text += "t"
                elif event.key == pygame.K_u:
                    text += "u"
                elif event.key == pygame.K_v:
                    text += "v"
                elif event.key == pygame.K_w:
                    text += "w"
                elif event.key == pygame.K_x:
                    text += "x"
                elif event.key == pygame.K_y:
                    text += "y"
                elif event.key == pygame.K_z:
                    text += "z"
                
                text_surface = font.render(text, True, BLACK)
        
        draw_window()
    
    pygame.quit()

if __name__ == "__main__":
    main()