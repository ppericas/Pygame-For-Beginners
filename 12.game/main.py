"""
Activity 12: Create a -Player- object that is controlled with the arrow keys. Create other objects that will be on the
screen randomly. Implement logic so that when the Player object touches any other object on the screen, the game ends.
"""
#----------------------------------------------------------------------------------------------------------------------
# imports
import pygame, os, random
from random import randint

pygame.init()

#----------------------------------------------------------------------------------------------------------------------
# constants
## window
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('11.Shooter')

## sizes
AVERAGE_ENEMY_WIDTH, AVERAGE_ENEMY_HEIGHT = 30, 23
HYENA_WIDTH, HYENA_HEIGHT = 35, 28
SCORPIO_WIDTH, SCORPIO_HEIGHT = 32, 23
SNAKE_WIDTH, SNAKE_HEIGHT = 28, 15
VULTURE_WIDTH, VULTURE_HEIGHT = 27, 26
PLAYER_WIDTH, PLAYER_HEIGHT = 32, 184 # 184 = 46 * 4 ya que tengo una sola imagen con las diferentes orientaciones

## assets
BACKGROUND_IMAGE = pygame.image.load(
    os.path.join('assets', 'background.png'))
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))

PLAYER_IMAGE = pygame.image.load(
    os.path.join('assets', 'player.png'))
PLAYER = pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))

HYENA_IMAGE = pygame.image.load(
    os.path.join('assets','enemies', 'Hyena.png'))
HYENA = pygame.transform.scale(HYENA_IMAGE, (HYENA_WIDTH, HYENA_HEIGHT))

SCORPIO_IMAGE = pygame.image.load(
    os.path.join('assets','enemies', 'Scorpio.png'))
SCORPIO = pygame.transform.scale(SCORPIO_IMAGE, (SCORPIO_WIDTH, SCORPIO_HEIGHT))

SNAKE_IMAGE = pygame.image.load(
    os.path.join('assets','enemies', 'Snake.png'))
SNAKE = pygame.transform.scale(SNAKE_IMAGE, (SNAKE_WIDTH, SNAKE_HEIGHT))

VULTURE_IMAGE = pygame.image.load(
    os.path.join('assets','enemies', 'Vulture.png'))
VULTURE = pygame.transform.scale(VULTURE_IMAGE, (VULTURE_WIDTH, VULTURE_HEIGHT))

# orientation
PLAYER_FACING_NORTH = (0, 138, PLAYER_WIDTH, PLAYER_HEIGHT / 4)
PLAYER_FACING_SOUTH = (0, 0, PLAYER_WIDTH, PLAYER_HEIGHT / 4)
PLAYER_FACING_EAST = (0, 92, PLAYER_WIDTH, PLAYER_HEIGHT / 4)
PLAYER_FACING_WEAST = (0, 46, PLAYER_WIDTH, PLAYER_HEIGHT / 4)

## others
FPS = 60

#----------------------------------------------------------------------------------------------------------------------
# class & functions
def random_coordinate():
    return randint((100 - HYENA_WIDTH), WIDTH - 100 - HYENA_WIDTH), - HYENA_HEIGHT # le restamos las medidas maximas, que en este caso son las de la hiena

def get_random_seconds():
    return random.randint(500, 1000)

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = PLAYER
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.orientation = "North"
        self.velocity = 5

    def move(self, keys):
        if keys[pygame.K_UP]:
            self.orientation = "North"
            if self.y > 100:
                self.y -= self.velocity
        if keys[pygame.K_DOWN]:
            self.orientation = "South"
            if self.y < (HEIGHT - 100 - (self.height / 4)): # dividimos height entre 4 por que realmente el cuadrado de player es 184, que es la altura de toda la imagen real, pero realmente el personaje son 46 (184 /4)
                self.y += self.velocity
        if keys[pygame.K_RIGHT]:
            self.orientation = "East"
            if self.x < (WIDTH - 100 - self.width):  # restamos el ancho del jugador para evitar que se salga de la pantalla.
                self.x += self.velocity
        if keys[pygame.K_LEFT]:
            self.orientation = "West"
            if self.x > 100:
                self.x -= self.velocity
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
            if self.orientation == "North":
                player_rect = PLAYER_FACING_NORTH
            elif self.orientation == "South":
                player_rect = PLAYER_FACING_SOUTH
            elif self.orientation == "East":
                player_rect = PLAYER_FACING_EAST
            elif self.orientation == "West":
                player_rect = PLAYER_FACING_WEAST
            WIN.blit(PLAYER, (self.x, self.y), player_rect)

def draw_window(player):
    WIN.blit(BACKGROUND, (0, 0))
    player.draw()
    for enemy_image, enemy_rect in enemies:
        WIN.blit(enemy_image, enemy_rect)
    pygame.display.update()

def create_enemy():
    enemy_choice = randint(0, 3)
    if enemy_choice == 0:
        enemy_image = HYENA
    elif enemy_choice == 1:
        enemy_image = SCORPIO
    elif enemy_choice == 2:
        enemy_image = SNAKE
    else:
        enemy_image = VULTURE
    print("enemy spawned")
    enemy_rect = enemy_image.get_rect(topleft=random_coordinate())
    return enemy_image, enemy_rect

#----------------------------------------------------------------------------------------------------------------------
# main function
def main():
    global enemies
    player = Player(100, 100, PLAYER_WIDTH, PLAYER_HEIGHT)
    enemies = [create_enemy() for _ in range(3)]
    clock = pygame.time.Clock()
    seconds = get_random_seconds()
    pygame.time.set_timer(pygame.USEREVENT, seconds)
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.USEREVENT:
                enemies.append(create_enemy())

        keys = pygame.key.get_pressed()
        player.move(keys)

        for enemy_image, enemy_rect in enemies:
            if player.rect.colliderect(enemy_rect):
                print("¡Has perdido!")
                run = False

        for enemy_image, enemy_rect in enemies:
            enemy_rect.y += 1
        draw_window(player)

    pygame.quit()

if __name__ == "__main__":
    main()