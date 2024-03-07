"""
Activity 11: Create a square (or drawing) that moves randomly around the screen. You can make it move continuously or
you can make it jump. Implement logic so that when you click on it with the mouse, it adds a point and displays it on
the screen. For the PRO version of this activity, you will have to program a maximum number of attempts and each time
you fail, subtract one attempt.
"""
#----------------------------------------------------------------------------------------------------------------------
# imports
import pygame
from random import randint

pygame.init()

#----------------------------------------------------------------------------------------------------------------------
# constants
## window
WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('11.Shooter')

## colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
LIGHT_GREY = (200, 200, 200)
RED = (255, 0, 0)

## sizes
square_size = 100

## text
font = pygame.font.SysFont(None, 48)
big_font = pygame.font.SysFont(None, 96)

score = 0
score_surface = font.render("SCORE: " + str(score), True, BLACK)
score_rect = score_surface.get_rect()

ammo = 5
ammo_surface = font.render("AMMO: " + str(ammo), True, BLACK)
ammo_rect = ammo_surface.get_rect()

play_surface = big_font.render("Play", True, LIGHT_GREY)
play_surface.set_alpha(0)
play_rect = play_surface.get_rect()

## others
FPS = 60

#----------------------------------------------------------------------------------------------------------------------
# classes & functions
def set_square_size():
    return randint(10, 100)

def set_square_backup(square):
    square.x = get_random_x()
    square.y = get_random_y()
    pygame.draw.rect(WIN, RED, square)
    pygame.display.update()

def set_square(square):
    square_size = set_square_size()
    square.x = get_random_x()
    square.y = get_random_y()
    square.width = square_size
    square.height = square_size
    if square.x + square.width > WIDTH:
        square.x = WIDTH - square.width
    if square.y + square.height > HEIGHT:
        square.y = HEIGHT - square.height
    pygame.draw.rect(WIN, RED, square)
    pygame.display.update()

def get_random_x():
    return randint(1, WIDTH - square_size)

def get_random_y():
    return randint(1, HEIGHT - square_size)

def get_random_time():
    return randint(1000, 5000)

def draw_window(square, mouse_x, mouse_y):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, RED, square)
    pygame.draw.line(WIN, GREY, (mouse_x, 0), (mouse_x, HEIGHT), 3) # x-axis of the scope
    pygame.draw.line(WIN, GREY, (0,mouse_y), (WIDTH, mouse_y), 3) # y-axis of the scope
    WIN.blit(score_surface, (10, 10))
    WIN.blit(play_surface, (((WIDTH // 2) - 100), ((HEIGHT // 2 - 50))))
    WIN.blit(ammo_surface, (750, 10))
    pygame.display.update()

def detect_collision(mouse_x, mouse_y, square):
    if square.collidepoint(mouse_x, mouse_y) == True:
        return True
    else:
        return False

class Timer: # Timer to make squares appear and disappear
    def __init__(self, duration):
        self.duration = duration
        self.start_time = pygame.time.get_ticks()
        self.is_finished = False

    def update(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.start_time
        if elapsed_time >= self.duration:
            self.is_finished = True

#----------------------------------------------------------------------------------------------------------------------
# main function
def main():
    global square_size, score_surface, ammo_surface, play_surface
    ammo = 5
    ammo_surface = font.render(f"AMMO: {ammo}", True, BLACK)
    score = 0
    score_surface = font.render(f"SCORE: {score}", True, BLACK)
    play_surface = big_font.render("Play Again", True, LIGHT_GREY)
    play_surface.set_alpha(0)
    square = pygame.Rect(get_random_x(),  get_random_y(), square_size, square_size)
    clock = pygame.time.Clock()
    state = "Waiting"
    timer = Timer(get_random_time())
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if ammo > 0:
                    play_surface.set_alpha(0)
                    if detect_collision(mouse_x, mouse_y, square) == True:
                        score += 1
                        score_surface = font.render(f"SCORE: {score}", True, BLACK)
                    else:
                        ammo -= 1
                        ammo_surface = font.render(f"AMMO: {ammo}", True, BLACK)
                else:
                    score = 0
                    ammo = 5
                    play_surface.set_alpha(255)
                    score_surface = font.render(f"SCORE: {score}", True, BLACK)

        if state == "Waiting":
            timer.update()
            if timer.is_finished:
                state = "Spawn"
                timer = Timer(get_random_time())

        elif state == "Spawn":
            set_square(square)
            state = "Waiting"

        mouse_pos = pygame.mouse.get_pos()
        mouse_x, mouse_y = mouse_pos
        detect_collision(mouse_x, mouse_y, square)
        draw_window(square, mouse_x, mouse_y)

    pygame.quit()


if __name__ == "__main__":
    main()