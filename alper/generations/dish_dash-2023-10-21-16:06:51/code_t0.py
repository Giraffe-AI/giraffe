import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create the player
player = pygame.Rect(WIDTH // 2, HEIGHT // 2, 50, 50)

# Create groups for the dishes and soap suds
dishes = pygame.sprite.Group()
soap_suds = pygame.sprite.Group()

# Create a variable to control the game loop
running = True

# Game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a white background
    screen.fill(WHITE)

    # Draw the player
    pygame.draw.rect(screen, RED, player)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()