import pygame
from settings import TILE_SIZE, BLUE, WHITE

LEVEL_MAP = [
    "################",
    "#..............#",
    "#.####.####.###.#",
    "#..............#",
    "################",
]

class Level:
    def __init__(self):
        self.walls = []
        self.dots = []
        self.load_level()

    def load_level(self):
        for y, row in enumerate(LEVEL_MAP):
            for x, tile in enumerate(row):
                world_x = x * TILE_SIZE
                world_y = y * TILE_SIZE
                if tile == '#':
                    self.walls.append(pygame.Rect(world_x, world_y, TILE_SIZE, TILE_SIZE))
                elif tile == '.':
                    self.dots.append(pygame.Rect(world_x + 12, world_y + 12, 8, 8))

    def draw(self, screen):
        for wall in self.walls:
            pygame.draw.rect(screen, BLUE, wall)
        for dot in self.dots:
            pygame.draw.circle(screen, WHITE, dot.center, 4)
