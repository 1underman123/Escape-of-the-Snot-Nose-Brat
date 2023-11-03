import pygame
from classes import Player, Platform, Lever, Door, Goal
import game_states
from sys import exit
import time

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
    brat = Player(5,52)
    brat.add(pygame.sprite.GroupSingle())

    # make images variables
    fifteen_platform = pygame.image.load('graphics/platforms/15-platform.png').convert_alpha()
    ten_platform = pygame.image.load('graphics/platforms/10-platform.png').convert_alpha()
    seven_platform = pygame.image.load('graphics/platforms/7-platform.png').convert_alpha()
    five_platform = pygame.image.load('graphics/platforms/5-platform.png').convert_alpha()
    floor = pygame.image.load('graphics/platforms/floor.png').convert_alpha()
    wall = pygame.image.load('graphics/platforms/wall.png').convert_alpha()
    piller = pygame.image.load('graphics/platforms/piller.png').convert_alpha()

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
    #platforms
    level_two_platforms = [Platform(floor, 0, 52), Platform(wall, -1, 0), Platform(wall, 80, 0),
                           Platform(piller, 30, -63), Platform(piller, 50, -63),
                           Platform(seven_platform, 30, 37), Platform(seven_platform, 50, 37), Platform(five_platform, 46, 20)]
    level_two_platforms_group = pygame.sprite.Group()
    level_two_platforms_group.add(level_two_platforms)
    #levers
    level_two_levers = [Lever("dark blue", 22, 52), 
                        Lever("yellow",47,20)]
    level_two_levers_group = pygame.sprite.Group()
    level_two_levers_group.add(level_two_levers)
    #doors
    level_two_doors = [Door("dark blue", 32, 37), Door("dark blue", 54,37, is_open=True), Door("dark blue", 54,49, is_open=True),
                       Door("yellow", 79, 52, False), Door("yellow", 32,49), Door("yellow", 51, 37), Door("yellow", 51,49)]
    level_two_doors_group = pygame.sprite.Group()
    level_two_doors_group.add(level_two_doors)
    #make dict and list
    level_two_dict = {"Platform Group": level_two_platforms_group,
                 "Lever Group": level_two_levers_group,
                 "Doors Group": level_two_doors_group}

    # level three #
    #platforms
    level_three_platforms = [Platform(floor, 0, 52), Platform(wall, -1, 0), Platform(wall, 80, 0),
                             Platform(piller, 45, -47),
                             Platform(ten_platform, 35, 40), Platform(ten_platform, 35, 28), Platform(ten_platform, 35, 16),
                             Platform(five_platform, 16, 35)]

    level_three_platforms_group = pygame.sprite.Group()
    level_three_platforms_group.add(level_three_platforms)
    #levers
    level_three_levers = [Lever("yellow", 18, 35), Lever("yellow", 54, 52),
                          Lever("dark blue", 40, 16),
                          Lever("green", 40, 28),
                          Lever("hot pink", 40, 40)]
    level_three_levers_group = pygame.sprite.Group()
    level_three_levers_group.add(level_three_levers)
    #doors
    level_three_doors = [Door("yellow", 79, 52), Door("yellow", 36, 16), Door("yellow", 48, 52, is_open=True),
                         Door("dark blue", 36, 28), Door("dark blue", 46, 52),
                         Door("green", 36, 40),
                         Door("hot pink", 45, 52)]

    level_three_doors_group = pygame.sprite.Group()
    level_three_doors_group.add(level_three_doors)
    #make dict and list
    level_three_dict = {"Platform Group": level_three_platforms_group,
                 "Lever Group": level_three_levers_group,
                 "Doors Group": level_three_doors_group}
                 
    # level four #
    #platforms
    level_four_platforms = [Platform(floor, 0, 52), Platform(wall, -1, 0), Platform(wall, 80, 0), Platform(wall, 80, -40),
                            Platform(fifteen_platform, 10, 40), Platform(fifteen_platform, 65, 25), Platform(fifteen_platform, 52, 13),
                            Platform(seven_platform, 39, 40),
                            Platform(piller, 40, -60)]
    level_four_platforms_group = pygame.sprite.Group()
    level_four_platforms_group.add(level_four_platforms)
    #levers
    level_four_levers = [Lever("green", 15, 52),
                         Lever("dark blue", 24, 40),
                         Lever("hot pink", 53, 13),
                         Lever("yellow", 75, 25)]
    level_four_levers_group = pygame.sprite.Group()
    level_four_levers_group.add(level_four_levers)
    #doors
    level_four_doors = [Door("green", 24, 52), Door("green", 66, 25, is_open=True),
                        Door("hot pink", 79, 52),
                        Door("dark blue", 5, 42, is_rotated=True), Door("dark blue", 68, 25), Door("dark blue", 42, 40),
                        Door("yellow", 79, 52)]
    level_four_doors_group = pygame.sprite.Group()
    level_four_doors_group.add(level_four_doors)
    #make dict and list
    level_four_dict = {"Platform Group": level_four_platforms_group,
                 "Lever Group": level_four_levers_group,
                 "Doors Group": level_four_doors_group}

    # Game States
    level_one = True
    level_two = False
    level_three = False
    level_four = False
    game_over = False
    win = False
    #timer
    total_time = 0
    elapsed_time = 0
    level_one_timer = 30
    level_two_timer = 8
    level_three_timer = 8
    level_four_timer = 8

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
                if event.key == pygame.K_RETURN and (game_over == True or win == True):
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

            screen.blit(font.render("Run from Mom", False, (125, 125, 125)), (5, 10))
            # check for failure
            if level_one_timer <= 0:
                level_one = False
                game_over = True
                level_one_timer = 30
                brat.kill()
            # check for success
            if goal.collision(brat):
                level_one = False
                level_two = True
                brat.kill()
                brat = Player(5,52)
                brat.add(pygame.sprite.GroupSingle())

            # draw brat to screen
            brat.draws(screen)

        elif level_two:
            brat.update(pygame.key.get_pressed(), level_two_platforms_group, level_two_levers_group, level_two_doors_group)
            screen.fill('Black')
            # draw the level
            game_states.level(level_two_dict, goal, screen, background, background_rect, level_two_timer, elapsed_time)
            # timer stuff
            total_time += 1
            elapsed_time += 1
            if elapsed_time >= 60:
                level_two_timer -= 1  # Increment by 1 second
                elapsed_time = 0
            if timer <= 0:
                level_two = False
                game_over = True
            timer_text = font.render("{:d}".format(level_two_timer), False, (255, 0, 0))
            screen.blit(timer_text,(0,0))
            # check for failure
            if level_two_timer <= 0:
                level_two = False
                game_over = True
                level_two_timer = 30
                brat.kill()
            # check for success
            if goal.collision(brat):
                level_two = False
                level_three = True
                brat.kill()
                brat = Player(5,52)
                brat.add(pygame.sprite.GroupSingle())
            # draw brat to screen
            brat.draws(screen)

        elif level_three:
            brat.update(pygame.key.get_pressed(), level_three_platforms_group, level_three_levers_group, level_three_doors_group)
            screen.fill('Black')
            # draw the level
            game_states.level(level_three_dict, goal, screen, background, background_rect,level_three_timer,elapsed_time)
            # timer stuff
            total_time += 1
            elapsed_time += 1
            if elapsed_time >= 60:
                level_three_timer -= 1  # Increment by 1 second
                elapsed_time = 0
            if timer <= 0:
                level_three = False
                game_over = True
            timer_text = font.render("{:d}".format(level_three_timer), False, (255, 0, 0))
            screen.blit(timer_text,(0,0))
            # check for failure
            if level_three_timer == 0:
                level_three = False
                game_over = True
                level_three_timer = 30
                brat.kill()
            # check for success
            if goal.collision(brat):
                level_three = False
                level_four = True
                brat.kill()
                brat = Player(5,52)
                brat.add(pygame.sprite.GroupSingle())
            # draw brat to screen
            brat.draws(screen)
        
        elif level_four:
            brat.update(pygame.key.get_pressed(), level_four_platforms_group, level_four_levers_group, level_four_doors_group)
            screen.fill('Black')
            # draw the level
            game_states.level(level_four_dict, goal, screen, background, background_rect,level_four_timer,elapsed_time)
            # timer stuff
            total_time += 1
            elapsed_time += 1
            if elapsed_time >= 60:
                level_four_timer -= 1  # Increment by 1 second
                elapsed_time = 0
            if timer <= 0:
                level_four = False
                game_over = True
            timer_text = font.render("{:d}".format(level_four_timer), False, (255, 0, 0))
            screen.blit(timer_text,(0,0))
            # check for failure
            if level_four_timer == 0:
                level_four = False
                game_over = True
                level_four_timer = 30
                brat.kill()
            # check for success
            if goal.collision(brat):
                level_four = False
                win = True
                brat.kill()
            # draw brat to screen
            brat.draws(screen)

        elif game_over:
            game_states.game_over(screen, font, total_time)

        elif win:
            game_states.win(screen, font, total_time)
        pygame.display.flip()
        # cap at 60 fps
        clock.tick(60)

if __name__ == "__main__":
    exitmessage = 'restart'
    while exitmessage == 'restart':
        exitmessage = main()
