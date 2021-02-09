# nrow < 0 & ncol < 0
# nrow >= len(maze) & ncol >= len(maze[0])
# visit[nrow][ncol]
# maze[nrow][ncol] == "*"
# all of these comparisons are the basic operations
# it is calculated once every time the algorithm tries a move legal or illegal
# Basic Operation Steps:  	∑ni=04*4
# 			=>	16 ∑ni=01
# 			=>	16(n+1)
# 			=>	16n + 16
# Let g(n) = n and t(n) = 16n + 16
# Limx->∞ (16n + 16)/n
# Limx->∞ 16n/n + Limx->∞16/n
# =16+0
# =16 is a constant
# Therefore t(n) ∈ Θg(n)=n.
import time
from collections import deque
import os


def main():
    name = input("Enter the name of the maze you want to check: ")
    name1 = "mazes/" + name + ".txt"
    count = -1
    global erow, ecol, temp
    global maze, neighbour, final, next_path, visit, total_move, left_path, cnt, num, rowQ, colQ
    rowQ = deque([])
    colQ = deque([])
    maze = []
    neighbour = []
    final = []
    next_path = 0
    visit = []
    total_move = 0
    left_path = 1
    cnt = 0
    f = open(name1, "r")
    data = f.readlines()
    for x in data:
        count = count + 1
        maze.append([])
        visit.append([])
        neighbour.append([])
        for y in x.rstrip():
            maze[count].append(y)
            visit[count].append(False)
            neighbour[count].append(None)
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "e":
                erow = i
                ecol = j
                break
    num = 0
    start = time.time()
    num = bfsalgo()
    end = time.time()
    temp = []
    if num == -1:
        print("No Path!!")
        print("Time: %f" % (end - start))
    else:
        print("Moves:", num)
        final.append((list(neighbour[erow][ecol])))
        temp = (list(neighbour[erow][ecol]))
        for i in range(num-1):
            for j in range(1):
                final.append(list(neighbour[temp[0]][temp[1]]))
                temp = list(neighbour[temp[0]][temp[1]])
        print(final)
        print("Time %f" % (end - start))


def bfsalgo():
    global complete
    global left_path
    global total_move
    global next_path
    global maze, neighbour, final, visit, total_move, cnt, srow, scol, rowQ, colQ
    complete = False
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "s":
                srow = i
                scol = j
    rowQ.append(srow)
    colQ.append(scol)
    visit[srow][scol] = True
    while len(rowQ) > 0:
        r = rowQ.popleft()
        c = colQ.popleft()
        if maze[r][c] == "e":
            complete = True
            break
        adjacent(r, c)
        left_path -= 1
        if left_path == 0:
            left_path = next_path
            next_path = 0
            total_move += 1
    if complete:
        return total_move
    return -1


def adjacent(r, c):
    global next_path
    global maze, neighbour, final, next_path, visit, total_move, cnt, nrow, ncol, rowQ, colQ
    dc = [-1, +1, 0, 0]
    dr = [0, 0, +1, -1]
    nrow = 0
    ncol = 0
    for i in range(4):
        nrow = r + dr[i]
        ncol = c + dc[i]
        if nrow < 0 or ncol < 0 or nrow >= len(maze) or ncol >= len(maze[0]) or visit[nrow][ncol] or \
                maze[nrow][ncol] == "*":
            continue
        rowQ.append(nrow)
        colQ.append(ncol)
        neighbour[nrow][ncol] = (r, c)
        visit[nrow][ncol] = True
        next_path += 1


def openfile():
    while True:
        menu = os.listdir("/Users/rehankedia/desktop/semester 4/comp 157/project1/mazes")
        while True:
            for x in menu:
                y = x.split(".txt")
                print(y[0])
            break
        main()


if __name__ == "__main__":
    openfile()
