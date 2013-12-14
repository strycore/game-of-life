import sys
import random
import pygame
from engine.game import World

pygame.init()

size = 800, 600
bg_color = 0, 0, 80

screen = pygame.display.set_mode(size)

cell_size = 5
cell_color = (253, 1, 80)
cell_surf = pygame.Surface((cell_size, cell_size))
cell_rect = cell_surf.fill(cell_color)
cell_rect.right = 100
cell_rect.bottom = 100

seed = set()
for i in range(6000):
    seed.add((random.randrange(160), random.randrange(120)))
world = World(seed)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(bg_color)
    for cell in world.cells:
        screen.blit(cell_surf, (cell[0] * cell_size, cell[1] * cell_size))
    pygame.time.delay(10)
    pygame.display.flip()
    world.tick()
