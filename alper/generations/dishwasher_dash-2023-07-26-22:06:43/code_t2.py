import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 60
DISH_FREQUENCY = 120  # Frequency of dish appearance (every 120 frames)

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up assets
PLAYER_SPEED = 5
DISH_SPEED = 2
DISH_SIZE = 20
SINK_POS = (WIDTH // 2, HEIGHT // 2)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed = PLAYER_SPEED

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

# Dish class
class Dish(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((DISH_SIZE, DISH_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - DISH_SIZE)
        self.rect.y = -DISH_SIZE
        self.speed = DISH_SPEED

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.kill()

# Create sprite groups
all_sprites = pygame.sprite.Group()
dishes = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Game loop
running = True
clock = pygame.time.Clock()
frame_count = 0
while running:
    # Keep loop running at the right speed
    clock.tick(FPS)
    frame_count += 1

    # Process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Create dishes periodically
    if frame_count % DISH_FREQUENCY == 0:
        dish = Dish()
        all_sprites.add(dish)
        dishes.add(dish)

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Flip the display
    pygame.display.flip()

pygame.quit()