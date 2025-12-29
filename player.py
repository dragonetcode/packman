import pygame
from entity import Entity
from settings import YELLOW, TILE_SIZE

class Player(Entity):
    def __init__(self, x, y, walls):
        super().__init__(x, y, speed=2)
        self.walls = walls

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.next_direction = pygame.Vector2(-1, 0)
        if keys[pygame.K_RIGHT]: self.next_direction = pygame.Vector2(1, 0)
        if keys[pygame.K_UP]: self.next_direction = pygame.Vector2(0, -1)
        if keys[pygame.K_DOWN]: self.next_direction = pygame.Vector2(0, 1)

    def update(self):
        self.input()

        if self.at_center():
            if self.can_move(self.next_direction, self.walls):
                self.direction = self.next_direction
            if not self.can_move(self.direction, self.walls):
                self.direction = pygame.Vector2(0, 0)

        self.pixel_pos += self.direction * self.speed
        self.update_grid_pos()

    def draw(self, screen):
        pygame.draw.circle(screen, YELLOW,
            (int(self.pixel_pos.x + TILE_SIZE//2), int(self.pixel_pos.y + TILE_SIZE//2)),
            TILE_SIZE//2 - 2)