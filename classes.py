import pygame
from pygame.sprite import Sprite

import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.brat_idle = pygame.image.load('graphics/brat/brat_idle.png').convert_alpha()
        self.image = pygame.image.load('graphics/brat/brat_idle.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.touching_ground = False
        self.looking_left = False
        self.velocity = pygame.Vector2(0, 0)  # Create a Vector2 object

        self.jump_strength = -3.5  # Adjust jump strength as needed
        self.gravity = 0.25  # Adjust gravity as needed

    def update(self, keys, platforms):
        self.velocity.x = 0  # Reset horizontal velocity

        # Adjust horizontal velocity based on key presses
        if keys[pygame.K_LEFT]:
            self.velocity.x = -0.9
            self.looking_left = True
        elif keys[pygame.K_RIGHT]:
            self.velocity.x = 0.9
            self.looking_left = False

        # Apply gravity
        self.velocity.y += self.gravity

        # Limit maximum falling speed
        if self.velocity.y > 10:
            self.velocity.y = 10

        self.move_with_collision(platforms)  # Handle collisions and move

        if keys[pygame.K_SPACE] and self.touching_ground == True:
            self.jump()
            self.touching_ground = False
        #self.draw()
    
    def animate(self):
        pass

    def move_with_collision(self, platforms):
        self.rect.x += self.velocity.x

        collisions = pygame.sprite.spritecollide(self, platforms, False)
        for platform in collisions:
            if self.velocity.x > 0:
                self.rect.right = platform.rect.left
            elif self.velocity.x < 0:
                self.rect.left = platform.rect.right

        self.rect.y += self.velocity.y

        collisions = pygame.sprite.spritecollide(self, platforms, False)
        for platform in collisions:
            if self.velocity.y > 0:
                self.rect.bottom = platform.rect.top
                self.velocity.y = 0
                self.touching_ground = True
            elif self.velocity.y < 0:
                self.rect.top = platform.rect.bottom
                self.velocity.y = 0

    def jump(self):
        self.velocity.y = self.jump_strength

    def draws(self,screen):
        if self.looking_left:
            screen.blit(pygame.transform.flip(self.image, True, False), self.rect)
        else:
            screen.blit(self.image, self.rect)
        


class Platform(Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill((0, 255, 0))  # Green color for platforms
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self, screen):
        screen.blit(self.image, self.rect)

