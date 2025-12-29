import pygame
from level import Level
from player import Player
from ghost import Ghost
from settings import BLACK

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.level = Level()
        self.player = Player(64, 64)
        self.ghost = Ghost(256, 64)
        self.score = 0

    def update(self):
        self.player.handle_input()
        self.player.move(self.level.walls)
        self.ghost.update(self.level.walls)

        for dot in self.level.dots[:]:
            if self.player.rect.colliderect(dot):
                self.level.dots.remove(dot)
                self.score += 10

    def draw(self):
        self.screen.fill(BLACK)
        self.level.draw(self.screen)
        self.player.draw(self.screen)
        self.ghost.draw(self.screen)