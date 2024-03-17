"""
Activity 9: Display the text "Activity 09" in the center of the screen. Implement logic so that when the spacebar is
pressed, the text toggles between uppercase and lowercase, depending on its current display state. Additionally, if
the up and down arrow keys are pressed, the orientation of the text should also change.
"""
#----------------------------------------------------------------------------------------------------------------------
# imports
import pygame
from pygame.locals import *

pygame.init()

#----------------------------------------------------------------------------------------------------------------------
# constants
## window
pygame.display.set_caption('9.Mostrar_un_mensaje_de_texto_y_modificarlo')
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

## colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

## text
font = pygame.font.SysFont('Arial', 48)
text = "actividad 09"
text_surface = font.render(text, True, BLACK)
text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
angle = 0

## others
FPS = 60

#----------------------------------------------------------------------------------------------------------------------
# class & functions
def draw_window():
    WIN.fill(WHITE)
    rotated_text = pygame.transform.rotate(text_surface, angle)
    rotated_rect = rotated_text.get_rect(center=text_rect.center)
    WIN.blit(rotated_text, rotated_rect)
    pygame.display.update()
 
def change_caps(text):
    if text.islower():
        return text.upper()
    elif text.isupper():
        return text.lower()
    return text
def rotate(text):
    text = pygame.transform.rotate(text_rect, angle)
    return text

#----------------------------------------------------------------------------------------------------------------------
# main function
def main():
    global text_surface, angle
    clock = pygame.time.Clock()
    text = "actividad 09"
    run = True

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    text = change_caps(text)
                    text_surface = font.render(text, True, BLACK)
                    angle += 90
        
        draw_window()
    
    pygame.quit()

if __name__ == "__main__":
    main()