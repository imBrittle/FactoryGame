import pygame
import sys
import time

from settings import *
from world import *
from buildings import *
from items import *

class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Factory Game')
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.keys = []
        self.mb = []
        self.world = world
        self.tiles = self.GenerateWorld()
        self.time = time.time()
        self.deltaTime = 0
    
    def GenerateWorld(self):
        tiles = []
        for y in range(len(self.world)):
            for x in range(len(self.world[y])):
                if self.world[y][x] == ' ':
                    tiles.append(Tile((x, y), None, self.screen))
                elif self.world[y][x] == 'C':
                    tiles.append(Tile((x, y), Conveyor(self.screen, (x, y), 'north', 1, None), self.screen))
                elif self.world[y][x] == 'F':
                    tiles.append(Tile((x, y), Fabricator(self.screen, (x, y), 'north', Stone, 1), self.screen))
        return tiles
        
    def GetInputs(self):
        keys = pygame.key.get_pressed()
        mb = pygame.mouse.get_pressed()
        
        for event in pygame.event.get():
            # Quit Event
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            # Keydown Event
            if event.type == pygame.KEYDOWN:
                # Escape Key Event
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                    
    def Update(self):
        self.deltaTime = time.time() - self.time
        print(f'time {self.time}')
        print(f'dt {self.deltaTime}')
        self.time = time.time()
        for tile in self.tiles:
            tile.Update(self.deltaTime)
    
    def Draw(self):
        self.screen.fill(BLACK)
        for tile in self.tiles:
            tile.Draw()
         
    def Run(self):
        self.GetInputs()
        self.Update()
        self.Draw()
        pygame.display.update()
        self.clock.tick(FPS)