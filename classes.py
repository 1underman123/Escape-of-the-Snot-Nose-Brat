import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.brat_idle = pygame.image.load('graphics/brat/brat_idle.png').convert_alpha()
        self.brat_walk = [pygame.image.load('graphics/brat/brat_walk1.png').convert_alpha(),pygame.image.load('graphics/brat/brat_walk2.png').convert_alpha()]
        self.image = pygame.image.load('graphics/brat/brat_idle.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.touching_ground = False
        self.looking_left = False
        self.velocity = pygame.Vector2(0, 0)  # Create a Vector2 object
        self.player_index = 0
        self.jump_strength = -2.6  # Adjust jump strength as needed
        self.gravity = 0.16  # Adjust gravity as needed
        self.image_timer = 0
        self.image_delay = 100

    def update(self, keys, platforms, levers, door_group, doors):
        self.velocity.x = 0  # Reset horizontal velocity

        # Adjust horizontal velocity based on key presses
        if keys[pygame.K_LEFT]:
            self.velocity.x = -0.6
            self.looking_left = True
        elif keys[pygame.K_RIGHT]:
            self.velocity.x = 0.6
            self.looking_left = False
        elif keys[pygame.K_e]:
            collisions = pygame.sprite.spritecollide(self, levers, False)
            for lever in collisions:
                lever.toggle(doors)

        # Apply gravity
        self.velocity.y += self.gravity

        # Limit maximum falling speed
        if self.velocity.y > 10:
            self.velocity.y = 10

        self.move_with_collision(platforms, door_group)  # Handle collisions and move

        if keys[pygame.K_SPACE]:
            self.jump()
        
        self.animate()
    
    def animate(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.image_timer > self.image_delay:
            self.image_timer = current_time
            if self.velocity != pygame.Vector2(0,self.velocity.y) and self.touching_ground:
                if self.player_index > 1:self.player_index = 0
                self.image = self.brat_walk[self.player_index]
                self.player_index += 1
            else:
                self.addplayer_index = 0
                self.image = self.brat_idle

    def move_with_collision(self, platforms, doors):
        self.rect.x += self.velocity.x
        collisions = pygame.sprite.Group()
        collisions.add(platforms)
        collisions.add(doors)
        collisions = pygame.sprite.spritecollide(self, collisions, False)
        for platform in collisions:
            if self.velocity.x > 0:
                self.rect.right = platform.rect.left
            elif self.velocity.x < 0:
                self.rect.left = platform.rect.right

        self.rect.y += self.velocity.y

        collisions = pygame.sprite.Group()
        collisions.add(platforms)
        collisions.add(doors)
        collisions = pygame.sprite.spritecollide(self, platforms, False)
        if collisions != []:
            for platform in collisions:
                if self.velocity.y >= 0:
                    self.rect.bottom = platform.rect.top
                    self.velocity.y = 0
                    self.touching_ground = True
                elif self.velocity.y < 0:
                    self.rect.top = platform.rect.bottom
                    self.velocity.y = 0
                    self.touching_ground = False
        else:
            self.touching_ground = False
    def jump(self):
        if self.touching_ground == True:
            self.velocity.y = self.jump_strength
            self.touching_ground = False

    def draws(self,screen):
        if self.looking_left:
            screen.blit(pygame.transform.flip(self.image, True, False), self.rect)
        else:
            screen.blit(self.image, self.rect)

class Platform(Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Lever(Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = self.color(color)
        self.color = color
        self.rect = self.image[0].get_rect(midbottom = (x,y))
        self.is_on = False
        self.image_timer = 0
        self.image_delay = 500
    def toggle(self, doors):
        current_time = pygame.time.get_ticks()
        if current_time - self.image_timer > self.image_delay:
            self.image_timer = current_time
            self.is_on = not self.is_on
            for door in doors:
                if door.color == self.color:
                    door.toggle()
    def draw(self, screen):
        if self.is_on:
            screen.blit(self.image[1], self.rect)
        else:
            screen.blit(self.image[0], self.rect)
    def color(self, color):
        if color == "dark blue":
            return [pygame.image.load('graphics/levers/dark_blue_off.png').convert_alpha(), pygame.image.load('graphics/levers/dark_blue_on.png').convert_alpha()]
        elif color == "green":
            return [pygame.image.load('graphics/levers/green_off.png').convert_alpha(), pygame.image.load('graphics/levers/green_on.png').convert_alpha()]
        elif color == "hot pink":
            return [pygame.image.load('graphics/levers/hot_pink_off.png').convert_alpha(), pygame.image.load('graphics/levers/hot_pink_on.png').convert_alpha()]
        else:
            return [pygame.image.load('graphics/levers/yellow_off.png').convert_alpha(), pygame.image.load('graphics/levers/yellow_on.png').convert_alpha()]

class Door(Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.color = color
        self.image = self.colors(self.color)
        self.rect = self.image.get_rect(midbottom = (x,y))
        self.is_open = False
    def toggle(self):
        self.is_open = not self.is_open
    def draw(self, screen):
        if self.is_open:
            pass
        else:
            screen.blit(self.image, self.rect)
    def colors(self, color):
        if color == "dark blue":
            return pygame.image.load('graphics/doors/dark_blue.png').convert_alpha()
        elif color == "green":
            return pygame.image.load('graphics/levers/green_door.png').convert_alpha()
        elif color == "hot pink":
            return pygame.image.load('graphics/levers/hot_pink_off.png').convert_alpha()
        else:
            return pygame.image.load('graphics/levers/yellow_off.png').convert_alpha()
