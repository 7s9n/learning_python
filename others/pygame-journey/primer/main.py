# Import the pygame module
import pygame
import os , sys

# Import random for random numbers
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    RLEACCEL
)

# Define constants for the screen width and height
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
#Define colors
WHITE = (255, 255 , 255)
BLACK = (0 , 0 , 0)
SKY_BLUE = (135, 206, 250)
# Define the Player object extending pygame.sprite.Sprite
# The surface we draw on the screen is now a property of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load( './others/pygame-journey/primer/resources/images/jet.png' ).convert()
        self.surf.set_colorkey(WHITE , RLEACCEL)
        self.rect = self.surf.get_rect()

    # Move the sprite based on keypresses
    def update(self , pressed_keys):
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5 , 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5 , 0)
        if pressed_keys[K_UP]:
            self.rect.move_ip(0 , -5)
            move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0 , 5)
            move_down_sound.play()

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# Define the enemy object extending pygame.sprite.Sprite
# Instead of a surface, we use an image for a better looking sprite
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load( 'others/pygame-journey/primer/resources/images/missile.png' ).convert()
        self.surf.set_colorkey(WHITE , RLEACCEL)
         # The starting position is randomly generated, as is the speed
        self.rect = self.surf.get_rect(
        center=(
        random.randint(SCREEN_WIDTH + 20 , SCREEN_WIDTH + 100) ,
        random.randint(0 , SCREEN_HEIGHT) ,)
        )
        self.speed = random.randint(4 , 20)

    # Move the enemy based on speed
    # Remove it when it passes the left edge of the screen

    def update(self):
        self.rect.move_ip( -self.speed , 0 )
        if self.rect.right < 0:
            self.kill()

# Define the cloud object extending pygame.sprite.Sprite
# Use an image for a better looking sprite
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load( 'others/pygame-journey/primer/resources/images/cloud.png' ).convert()
        self.surf.set_colorkey(BLACK , RLEACCEL)
         # The starting position is randomly generated
        self.rect = self.surf.get_rect(
        center=(
        random.randint(SCREEN_WIDTH + 20 , SCREEN_WIDTH + 100) ,
        random.randint(0 , SCREEN_HEIGHT) ,)
        )
    # Move the cloud based on a constant speed
    # Remove it when it passes the left edge of the screen

    def update(self):
        self.rect.move_ip( -5 , 0 )
        if self.rect.right < 0:
            self.kill()

# Initialize pygame
pygame.init()

# Setup the clock for a decent framerate
clock = pygame.time.Clock()
FPS = 30

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode( (SCREEN_WIDTH , SCREEN_HEIGHT) )
pygame.display.set_caption('Game')

#load fonts
font = pygame.font.SysFont('Arial' , 30)
game_over_txt = font.render('You\'ve lost' , True , BLACK)

def game_over():
    screen.blit(game_over_txt ,
    ( ( SCREEN_WIDTH - game_over_txt.get_width() ) / 2 ,
    (SCREEN_HEIGHT - game_over_txt.get_height()) /2 ))
    pygame.display.flip()
    pygame.event.pump()

    pygame.time.delay(3000)
# Create custom events for adding a new enemy and cloud
ADDENEMY_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY_EVENT , 250)

ADD_CLOUD_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(ADD_CLOUD_EVENT , 1000)
# Create our 'player'
player = Player()

# Create groups to hold enemy sprites, cloud sprites, and all sprites
# - enemies is used for collision detection and position updates
# - clouds is used for position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Load and play our background music
# Sound source: http://ccmixter.org/files/Apoxode/59262
# License: https://creativecommons.org/licenses/by/3.0/
pygame.mixer.music.load('others/pygame-journey/primer/resources/music/background-music.mp3')
pygame.mixer.music.play(-1)

# Load all our sound files
# Sound sources: Jon Fincher
move_up_sound = pygame.mixer.Sound('others/pygame-journey/primer/resources/music/move_up_sound.ogg')
move_down_sound = pygame.mixer.Sound('others/pygame-journey/primer/resources/music/move_down_sound.ogg')
collision_sound = pygame.mixer.Sound('others/pygame-journey/primer/resources/music/collision_sound.ogg')

# Set the base volume for all sounds
move_up_sound.set_volume(0.5)
move_down_sound.set_volume(0.5)
collision_sound.set_volume(0.5)

# Variable to keep our main loop running
running = True

#game loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        if event.type == KEYDOWN:
             # Was it the Escape key? If so, stop the loop
            if event.key == K_ESCAPE:
                running = False
        # Did the user click the window close button? If so, stop the loop
        elif event.type == QUIT:
            running = False

        # Should we add a new enemy?
        elif event.type == ADDENEMY_EVENT:
            new_enemy = Enemy()
            enemies.add(new_enemy)

            all_sprites.add(new_enemy)

        # Should we add a new cloud?
        elif event.type == ADD_CLOUD_EVENT:
            # Create the new cloud, and add it to our sprite groups
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # Update the position of our enemies and clouds
    enemies.update()
    clouds.update()
    # Fill the screen with sky blue
    screen.fill(SKY_BLUE)

     # Draw all our sprites
    for entity in all_sprites:
        screen.blit(entity.surf , entity.rect)

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player , enemies):
        # If so, remove the player
        player.kill()

        # Stop any moving sounds and play the collision sound
        move_up_sound.stop()
        move_down_sound.stop()
        collision_sound.play()

        game_over()
        # Stop the loop
        running = False

    pygame.display.flip()
    # Ensure we maintain a 30 frames per second rate
    clock.tick(FPS)

# At this point, we're done, so we can stop and quit the mixer and thr game
pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()
sys.exit()
