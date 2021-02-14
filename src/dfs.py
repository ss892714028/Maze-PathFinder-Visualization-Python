import sys
import numpy as np
from config import config
from collections import deque
import time


def dfs(win, startEnd, walls):
    start, end = startEnd
    start_x, start_y = start
    end_x, end_y = end
    mat = np.zeros([config['board']['w'], config['board']['h']])
    for i in walls:
        mat[i] = 1
    M, N = mat.shape
    

