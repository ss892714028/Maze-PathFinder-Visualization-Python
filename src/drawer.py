import pygcurse
import pygame
from pygame.locals import *
import sys
import numpy as np
from config import config
from collections import deque
import time
from bfs import bfs



def drawer():
    win = pygcurse.PygcurseWindow(config['board']['w'], config['board']['h'], fgcolor='black')
    win.setscreencolors(None, 'white', clear=True)
    drag = False
    startEnd = []
    while len(startEnd) < 2:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                coordinate = win.getcoordinatesatpixel(event.pos)
                win.write('@', *coordinate)
                startEnd.append(coordinate)

    walls = set()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                drag = True
            elif event.type == pygame.MOUSEBUTTONUP:
                drag = False
            elif event.type == pygame.MOUSEMOTION:
                if drag:
                    coordinate = win.getcoordinatesatpixel(event.pos)
                    win.write('#', *coordinate)
                    walls.add(coordinate)
            elif event.type == pygame.KEYDOWN:
                if config['algo'] == 'bfs':
                    bfs(win, startEnd, walls)



if __name__ == "__main__":
    drawer()
