import sys
import numpy as np
from config import config
from collections import deque
import time
import pygame


def is_valid(mat, visited, row, col):
    M, N = mat.shape
    return (row >= 0) and (row < M) and (col >= 0) and (col < N) \
        and mat[row][col] == 0 and not visited[row][col]


def bfs(win, startEnd, walls):
    start, end = startEnd
    start_x, start_y = start
    end_x, end_y = end
    mat = np.zeros([config['board']['w'], config['board']['h']])
    for i in walls:
        mat[i] = 1
    M, N = mat.shape

    # explore 4 neighbors
    row = [-1, 0, 0, 1]
    col = [0, -1, 1, 0]
    move = ['L', 'U', 'D', 'R']
    q = deque()

    visited = [[False for _ in range(N)] for __ in range(M)]
    visited[start_x][start_y] = True
    add = ""
    q.append((start_x, start_y, 0,add))
    min_dist = sys.maxsize

    while q:
        for event in pygame.event.get():
            # Quit if the user closes the window.
            if event.type == pygame.QUIT:
                return
        (start_x, start_y, dist, add) = q.popleft()
        if start_x == end_x and start_y == end_y:
            min_dist = dist
            break
        for k in range(4):
            if is_valid(mat, visited, start_x + row[k], start_y + col[k]):
                visited[start_x + row[k]][start_y + col[k]] = True

                win.write('*', start_x + row[k], start_y + col[k], fgcolor='green')
                q.append((start_x + row[k], start_y + col[k], dist + 1, add + move[k]))

    win.write('@', end_x, end_y)

    if min_dist != sys.maxsize:
        # find path
        start_x, start_y = startEnd[0]
        for i in range(len(add)):
            for event in pygame.event.get():
                # Quit if the user closes the window.
                if event.type == pygame.QUIT:
                    return
            index = move.index(add[i])
            start_x, start_y = start_x + row[index], start_y + col[index]
            win.write('+', start_x, start_y, fgcolor='red')
            time.sleep(0.02)

        win.write('@', end_x, end_y)
        win.write(f"The shortest path from source to destination has length {min_dist}", 1, 1)
    else:
        win.write("Destination can't be reached from a given source", 1, 1)