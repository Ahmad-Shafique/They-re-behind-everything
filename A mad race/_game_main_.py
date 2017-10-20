# Module import starts here
import os
import sys
import math
import pygame
from pygame.locals import *
#Module import ends here


# Color definitions start here
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
# Color definitions end here


# Variable declarations start here
class GlobalVariables:
    current_level = 1
    total_levels = 1
    screen_size = (800,600)
    caption = 'A mad race'
# Variable declarations end here



# Function to writ something on screen starts here
def WriteOnScreen(string,coords=None):
    try:
        if GlobalVariables.main_screen is None: print('Main screen not found')
        elif not pygame.font: print('Warning! Font not available!!!')
        else:
            font = pygame.font.Font(None, 36)
            text = font.render(string, 1, (10, 10, 10))
            if coords is None:
                coords = text.get_rect(centerx=GlobalVariables.main_screen.get_width()/2)
            GlobalVariables.main_screen.blit(text, coords)
            pygame.display.update()
    except:
        print('Unable to print out the text for some reason ...')
# Function to writ something on screen ends here



# # # Game main activity starts here

# Check availability of required modules starts here
if not pygame.font: print ('Warning, fonts disabled')
if not pygame.mixer: print ('Warning, sound disabled')
if not pygame.font: print('Warning! Font not available!!!')
# Check availability of required modules ends here

# Screen initialization starts here
os.environ['SDL_VIDEO_CENTERED'] = '1'                                                                                          #Set the game screen at the center of dsiplay
pygame.init()
main_screen = pygame.display.set_mode(GlobalVariables.screen_size)
pygame.display.set_caption(GlobalVariables.caption)
GlobalVariables.main_screen = main_screen                                                                                       #Saving the reference to main game screen in global variables, just in case
# Screen initialization ends here



# # # Game main activity ends here




