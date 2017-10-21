#### Credits/References start here
#Original moving figure credit    :::   https://gamedevelopment.tutsplus.com/tutorials/bone-based-unity-2d-animation-introduction--cms-21364
#### Credits/References start here

# Module import starts here
import os
import sys
import math
import pygame
import time
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
maroon = (128,0,0)
# Color definitions end here


# Variable declarations start here
class GlobalVariables:
    current_level = 1
    #total_levels = 3
    screen_size = (800,600)
    caption = 'A mad race'
    funcList = []
    paramsList = []
    characterPosition=[0,200]
    characterSelected = 1
    success =True
# Variable declarations end here


# # Utility functions start here

def ConvertYCoordinate(y):
    return GlobalVariables.screen_size[1]-y

def ImageBlitFunction(imagePath,coordinates=(0,ConvertYCoordinate(100))):
    image = pygame.image.load(imagePath).convert()
    GlobalVariables.main_screen.blit(image,coordinates)
    return

def StoreFunctionAndDraw(function,*params):
    GlobalVariables.funcList.append(function)
    GlobalVariables.paramsList.append(list(params))
    function(*params)
    pygame.display.update()
    return

def DrawEntireStack():
    functionList=GlobalVariables.funcList
    paramsList = GlobalVariables.paramsList
    for function in functionList:
        index = functionList.index(function)
        function(*paramsList[index])
    pygame.display.update()
    return

def ChangeCharacter():
    GlobalVariables.characterSelected = -GlobalVariables.characterSelected
    return

# Function to write something on screen starts here
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
    return
# Function to writ something on screen ends here

# # Utility functions end here


# # Game Level definitions start here

# Level One definitions start here
def DrawBackground():
    pygame.draw.rect(GlobalVariables.main_screen,black,(0,ConvertYCoordinate(100),800,ConvertYCoordinate(0)))
    pygame.draw.rect(GlobalVariables.main_screen,blue,(600,ConvertYCoordinate(100),200,ConvertYCoordinate(50)))
    pygame.display.update()
    return

def DrawLevelOne():
    GlobalVariables.main_screen.fill(white)
    DrawBackground()
    if GlobalVariables.characterSelected == 1:
        ImageBlitFunction('m1.png',(GlobalVariables.characterPosition[0],ConvertYCoordinate(GlobalVariables.characterPosition[1])))
    else:
        ImageBlitFunction('m2.png',(GlobalVariables.characterPosition[0],ConvertYCoordinate(GlobalVariables.characterPosition[1])))
    pygame.display.update()
    return

def LevelOneIntro():
    DrawLevelOne()
    WriteOnScreen('You are Nathan the Ninja',(200,100))
    time.sleep(3)
    DrawLevelOne()
    WriteOnScreen('You are on your path on discovery of secrets of the universe today...',(0,100))
    time.sleep(3)
    DrawLevelOne()
    WriteOnScreen('Well, to your brain capacity anyway...',(100,100))
    time.sleep(3)
    return

def LevelOneEnding():
    DrawLevelOne()
    WriteOnScreen('Nathan needs to cross the water body',(200,100))
    time.sleep(3)
    DrawLevelOne()
    WriteOnScreen('He just realised that for every move',(100,100))
    WriteOnScreen('He had to calculate amount of energy and vector  needed',(0,150))
    WriteOnScreen('And apply as much',(200,200))
    time.sleep(3)
    return

def LevelOne():
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: return
            elif event.type == pygame.KEYDOWN and (event.key == ord('a') or event.key == ord('A') or event.key == pygame.K_LEFT):
                if GlobalVariables.characterPosition[0] >= 2:
                    GlobalVariables.characterPosition[0] -= 20
                    ChangeCharacter()
            elif event.type == pygame.KEYDOWN and (event.key == ord('d') or event.key == ord('D') or event.key == pygame.K_RIGHT):
                if GlobalVariables.characterPosition[0] >=550:
                    GlobalVariables.success = True
                    GlobalVariables.current_level = 2
                    return
                else:
                    GlobalVariables.characterPosition[0] += 20
                    ChangeCharacter()
        DrawLevelOne()

