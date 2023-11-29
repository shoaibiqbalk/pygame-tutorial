import pygame
import sys

# Initializing a pygame object - Starting pygame program
pygame.init()

# Pygame window screen size
screen = pygame.display.set_mode((800, 400))
# Window title
pygame.display.set_caption('Football')


# Setting framerates
clock = pygame.time.Clock() 

## Adding object
# test_surface = pygame.Surface((100, 200))
# test_surface.fill('Red')

# importing image
sky_surface = pygame.image.load('graphics/Sky.png') # variable name specify what object we are adding
ground_surface = pygame.image.load('graphics/ground.png')

# adding text
# 1. create a font
score_font = pygame.font.Font('font/Pixeltype.ttf', 50)
# 2. write text on a surface 
score_text = score_font.render('Score', True, 'Black')
# 3. blid the text surface


snail_surface = pygame.image.load('graphics/snail/snail1.png')
snail_x_position = 700
movement = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.blit(sky_surface, (0,0)) # block image transfer
    screen.blit(ground_surface, (0,300))
    screen.blit(score_text, (10, 10))
    snail_x_position = snail_x_position - movement
    if snail_x_position < 10:
        movement = -2
    elif snail_x_position > 700:
        movement = 2
    else:
        pass
    
    screen.blit(snail_surface, (snail_x_position, 265))
    
    pygame.display.update()
    clock.tick(60) # maximum 60 fps
 