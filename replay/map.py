import pygame
from utils import load_image

class Map(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        image, rect = load_image('ground.png')
        self.image = image
        self.rect = pygame.rect.Rect(0, 0, 64, 64)
