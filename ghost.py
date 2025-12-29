import pygame
from settings import TILE_SIZE, RED

class Ghost:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        self.speed = 2
        self.direction = pygame.Vector2(1, 0)

    def update(self, walls):
        self.rect.x += self.direction.x * self.speed
        for wall in walls:
            if self.rect.colliderect(wall):
                self.direction.x *= -1
                self.rect.x += self.direction.x * self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)