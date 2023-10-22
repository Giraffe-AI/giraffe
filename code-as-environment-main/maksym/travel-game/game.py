import pygame
import sys

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define the player, goal, and obstacle attributes
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]

goal_size = 50
goal_pos = [WIDTH - goal_size, HEIGHT - goal_size - 100]

obstacle_width = 200
obstacle_height = 50
obstacle_pos = [WIDTH // 2 - obstacle_width // 2, HEIGHT // 2 - obstacle_height // 2]

font = pygame.font.SysFont('Arial', 30)

def check_collision(player_pos, block_pos, block_size):
    px, py = player_pos
    bx, by = block_pos
    size = block_size
    return px < bx + size and px + player_size > bx and py < by + size and py + player_size > by

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    
    player_pos[0] += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5
    player_pos[1] += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 5

    # Check collisions
    if check_collision(player_pos, goal_pos, goal_size):
        print("You win!")
        pygame.quit()
        sys.exit()

    if check_collision(player_pos, obstacle_pos, obstacle_width):
        print("Collision!")
        player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(screen, GREEN, (goal_pos[0], goal_pos[1], goal_size, goal_size))
    pygame.draw.rect(screen, RED, (obstacle_pos[0], obstacle_pos[1], obstacle_width, obstacle_height))
    
    pygame.display.flip()
    pygame.time.Clock().tick(30)
