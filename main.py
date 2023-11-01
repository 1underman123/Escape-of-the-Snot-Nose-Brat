import pygame
from classes import Player, Platform, Lever, Door
from sys import exit

pygame.init()
pygame.mixer.init()
flags = pygame.SCALED | pygame.RESIZABLE
screen = pygame.display.set_mode((80,60),flags)
pygame.display.set_caption("Snots and Spooks: Escape-of-the-Snot-Nose-Brat")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
gameRun = True
windowed_mode = True

# on screen timer
#font
font = pygame.font.Font('font/PixeloidMono.ttf', 9)
timer = 30
elapsed_time = 0

# create player & put it in GroupSingle
brat = Player(10,53)
brat.add(pygame.sprite.GroupSingle())
# make platforms & put in a group
five_platform = pygame.image.load('graphics/platforms/5-platform.png')
floor = pygame.image.load('graphics/platforms/floor.png')
platforms = [Platform(floor, 0, 52),Platform(five_platform, screen.get_width()/2, (screen.get_height()/2)+3 )]
platforms_group = pygame.sprite.Group()
platforms_group.add(platforms)
# background
background = pygame.image.load('graphics/background.png').convert_alpha()
background_rect = background.get_rect(topleft = (0,2))
# make levers & group them
levers = [Lever("dark blue", 10, 52), Lever("yellow", 25, 52)]
lever_group = pygame.sprite.Group()
lever_group.add(levers)

# doors
doors = [Door("dark blue", 20, 52, False), Door("yellow", 30, 52, True)]
door_group = pygame.sprite.Group()
door_group.add(doors)

# Game States
title_screen = False
level_one = True
game_over = False

while gameRun:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                windowed_mode = not windowed_mode
                if windowed_mode:
                    screen = pygame.display.set_mode((80, 60), pygame.SCALED | pygame.RESIZABLE)
                else:
                    screen = pygame.display.set_mode((80, 60), pygame.SCALED | pygame.RESIZABLE | pygame.FULLSCREEN)

    if level_one:
        # update player(the brat)
        brat.update(pygame.key.get_pressed(), platforms_group, lever_group, door_group)
        # draw things idk
        screen.fill('Black')
        screen.blit(background,background_rect)
        platforms_group.draw(screen)
        brat.draws(screen)
        for lever in lever_group:
            lever.draw(screen)
        for door in door_group:
            door.draw(screen)
        
        

        elapsed_time += 1
        if elapsed_time >= 60:
            timer -= 1  # Increment by 1 second
            elapsed_time = 0
        if timer <= 0:
            level_one = False
            game_over = True

        timer_text = font.render("{:d}".format(timer), True, (255, 0, 0))
        screen.blit(timer_text,(0,0))

        # update the screen
        pygame.display.flip()
        
    elif game_over:
        break
    else:
        break

    # cap at 60 fps
    clock.tick(60)