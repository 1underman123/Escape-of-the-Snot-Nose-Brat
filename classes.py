import pygame
from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.brat_idle = pygame.image.load('graphics/brat/brat_idle.png').convert_alpha()
        self.brat_walk = [pygame.image.load('graphics/brat/brat_walk1.png').convert_alpha(),pygame.image.load('graphics/brat/brat_walk2.png').convert_alpha()]
        self.image = pygame.image.load('graphics/brat/brat_idle.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (x, y))
        self.touching_ground = False
        self.looking_left = False
        self.velocity = pygame.Vector2(0, 0)  # Create a Vector2 object
        self.player_index = 0
        self.jump_strength = -2.6  # Adjust jump strength as needed
        self.gravity = 0.16  # Adjust gravity as needed
        self.image_timer = 0
        self.image_delay = 60
        self.jump_sfx = pygame.mixer.Sound('sounds/sfx/jump.wav')

    def update(self, keys, platforms, levers, door_group):
        self.velocity.x = 0  # Reset horizontal velocity
        
        # Adjust horizontal velocity based on key presses
        if keys[pygame.K_LEFT]:
            self.velocity.x = -0.6
            self.looking_left = True
        if keys[pygame.K_RIGHT]:
            self.velocity.x = 0.6
            self.looking_left = False
        if keys[pygame.K_e]:
            collisions = pygame.sprite.spritecollide(self, levers, False)
            for lever in collisions:
                lever.toggle(door_group)

        # Apply gravity
        self.velocity.y += self.gravity

        # Limit maximum falling speed
        if self.velocity.y > 10:
            self.velocity.y = 10

        self.move_with_collision(platforms, door_group)  # Handle collisions and move
        self.animate()

        if keys[pygame.K_SPACE]:
            self.jump()
    
    def animate(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.image_timer > self.image_delay:
            self.image_timer = current_time
            if self.velocity != pygame.Vector2(0,self.velocity.y) and self.touching_ground:
                if self.player_index > 1:self.player_index = 0
                self.image = self.brat_walk[self.player_index]
                self.player_index += 1
            else:
                self.player_index = 0
                self.image = self.brat_idle

    def move_with_collision(self, platforms, doors):
        self.rect.x += self.velocity.x
        collisions = pygame.sprite.Group()
        collisions.add(platforms)
        collisions.add(doors)
        collisions = pygame.sprite.spritecollide(self, collisions, False)
        for collision in collisions:
            if self.velocity.x > 0:
                self.rect.right = collision.rect.left
            elif self.velocity.x < 0:
                self.rect.left = collision.rect.right
            else:
                self.rect
        
        #self.velocity.y = 0
        self.rect.y += self.velocity.y

        collisions = pygame.sprite.Group()
        collisions.add(platforms)
        collisions.add(doors)
        collisions = pygame.sprite.spritecollide(self, platforms, False)
        if collisions != []:
            for collision in collisions:
                if self.velocity.y > 0:
                    self.rect.bottom = collision.rect.top
                    self.velocity.y = 0
                    self.touching_ground = True
                elif self.velocity.y < 0:
                    self.rect.top = collision.rect.bottom
                    self.velocity.y = 0
                    self.touching_ground = False

        door_collisions = pygame.sprite.spritecollide(self, doors, False)
        if door_collisions != []:
            for door in door_collisions:
                if self.velocity.y >= 0:
                    self.rect.bottom = door.rect.top
                    self.velocity.y = 0
                    self.touching_ground = True
                else:
                    self.rect.top = door.rect.bottom
                    self.velocity.y = 0

    def jump(self):
        if self.touching_ground == True:
            self.jump_sfx.play()
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
    def __init__(self, color, x, y, is_open=False, is_rotated=False):
        super().__init__()
        self.is_rotated = is_rotated
        self.initialy_open = is_open
        self.color = color
        self.image = self.colors(self.color)
        self.rect = self.image.get_rect(midbottom = (x,y))
        self.is_open = is_open
        self.pos = (x,y)
        self.sfx = pygame.mixer.Sound('sounds/sfx/door.wav')
    
    def toggle(self):
        self.is_open = not self.is_open
        self.sfx.play()

    def draw(self, screen):
        if not self.is_open:
            self.rect = self.image.get_rect(midbottom = self.pos)
            screen.blit(self.image, self.rect)
        else:
            self.rect.width = 0
            self.rect.height = 0
            
    def colors(self, color):
        if self.is_rotated == False:
            if color == "dark blue":
                return pygame.image.load('graphics/doors/dark_blue.png').convert_alpha()
            elif color == "green":
                return pygame.image.load('graphics/doors/green.png').convert_alpha()
            elif color == "hot pink":
                return pygame.image.load('graphics/doors/hot_pink.png').convert_alpha()
            elif color == "yellow":
                return pygame.image.load('graphics/doors/yellow.png').convert_alpha()
            elif color == "dark blue rotated":
                return pygame.image.load('graphics/doors/dark_blue_rotated.png')
        else:
            return pygame.image.load('graphics/doors/dark_blue_rotated.png')

class Goal(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("graphics/goal.png")
        self.rect = self.image.get_rect(midbottom = (x,y))
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def collision(self, player):
        if player.rect.colliderect(self.rect):
            return True
