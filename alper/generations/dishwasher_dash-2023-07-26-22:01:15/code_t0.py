import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up assets
player_img = pygame.image.load('player.png')
dish_img = pygame.image.load('dish.png')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.right > WIDTH:
            self.rect.left = 0

class Dish(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = dish_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(HEIGHT - self.rect.height)

    def update(self):
        self.rect.y += 1
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0

# Create sprite groups
all_sprites = pygame.sprite.Group()
dishes = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Create dishes
for i in range(10):
    dish = Dish()
    all_sprites.add(dish)
    dishes.add(dish)

# Game loop
running = True
while running:
    # Keep the loop running at the right speed
    pygame.time.Clock().tick(FPS)
    # Process input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Flip the display
    pygame.display.flip()

pygame.quit()