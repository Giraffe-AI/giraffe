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
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

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
    # Keep loop running at the right speed
    pygame.time.Clock().tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Check for collisions
    hits = pygame.sprite.spritecollide(player, dishes, False)
    for hit in hits:
        # Implement logic for picking up dish here
        pass

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # After drawing everything, flip the display
    pygame.display.flip()

pygame.quit()