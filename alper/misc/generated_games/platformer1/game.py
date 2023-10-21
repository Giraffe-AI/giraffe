import pygame
import pymunk
import sys

# Game constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 60, 60
PLAYER_MASS = 1.0
PLAYER_FRICTION = 1.0
PLAYER_ELASTICITY = 0.5
JUMP_HEIGHT = 1000
PLAYER_COLOR = (0, 0, 255)
PLATFORM_HEIGHT = 20
PLATFORM_COLOR = (255, 0, 0)
BLOCK_SIZE = 30
BLOCK_MASS = 0.5
BLOCK_FRICTION = 0.5
BLOCK_ELASTICITY = 0.5
BLOCK_COLOR = (0, 255, 0)
FPS = 60
GRAVITY = 1000
PLATFORMS = [
    (0, SCREEN_HEIGHT - 40, SCREEN_WIDTH, PLATFORM_HEIGHT),  # Ground
    (SCREEN_WIDTH // 4, 3 * SCREEN_HEIGHT // 4, SCREEN_WIDTH // 2, PLATFORM_HEIGHT),
    (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH // 4, PLATFORM_HEIGHT),
]
BLOCKS = [
    (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50),
    (SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT // 2 - 50),
    (SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT // 2 - 50),
]

def draw_poly(screen, body, shape):
    vertices = [(body.position.x + v.x, body.position.y - v.y) for v in shape.get_vertices()]
    pygame.draw.polygon(screen, shape.color, vertices)

def create_player(space, x, y):
    points = [(-PLAYER_WIDTH // 2, -PLAYER_HEIGHT // 2), (-PLAYER_WIDTH // 2, PLAYER_HEIGHT // 2), 
              (PLAYER_WIDTH // 2, PLAYER_HEIGHT // 2), (PLAYER_WIDTH // 2, -PLAYER_HEIGHT // 2)]
    mass = PLAYER_MASS
    moment = pymunk.moment_for_poly(mass, points)
    body = pymunk.Body(mass, moment)
    body.position = x, y
    shape = pymunk.Poly(body, points)
    shape.friction = PLAYER_FRICTION
    shape.elasticity = PLAYER_ELASTICITY
    shape.color = PLAYER_COLOR
    space.add(body, shape)
    return body

def create_platform(space, x, y, w, h):
    points = [(-w // 2, -h // 2), (-w // 2, h // 2), (w // 2, h // 2), (w // 2, -h // 2)]
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = x, y
    shape = pymunk.Poly(body, points)
    shape.color = PLATFORM_COLOR
    space.add(body, shape)

def create_block(space, x, y):
    points = [(-BLOCK_SIZE // 2, -BLOCK_SIZE // 2), (-BLOCK_SIZE // 2, BLOCK_SIZE // 2), 
              (BLOCK_SIZE // 2, BLOCK_SIZE // 2), (BLOCK_SIZE // 2, -BLOCK_SIZE // 2)]
    mass = BLOCK_MASS
    moment = pymunk.moment_for_poly(mass, points)
    body = pymunk.Body(mass, moment)
    body.position = x, y
    shape = pymunk.Poly(body, points)
    shape.friction = BLOCK_FRICTION
    shape.elasticity = BLOCK_ELASTICITY
    shape.color = BLOCK_COLOR
    space.add(body, shape)

def player_on_ground(player, platforms):
    for platform in platforms:
        if abs(player.position.y - platform.body.position.y) <= PLAYER_HEIGHT // 2 + PLATFORM_HEIGHT // 2 + 1 and \
           platform.body.position.x - PLATFORM_WIDTH // 2 < player.position.x < platform.body.position.x + PLATFORM_WIDTH // 2:
            return True
    return False

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0, GRAVITY)

    player = create_player(space, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    platforms = []
    for x, y, w, h in PLATFORMS:
        platforms.append(create_platform(space, x + w // 2, y + h // 2, w, h))
    for x, y in BLOCKS:
        create_block(space, x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and player_on_ground(player, platforms):
                player.apply_impulse_at_local_point((0, -JUMP_HEIGHT))
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                player.apply_impulse_at_local_point((-JUMP_HEIGHT, 0))
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                player.apply_impulse_at_local_point((JUMP_HEIGHT, 0))

        space.step(1 / FPS)

        screen.fill((0, 0, 0))
        for body in space.bodies:
            for shape in body.shapes:
                draw_poly(screen, body, shape)
        pygame.display.flip()

        clock.tick(FPS)

if __name__ == "__main__":
    main()

