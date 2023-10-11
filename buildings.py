import pygame
from settings import *
from functions import LoadImage, DrawText

class Building():
    def __init__(self, screen, pos, facing, image, name):
        self.screen = screen
        # Position
        self.cell = pygame.Vector2(pos) # Int: Position on the grid
        self.pos = pygame.Vector2(pos[0] * TILESIZE, pos[1] * TILESIZE) # Int: Position on the map
        self.facing = facing # String: North, East, South, West
        # Display
        self.name = name
        self.image = LoadImage(image, (TILESIZE, TILESIZE))
        # Attributes
        self.inventory = []
        self.inputInventory = []
        self.outputInventory = []
        
    # def Transfer(self, item, direction):
    #     if direction == 'north':
    #         pass
    #     elif direction == 'east':
    #         pass
    #     elif direction == 'south':
    #         pass
    #     elif direction == 'west':
    #         pass
        
class Conveyor(Building):
    def __init__(self, screen, pos, facing, speed, item):
        image = 'assets/img/conveyor.png'
        name = 'Conveyor'
        super().__init__(screen, pos, facing, image, name)
        # Conveyor Attributes
        self.speed = speed # Float: Number of resources per second
        self.item = item # String: Iron, Copper, etc.
        
    def Update(self):
        pass
    
    def Draw(self):
        self.screen.blit(self.image, (self.pos.x, self.pos.y))

class Fabricator(Building):
    def __init__(self, screen, pos, facing, item, productionRate):
        image = 'assets/img/fabricator.png'
        name = 'Fabricator'
        super().__init__(screen, pos, facing, image, name)
        # Fabricator Attributes
        self.productionRate = productionRate # Float: Number of resources per second
        self.item = item # String: Iron, Copper, etc.
        self.time_since_last_production = 0 # Float: Time since last production in seconds
        
    def Update(self, dt):
        # Generate self.item at self.productionRate
        print(self.time_since_last_production)
        self.time_since_last_production += dt
        if self.time_since_last_production >= 1 / self.productionRate:
            self.outputInventory.append(self.item)
            self.inventory.append(self.item)
            self.time_since_last_production = 0
    
    def Draw(self):
        self.screen.blit(self.image, (self.pos.x, self.pos.y))
        DrawText(self.screen, str(self.inventory), font, WHITE, (self.pos.x + (TILESIZE / 2), self.pos.y + (TILESIZE / 2)))