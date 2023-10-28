import pygame
from classes import Player, Platform
from sys import exit

pygame.init()
flags = pygame.SCALED | pygame.RESIZABLE
screen = pygame.display.set_mode((80,60),flags)
pygame.display.set_caption('game')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
gameRun = True

# create player & put it in GroupSingle
brat = Player(10,10)
brat.add(pygame.sprite.GroupSingle())
# make platforms & put in a group
platform1 = Platform(-1000, 55, 2000, 20)
platforms_group = pygame.sprite.Group()
platforms_group.add(platform1)


while gameRun:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    brat.update(pygame.key.get_pressed(), platforms_group)
    
    # draw things idk
    screen.fill('White')
    platforms_group.draw(screen)
    brat.draws(screen)

    # update the screen
    pygame.display.update()
    pygame.display.flip()
    
    # cap at 60 fps
    clock.tick(60)