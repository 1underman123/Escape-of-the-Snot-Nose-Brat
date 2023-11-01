import pygame
from classes import Player, Platform, Lever, Door


def level(level_dict, screen, background, background_rect, timer, elapsed_time):
    screen.blit(background,background_rect)
    for groups, group in level_dict.items():
        if groups == "Platform Group":
            group.draw(screen)
        elif groups == "Lever Group":
            for lever in group:
                lever.draw(screen)
        else:
            for door in group:
                door.draw(screen)
    

#five_platform = pygame.image.load('graphics/platforms/5-platform.png').convert_alpha()
#floor = pygame.image.load('graphics/platforms/floor.png').convert_alpha()
#wall = pygame.image.load('graphics/platforms/wall.png').convert_alpha()
#platforms = [Platform(floor, 0, 52),Platform(five_platform, screen.get_width()/2, (screen.get_height()/2)+3), Platform(wall, -1, 0), Platform(wall, 80, 0)]
#platforms_group = pygame.sprite.Group()
#platforms_group.add(platforms)
## background
#background = pygame.image.load('graphics/background.png').convert_alpha()
#background_rect = background.get_rect(topleft = (0,2))
## make levers & group them
#levers = [Lever("dark blue", 10, 52), Lever("yellow", 25, 52)]
#lever_group = pygame.sprite.Group()
#lever_group.add(levers)
#
#
#
#
#
#        screen.blit(background,background_rect)
#        platforms_group.draw(screen)
#        brat.draws(screen)
#        for lever in lever_group:
#            lever.draw(screen)
#        for door in door_group:
#            door.draw(screen)
#        
#        
#
#        
#
#        # update the screen
#        pygame.display.flip()