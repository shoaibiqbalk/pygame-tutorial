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


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.blit(sky_surface, (0,0)) # block image transfer
    screen.blit(ground_surface, (0,300))

    pygame.display.update()
    clock.tick(60) # maximum 60 fps
 