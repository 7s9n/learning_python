import pygame
import sys
from os import path
import random

pygame.mixer.pre_init()
pygame.init()

# Window settings
TITLE = 'Name Of Game'
WIDTH = 800
HEIGHT = 400
SIZE = [WIDTH , HEIGHT]
FBS = 60
# Controls
JUMP = [pygame.K_UP , pygame.K_SPACE]

# Colors
WHITE = (255 , 255 , 255)
BLACK = (0 , 0  , 0)
# Fonts
FONT_SM = pygame.font.Font("assets/font/Pixeltype.ttf", 32)
FONT_MD = pygame.font.Font("assets/font/Pixeltype.ttf", 64)

# Helper functions

def load_image(file_path , width = None , height = None):
    img = pygame.image.load(file_path)
    if not width or not height:
        width , height = img.get_size()
    img = pygame.transform.scale(img , (width , height))

    return img

def play_sound(sound , loops = 0 , maxtime = 0 , fade_ms = 0):
    sound.play(loops , maxtime , fade_ms)

def play_music():
    pygame.mixer.music.play(-1)

# Images
player_walk1 = load_image( path.join('assets' , 'graphics' , 'player' , 'player_walk_1.png') )
player_walk2 = load_image( path.join('assets' , 'graphics' , 'player' , 'player_walk_2.png') )
player_jump = load_image( path.join('assets' , 'graphics' , 'player' , 'jump.png') )

player_images = {
    'run' : [player_walk1 , player_walk2] ,
    'jump': player_jump,
}

fly1 = load_image( path.join('assets' , 'graphics' , 'fly' , 'fly1.png') )
fly2 = load_image( path.join('assets' , 'graphics' , 'fly' , 'fly2.png') )

fly_images = [ fly1 , fly2 ]

snail1 = load_image( path.join('assets' , 'graphics' , 'snail' , 'snail1.png') )
snail2 = load_image( path.join('assets' , 'graphics' , 'snail' , 'snail2.png') )

snail_images = [snail1 , snail2]

ground = load_image( path.join('assets' , 'graphics' , 'ground.png') )
sky = load_image( path.join('assets' , 'graphics' , 'sky.png') )

# Sounds
JUMP_SOUND = pygame.mixer.Sound( path.join('assets' , 'audio' , 'jump.wav') )

#Musics
pygame.mixer.music.load( path.join('assets' , 'audio' , 'music.wav') )

#User defined events
ADD_OBSTACLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_OBSTACLE_EVENT , 2000)

#configurations
config = {
    'snail_images':snail_images,
    'fly_images' : fly_images,
}

class Entity(pygame.sprite.Sprite):
    def __init__(self , x , y , image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.vx = 0
        self.vy = 0

class Character(Entity):
    score = 0
    def __init__(self , images):
        self.running_images = list( map(lambda img: img.convert_alpha() , images['run'] ) )
        super().__init__(0 , 0 , self.running_images[0])
        self.image_jump = images['jump'].convert_alpha()
        self.image_index = 0
        self.rect.midbottom = (80 , 300)
        self.gravity = 0

    def update(self , *args , **kwargs):
        self.set_image()
        self.jump()

    def jump(self):
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
        self.gravity += 1

    def set_image(self):
        if self.rect.bottom < 300:
            self.image = self.image_jump
        else:
            self.image_index += 0.1
            if self.image_index >= len(self.running_images):
                self.image_index = 0
            self.image = self.running_images[ int( self.image_index ) ]

    @property
    def can_jump(self):
        return self.rect.bottom == 300

class Obstacle(Entity):
    def __init__(self , x , y , images):
        if not isinstance(images , list):
            images = [images]
        self.images = list( map(lambda img: img.convert_alpha() , images ) )
        self.image_index = 0
        super().__init__(x , y , self.images[0])
        self.vx = random.randint(4 , 6)

    def set_image(self):
        self.image_index += 0.1
        if self.image_index >= len( self.images ):
            self.image_index = 0
        self.image = self.images[ int(self.image_index) ]

    def move(self):
        self.rect.move_ip( -self.vx , self.vy )

    def destroy(self):
        if self.rect.right < 0:
            self.kill()
            Character.score += 1

class Fly(Obstacle):
    def __init__(self , fly_images , **_ignored):
        super().__init__(0 , 0 , fly_images)
        self.rect.midbottom = ( random.randint(1000 , 1100) , 210 )

    def update(self , *args , **kwargs):
        self.set_image()
        self.move()
        self.destroy()

class Snail(Obstacle):
    def __init__(self , snail_images , **_ignored):
        super().__init__(0 , 0 ,  snail_images)
        self.rect.midbottom = ( random.randint(1000 , 1500) , 300 )

    def update(self):
        self.set_image()
        self.move()
        self.destroy()

def get_random_obstacle(**kwargs):
    return random.choice([Fly , Snail])(**kwargs)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.done = False
        self.reset()

    def reset(self):
        play_music()
        self.player = pygame.sprite.GroupSingle( Character(player_images) )
        self.obstacle_group = pygame.sprite.Group()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.done = True
                elif event.key in JUMP and self.player.sprite.can_jump:
                    self.player.sprite.gravity = -20
                    self.player.sprite.jump()
                    play_sound(JUMP_SOUND)
            elif event.type == ADD_OBSTACLE_EVENT:
                self.obstacle_group.add( get_random_obstacle(**config) )

    def update(self):
        self.player.update()
        self.obstacle_group.update()

    def draw(self):
        self.screen.blit( sky.convert_alpha() , (0 , 0) )
        self.screen.blit( ground.convert_alpha() , (0 , 300) )
        self.display_stats()

        self.player.draw(self.screen)
        self.obstacle_group.draw(self.screen)

        pygame.display.flip()

    def display_stats(self):
        score_text = FONT_SM.render( f'Score: {str(Character.score)}' , 1 , BLACK )
        self.screen.blit(score_text , (WIDTH - score_text.get_width() - 32 , 32) )

    def loop(self):
        while not self.done:
            self.process_events()
            self.update()
            self.draw()
            self.clock.tick(FBS)


if __name__ == '__main__':
    game = Game()
    game.loop()
    pygame.quit()
    sys.exit()
