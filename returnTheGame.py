import pygame
from console import Console
from computer import Computer
from level import Screen
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((1024,768))
spaceConsole = Console()
spaceComputer = Computer()

oxigen = 25
testStates = [["close",1],["open",0]]

testTransitions = {"open":("close","capsule","open")}
testObjects = {oxigen, "capsule"}

testScreen = Screen(testObjects,testStates,testTransitions)

while 1:
    line = spaceConsole.update()
    if line is not None:
        line = line.lower()
        spaceComputer.processString(line,testScreen)
        print testScreen.getState()
    pygame.display.flip()