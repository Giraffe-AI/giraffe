import pygame
import random
import time

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GARBAGE_TRUCK_COLOR = (128, 128, 128)
GARBAGE_COLOR = (135, 84, 0) # Brown


# Garbage Truck
class GarbageTruck(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(GARBAGE_TRUCK_COLOR)
        self.rect = self.image.get_rect()
        self.speed = 1

    def update(self, keys, screenWidth, screenHeight):
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < screenHeight - 50:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < screenWidth - 50:
            self.rect.x += self.speed


# Garbage
class Garbage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([25, 25])
        self.image.fill(GARBAGE_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_width - 25)
        self.rect.y = random.randrange(screen_height - 25)

# Initialize Pygame
pygame.init()
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Garbage Collection Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

garbage_truck = GarbageTruck()
all_sprites.add(garbage_truck)

for i in range(10):  # Generates 10 pieces of garbage
    garbage = Garbage()
    all_sprites.add(garbage)

# Main Game Loop
running = True
start_time = pygame.time.get_ticks()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    garbage_truck.update(keys, screen_width, screen_height)

    # If truck collides with garbage, it disappears (gets collected).
    hit_list = pygame.sprite.spritecollide(garbage_truck, all_sprites, True)

    if len(hit_list) == 1:  # only the truck is left
        print("All garbage collected.")
        running = False

    # If the time limit is exceeded, the game ends.
    if pygame.time.get_ticks() - start_time > 60000:  # 1 min
        print("Time out!")
        running = False

    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()