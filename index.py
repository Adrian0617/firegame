import pygame
import random
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SHIP_WIDTH = 50
SHIP_HEIGHT = 50
INVADER_WIDTH = 50
INVADER_HEIGHT = 50

SHIP_SPEED = 5
INVADER_SPEED = 2

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([SHIP_WIDTH, SHIP_HEIGHT])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT - SHIP_HEIGHT - 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= SHIP_SPEED
        if keys[pygame.K_RIGHT] and self.rect.x < SCREEN_WIDTH - SHIP_WIDTH:
            self.rect.x += SHIP_SPEED

class Invader(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([INVADER_WIDTH, INVADER_HEIGHT])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - INVADER_WIDTH)
        self.rect.y = random.randint(-300, -INVADER_HEIGHT)

    def update(self):
        self.rect.y += INVADER_SPEED
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = random.randint(-300, -INVADER_HEIGHT)
            self.rect.x = random.randint(0, SCREEN_WIDTH - INVADER_WIDTH)

def draw_text(screen, text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Invaders")

    player = Ship()
    invaders = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    for _ in range(10):
        invader = Invader()
        invaders.add(invader)
        all_sprites.add(invader)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()

        hits = pygame.sprite.spritecollide(player, invaders, True)
        if hits:
            draw_text(screen, "GAME OVER", 64, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False

        screen.fill(BLACK)
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

