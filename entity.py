import pygame
from settings import TILE_SIZE

class Entity:
    def __init__(self, grid_x, grid_y, speed):
        self.grid_pos = pygame.Vector2(grid_x, grid_y)
        self.pixel_pos = self.grid_pos * TILE_SIZE
        self.direction = pygame.Vector2(0, 0)
        self.next_direction = pygame.Vector2(0, 0)
        self.speed = speed

    def at_center(self):
        return self.pixel_pos.x % TILE_SIZE == 0 and self.pixel_pos.y % TILE_SIZE == 0

    def can_move(self, direction, walls):
        next_pos = self.grid_pos + direction
        return (int(next_pos.x), int(next_pos.y)) not in walls

    def update_grid_pos(self):
        self.grid_pos = self.pixel_pos / TILE_SIZE