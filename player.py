import pygame
from settings import TILE_SIZE, YELLOW

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        self.speed = 3
        self.direction = pygame.Vector2(0, 0)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = pygame.Vector2(-1, 0)
        elif keys[pygame.K_RIGHT]:
            self.direction = pygame.Vector2(1, 0)
        elif keys[pygame.K_UP]:
            self.direction = pygame.Vector2(0, -1)
        elif keys[pygame.K_DOWN]:
            self.direction = pygame.Vector2(0, 1)

    def move(self, walls):
        self.rect.x += self.direction.x * self.speed
        for wall in walls:
            if self.rect.colliderect(wall):
                self.rect.x -= self.direction.x * self.speed

        self.rect.y += self.direction.y * self.speed
        for wall in walls:
            if self.rect.colliderect(wall):
                self.rect.y -= self.direction.y * self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, YELLOW, self.rect.center, TILE_SIZE // 2)