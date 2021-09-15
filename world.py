import PPlay
from PPlay.gameimage import *
import pygame
from pygame.locals import *

TILE_SIZE = 64
img_list = []
for x in range(19):
    img = pygame.image.load(f'assets/tiles/{x}.png')
    img_list.append(img)
    
class World():
    def __init__(self):
        self.obstacle_list = []
        self.decoration_list = []
    
    def processa_dado(self, data):
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    img = img_list[tile]
                    img_rect = img.get_rect()
                    img_rect.x = x * TILE_SIZE
                    img_rect.y = y * TILE_SIZE
                    tile_data = (img, img_rect)
                if tile == 1 or tile == 2  or tile == 5  or tile == 6  or tile == 14:
                    self.obstacle_list.append(tile_data)
                else:
                    self.decoration_list.append(tile_data)
                #1,2,5,6,14

    def desenha(self, janela):
        for tile in self.obstacle_list:
            janela.screen.blit(tile[0],tile[1])
        for tile in self.decoration_list:
            janela.screen.blit(tile[0],tile[1])