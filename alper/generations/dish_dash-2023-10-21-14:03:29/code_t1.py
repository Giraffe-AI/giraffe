import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
DISH_SPEED = 5
PLAYER_SPEED = 5
SOAP_SUDS_SPEED = 3
FALLING_DISH_SPEED = 7

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the clock
clock = pygame.time.Clock()

# Set up the player
player = pygame.Rect(WIDTH // 2, HEIGHT - 50, 50, 50)

# Set up the dishes
dishes = [pygame.Rect(random.randint(0, WIDTH), 0, 30, 30) for _ in range(5)]

# Set up the soap suds
soap_suds = [pygame.Rect(random.randint(0, WIDTH), 0, 20, 20) for _ in range(3)]

# Set up the falling dishes
falling_dishes = [pygame.Rect(random.randint(0, WIDTH), 0, 30, 30) for _ in range(2)]

# Set up the score
score = 0

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player.x += PLAYER_SPEED

    # Dish movement
    for dish in dishes:
        dish.y += DISH_SPEED
        if dish.colliderect(player):
            score += 1
            dish.x = random.randint(0, WIDTH)
            dish.y = 0

    # Soap suds movement
    for sud in soap_suds:
        sud.y += SOAP_SUDS_SPEED
        if sud.colliderect(player):
            PLAYER_SPEED /= 2
            sud.x = random.randint(0, WIDTH)
            sud.y = 0

    # Falling dish movement
    for falling_dish in falling_dishes:
        falling_dish.y += FALLING_DISH_SPEED
        if falling_dish.colliderect(player):
            score -= 1
            falling_dish.x = random.randint(0, WIDTH)
            falling_dish.y = 0

    # Draw everything
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), player)
    for dish in dishes:
        pygame.draw.rect(screen, (0, 255, 0), dish)
    for sud in soap_suds:
        pygame.draw.rect(screen, (0, 0, 255), sud)
    for falling_dish in falling_dishes:
        pygame.draw.rect(screen, (255, 0, 0), falling_dish)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()