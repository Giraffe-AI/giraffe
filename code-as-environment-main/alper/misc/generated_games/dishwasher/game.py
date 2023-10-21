#https://chat.openai.com/share/9f6c1a26-5ab7-479c-98d1-1a64a6fb827e

import pygame
import random
import time

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Game settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Dish settings
DISH_SPEED = 10
DISH_SIZE = 30
DISH_DROP_PENALTY = 1
DISH_CATCH_SCORE = 10
MAX_BROKEN_DISHES = 20
LEVEL_TIME = 120
DISH_CLEANING_TIME = 1

# Player settings
PLAYER_SIZE = 70

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - PLAYER_SIZE)
        self.score = 0
        self.broken_dishes = 0
        self.holding = None
        self.holding_since = 0

    def catch(self, dish):
        self.holding = dish
        self.holding_since = pygame.time.get_ticks()

    def release(self):
        if self.holding and pygame.time.get_ticks() - self.holding_since > DISH_CLEANING_TIME * 1000:
            self.holding = None
            self.score += DISH_CATCH_SCORE

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= DISH_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += DISH_SPEED

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        if self.holding:
            self.holding.rect.center = self.rect.center

class Dish(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((DISH_SIZE, DISH_SIZE))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - DISH_SIZE)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 4)

    def update(self):
        if self != player.holding:
            self.rect.y += self.speedy
            if self.rect.top > SCREEN_HEIGHT + 10:
                player.broken_dishes += 1
                player.score -= DISH_DROP_PENALTY
                self.kill()

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
dishes = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

for i in range(5):
    dish = Dish()
    all_sprites.add(dish)
    dishes.add(dish)

font = pygame.font.Font(None, 36)

start_ticks = pygame.time.get_ticks()  # starter tick

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player.holding:
                    player.release()
                elif not player.holding:
                    hits = pygame.sprite.spritecollide(player, dishes, False)
                    if hits:
                        player.catch(hits[0])

    all_sprites.update()

    if player.broken_dishes >= MAX_BROKEN_DISHES or player.score < 0:
        running = False

    # calculate how many seconds
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000

    if seconds > LEVEL_TIME:
        running = False

    screen.fill(BLACK)
    all_sprites.draw(screen)

    score_text = font.render("Score: " + str(player.score), True, WHITE)
    screen.blit(score_text, (20, 20))

    broken_text = font.render("Broken: " + str(player.broken_dishes), True, RED)
    screen.blit(broken_text, (20, 60))

    timer_text = font.render("Time: " + str(int(LEVEL_TIME - seconds)), True, WHITE)
    screen.blit(timer_text, (SCREEN_WIDTH - 150, 20))

    pygame.display.flip()

pygame.quit()

