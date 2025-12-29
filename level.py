import pygame
from settings import TILE_SIZE, BLUE, WHITE

LEVEL_MAP = [
    "####################",
    "#........##........#",
    "#.#######.##.#######.#",
    "#..................#",
    "#.####.########.####.#",
    "#..................#",
    "####################",
]

class Level:
    def __init__(self):
        self.walls = set()
        self.dots = set()
        self.load()

    def load(self):
        for y, row in enumerate(LEVEL_MAP):
            for x, tile in enumerate(row):
                if tile == '#':
                    self.walls.add((x, y))
                elif tile == '.':
                    self.dots.add((x, y))

    def draw(self, screen):
        for x, y in self.walls:
            pygame.draw.rect(screen, BLUE, (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))
        for x, y in self.dots:
            pygame.draw.circle(screen, WHITE,
                (x*TILE_SIZE + TILE_SIZE//2, y*TILE_SIZE + TILE_SIZE//2), 4)