# Level One definitions end  here


# Level Two definitions start here
def LevelTwo():
    GlobalVariables.main_screen.fill(white)
    pygame.display.update()
    pygame.draw.rect(GlobalVariables.main_screen, blue, (0, 200, 800,300))
    WriteOnScreen('Input the number of steps required to cross the water body', (0, 50))
    WriteOnScreen('And press Enter', (100, 100))
    brickCoordsSetOne = [380, 220]
    brickCoordsSetTwo = [420, 240]
    inputString = ''
    runLoop = True
    while True:
        if brickCoordsSetOne[1] >= 480 or brickCoordsSetTwo[1] >= 480:
            break
        pygame.draw.rect(GlobalVariables.main_screen, maroon,
                         (brickCoordsSetOne[0], brickCoordsSetOne[1],
                         10, 20))
        pygame.draw.rect(GlobalVariables.main_screen, maroon,
                         (brickCoordsSetTwo[0], brickCoordsSetTwo[1],
                         10, 20))
        brickCoordsSetOne[1] += 40
        brickCoordsSetTwo[1] += 40
    pygame.display.update()
    #print('Completed background drawing')
    runLoop = True
    while runLoop:
        clock.tick(60)
        for event in pygame.event.get():
            #print('found key ')
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                #print('Found enter key')
                runLoop = False
            elif event.type == pygame.KEYDOWN and event.unicode.isdigit():
                #print('Found alphanumeric')
                inputString += event.unicode
    print('completed event loop')
    try:
        inputString = inputString.strip()
        steps = int(inputString)
    except:
       # print ('Unable to convert to integer !!!')
        return
    #print('completed try catch block')
    if steps == 13:
        GlobalVariables.main_screen.fill(white)
        WriteOnScreen('Correct !!!', (100, 100))
        WriteOnScreen('Can be expressed in the formula :', (50, 150))
        WriteOnScreen('Steps = x + 1       where x is number of bricks'
                      , (0, 200))
        time.sleep(4)
        GlobalVariables.main_screen.fill(white)
        WriteOnScreen('Now Nathan knows math is behind everything', (0,
                      100))
        WriteOnScreen('Game Over !!!', (100, 200))
        time.sleep(3)
        #print('Game completed!!!')
    else:
        GlobalVariables.main_screen.fill(white)
        WriteOnScreen('Wrong !!!', (300, 100))
        WriteOnScreen('Game Over !!!', (100, 200))
        time.sleep(3)
       # print('Game over !!!')
    #print('Level Two complete !!!')
    return
# Level Two definitions end here

# # Game Level definitions end here




# # # Game main activity starts here

# Check availability of required modules starts here
if not pygame.font: print ('Warning, fonts disabled')
if not pygame.mixer: print ('Warning, sound disabled')
if not pygame.font: print('Warning! Font not available!!!')
# Check availability of required modules ends here

# Screen initialization starts here
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
main_screen = pygame.display.set_mode(GlobalVariables.screen_size)
pygame.display.set_caption(GlobalVariables.caption)
main_screen.fill(white)
GlobalVariables.main_screen = main_screen
clock = pygame.time.Clock()
# Screen initialization ends here

# MAIN LOOP STARTS HERE --------------------------------------------------------------------------------------------------------------------------------------------------------------
GlobalVariables.success == False
while GlobalVariables.success == True:
    if GlobalVariables.current_level == 1:
        GlobalVariables.success = False
        LevelOneIntro()
        LevelOne()
        LevelOneEnding()
    elif GlobalVariables.current_level == 2:
        GlobalVariables.success = False
        LevelTwo()
    elif GlobalVariables.current_level == 3:
        GlobalVariables.success = False
        LevelThree = None
# MAIN LOOP ENDS HERE  --------------------------------------------------------------------------------------------------------------------------------------------------------------

# # # Game main activity ends here




