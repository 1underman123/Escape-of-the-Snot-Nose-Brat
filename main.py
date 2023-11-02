import pygame
from classes import Player, Platform, Lever, Door, Goal
import game_states
from sys import exit
import time

pygame.init()
pygame.mixer.init()
flags = pygame.SCALED | pygame.RESIZABLE
screen = pygame.display.set_mode((80,60),flags)
pygame.display.set_caption("Snots and Spooks: Escape-of-the-Snot-Nose-Brat")
clock = pygame.time.Clock()
gameRun = True
windowed_mode = True

# on screen timer
#font
font = pygame.font.Font('font/PixeloidMono.ttf', 9)
timer = 30
elapsed_time = 0

# make background
background = pygame.image.load('graphics/background.png').convert_alpha()
background_rect = background.get_rect(topleft = (0,2))
# create player & put it in GroupSingle
brat = Player(10,53)
brat.add(pygame.sprite.GroupSingle())

# make images variables
five_platform = pygame.image.load('graphics/platforms/5-platform.png').convert_alpha()
floor = pygame.image.load('graphics/platforms/floor.png').convert_alpha()
wall = pygame.image.load('graphics/platforms/wall.png').convert_alpha()

# make goal post
goal = Goal(79, 50)
# level one #
#platforms
level_one_platforms = [Platform(floor, 0, 52),Platform(five_platform, screen.get_width()/2, (screen.get_height()/2)+3), Platform(wall, -1, 0), Platform(wall, 80, 0)]
level_one_platforms_group = pygame.sprite.Group()
level_one_platforms_group.add(level_one_platforms)
#levers
level_one_levers = [Lever("dark blue", (screen.get_width()/2) + 2, (screen.get_height()/2)+3)]
level_one_levers_group = pygame.sprite.Group()
level_one_levers_group.add(level_one_levers)
#doors
level_one_doors = [Door("dark blue", 79, 52, False)]
level_one_doors_group = pygame.sprite.Group()
level_one_doors_group.add(level_one_doors)
#make dict and list
level_one_dict = {"Platform Group": level_one_platforms_group,
             "Lever Group": level_one_levers_group,
             "Doors Group": level_one_doors_group}
level_one_list = [level_one_platforms, level_one_levers, level_one_doors]
# level two #

# level three #

# level four #

# list of all levels #
levels_list = [level_one_list]
# Game States
title_screen = True
level_one = False
level_two = False
level_three = False
level_four = False
game_over = False
#timer
total_time = 0
elapsed_time = 0
level_one_timer = 30
level_two_timer = 20
level_three_timer = 6
level_four_timer = 10

# game loop
def main():
    pygame.init()
    pygame.mixer.init()
    flags = pygame.SCALED | pygame.RESIZABLE
    screen = pygame.display.set_mode((80,60),flags)
    pygame.display.set_caption("Snots and Spooks: Escape-of-the-Snot-Nose-Brat")
    clock = pygame.time.Clock()
    gameRun = True
    windowed_mode = True

    # on screen timer
    #font
    font = pygame.font.Font('font/PixeloidMono.ttf', 9)
    timer = 30
    elapsed_time = 0

    # make background
    background = pygame.image.load('graphics/background.png').convert_alpha()
    background_rect = background.get_rect(topleft = (0,2))
    # create player & put it in GroupSingle
    brat = Player(10,53)
    brat.add(pygame.sprite.GroupSingle())

    # make images variables
    five_platform = pygame.image.load('graphics/platforms/5-platform.png').convert_alpha()
    floor = pygame.image.load('graphics/platforms/floor.png').convert_alpha()
    wall = pygame.image.load('graphics/platforms/wall.png').convert_alpha()

    # make goal post
    goal = Goal(79, 50)
    # level one #
    #platforms
    level_one_platforms = [Platform(floor, 0, 52),Platform(five_platform, screen.get_width()/2, (screen.get_height()/2)+3), Platform(wall, -1, 0), Platform(wall, 80, 0)]
    level_one_platforms_group = pygame.sprite.Group()
    level_one_platforms_group.add(level_one_platforms)
    #levers
    level_one_levers = [Lever("dark blue", (screen.get_width()/2) + 2, (screen.get_height()/2)+3)]
    level_one_levers_group = pygame.sprite.Group()
    level_one_levers_group.add(level_one_levers)
    #doors
    level_one_doors = [Door("dark blue", 79, 52, False)]
    level_one_doors_group = pygame.sprite.Group()
    level_one_doors_group.add(level_one_doors)
    #make dict and list
    level_one_dict = {"Platform Group": level_one_platforms_group,
                 "Lever Group": level_one_levers_group,
                 "Doors Group": level_one_doors_group}
    # level two #

    # level three #

    # level four #

    # Game States
    level_one = True
    level_two = False
    level_three = False
    level_four = False
    game_over = False
    #timer
    total_time = 0
    elapsed_time = 0
    level_one_timer = 30
    level_two_timer = 20
    level_three_timer = 6
    level_four_timer = 10

    # game loop
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
                if event.key == pygame.K_RETURN and (game_over == True or title_screen == True):
                    game_over = False
                    title_screen = False
                    level_one = True
                    return "restart"
        # game states
        if level_one:
            # update player(the brat)
            brat.update(pygame.key.get_pressed(), level_one_platforms_group, level_one_levers_group, level_one_doors_group)
            screen.fill('Black')
            # draw the level
            game_states.level(level_one_dict, goal, screen, background, background_rect,level_one_timer,elapsed_time)
            # timer stuff
            total_time += 1
            elapsed_time += 1
            if elapsed_time >= 60:
                level_one_timer -= 1  # Increment by 1 second
                elapsed_time = 0
            if timer <= 0:
                level_one = False
                game_over = True
            timer_text = font.render("{:d}".format(level_one_timer), False, (255, 0, 0))
            screen.blit(timer_text,(0,0))
            # check for failure
            if level_one_timer == 0:
                level_one = False
                game_over = True
                level_one_timer = 30
                brat.kill()
            # check for success
            if goal.collision(brat):
                level_one = False
                game_over = True
                level_one_timer = 30
                brat.kill()
            # draw brat to screen
            brat.draws(screen)

        elif game_over:
            game_states.game_over(screen, font, total_time)

        pygame.display.flip()
        # cap at 60 fps
        clock.tick(60)

if __name__ == "__main__":
    exitmessage = 'restart'
    while exitmessage == 'restart':
        exitmessage = main()
