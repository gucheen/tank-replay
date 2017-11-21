import pygame, os, ast
from pygame.locals import *
from tank import Tank
from map import Map

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Tank Replay')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    bg = Map()

    # Display some text
    # font = pygame.font.Font(None, 36)
    # text = font.render("Hello There", 1, (10, 10, 10))
    # textpos = text.get_rect()
    # textpos.centerx = background.get_rect().centerx
    # background.blit(text, textpos)

    screen.blit(background, (0, 0))
    pygame.display.flip()

    clock = pygame.time.Clock()
    tanks = pygame.sprite.Group()
    targets = ('RIGTH', 'RIGTH', 'RIGTH', 'BOTTOM', 'BOTTOM')
    for y in range(0, 800, bg.rect.height):
        for x in range(0, 800, bg.rect.width):
            background.blit(bg.image, (x, y))
    for i in range(0, 5):
        tank = Tank((0, 64 * i), targets[i])
        tanks.add(tank)
    allsprites = pygame.sprite.RenderPlain(tanks)

    with open(os.path.join('replay/logs/replay.log')) as file:
        lines = file.readlines()

    going = True
    round = 1
    # Event loop
    while going:
        clock.tick(60)
        if round > len(lines):
            # going = False
            pass
        else:
            # log = ast.literal_eval(lines[round - 1][11:])
            log = lines[round - 1][11:]
            print(log)
            round += 1
        #Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            elif event.type == pygame.KEYDOWN:
                print('press key', event.key)
                tanks.sprites()[1].go()
            # elif event.type == MOUSEBUTTONDOWN:
            #     if fist.punch(chimp):
            #         punch_sound.play() #punch
            #         chimp.punched()
            #     else:
            #         whiff_sound.play() #miss
            # elif event.type == MOUSEBUTTONUP:
            #     fist.unpunch()

        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()


if __name__ == '__main__': main()