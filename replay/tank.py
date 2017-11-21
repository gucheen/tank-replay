import pygame
from utils import load_image

class Tank(pygame.sprite.Sprite):
    def __init__(self, default_pos, default_target):
        pygame.sprite.Sprite.__init__(self)
        tank_body, tank_body_rect = load_image('tank.png', -1)
        gun, gun_rect = load_image('gun.png', -1)
        tank = tank_body.copy()
        tank.blit(gun, (22, 22))
        self.image = tank
        self.rect = default_pos or (0, 0)
        self.hp = 3
        self.living = True
        self.speed = 3
        self.target = 'RIGHT'
        self.angle = 0
        self.rotate(default_target or 'RIGHT')

    def rotate(self, new_target):
        if self.target is new_target:
            return
        elif new_target is 'TOP':
            self.angle -= 90
        elif new_target is 'RIGHT':
            pass
        elif new_target is 'BOTTOM':
            self.angle += 90
        elif new_target is 'LEFT':
            self.angle += 180
        new_texture = pygame.transform.rotate(self.image, self.angle)
        self.target = new_target
        self.image = new_texture
        self.block = 200

    def go(self):
        if self.target is 'TOP':
            self.rect.move_ip(0, -(self.block * self.speed))
        elif self.target is 'RIGHT':
            self.rect.move_ip(self.block * self.speed, 0)
        elif self.target is 'BOTTOM':
            self.rect.move_ip(0, self.block * self.speed)
        elif self.target is 'LEFT':
            self.rect.move_ip(-(self.block * self.speed), 0)
        