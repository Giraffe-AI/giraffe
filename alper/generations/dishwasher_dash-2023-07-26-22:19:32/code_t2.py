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
        self.holding = None

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

        # Keep player on screen
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))

        # Pick up or put down dishes
        if keys[pygame.K_SPACE]:
            if self.holding:
                self.holding = None
            else:
                hit_dishes = [d for d in dishes if pygame.sprite.collide_rect(self, d)]
                if hit_dishes:
                    self.holding = hit_dishes[0]

        # Update position of held dish
        if self.holding:
            self.holding.rect.center = self.rect.center

# Dish class
class Dish(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = DISH_SPEED

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
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
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spawn dishes
    if random.random() < 0.01:
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