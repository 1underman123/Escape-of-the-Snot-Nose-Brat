import pygame
from classes import Player, Platform, Lever, Door
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
five_platform = pygame.image.load('graphics/platforms/5-platform.png')
platforms = [Platform(pygame.image.load('graphics/platforms/floor.png'), 0, 52),Platform(five_platform, screen.get_width()/2, (screen.get_height()/2)+3 )]
platforms_group = pygame.sprite.Group()
platforms_group.add(platforms)
# background
background = pygame.image.load('graphics/background.png').convert_alpha()
background_rect = background.get_rect(topleft = (0,2))
# make levers & group them
levers = [Lever("dark blue", 10, 52), Lever("yellow", 15, 52)]
lever_group = pygame.sprite.Group()
lever_group.add(levers)
# doors
doors = [Door("dark blue", 20, 52)]
door_group = pygame.sprite.Group()
door_group.add(doors)

while gameRun:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        

    brat.update(pygame.key.get_pressed(), platforms_group, lever_group, door_group, doors)

    # draw things idk
    screen.fill('Black')
    screen.blit(background,background_rect)
    platforms_group.draw(screen)
    brat.draws(screen)
    for lever in levers:
        lever.draw(screen)
    for door in doors:
        door.draw(screen)
    
    # update the screen
    pygame.display.update()
    pygame.display.flip()
    
    # cap at 60 fps
    clock.tick(60)