# +
import numpy as np
from functools import wraps
from time import time

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f'Elapsed Time: {(te-ts): 2.4f} sec')
        return result
    return wrap


# -


DAY = 5


def readnumpy():
    x = np.loadtxt(f'inputs/{DAY}.txt')
    print("Input:", x)
    print("Shape:", x.shape)
    print("Min:", x.min())
    print("Max:", x.max())
    return x


def readlines():
    with open(f'inputs/{DAY}.txt') as f:
        x = [line.rstrip() for line in f]
    print("Lines:", len(x))
    return x


x = readlines() # readnumpy()


@timing
def solve_task1(x):
    
    board = None
    
    lines = []
    for xx in x:
        p1, p2 = xx.split(' -> ')
        x1, y1 = p1.split(',')
        x2, y2 = p2.split(',')
        
        lines.append([int(x1), int(y1), int(x2), int(y2)])
    
    lines = np.array(lines)
    board = np.zeros(shape=(lines.max()+1, lines.max()+1))
        
    for x1, y1, x2, y2 in lines:
        
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        
        #print(x1, x2, y1, y2)
        
        if x1 == x2:
            for y in range(y1, y2+1):
                board[y, x1] += 1
        elif y1 == y2:
            for x in range(x1, x2+1):
                board[y1, x] += 1
                
    return len(np.where(board >= 2)[0])


@timing
def solve_task1(x):
    
    board = None
    
    lines = []
    for xx in x:
        p1, p2 = xx.split(' -> ')
        x1, y1 = p1.split(',')
        x2, y2 = p2.split(',')
        
        lines.append([int(x1), int(y1), int(x2), int(y2)])
    
    lines = np.array(lines)
    board = np.zeros(shape=(lines.max()+1, lines.max()+1))
        
    for x1, y1, x2, y2 in lines:
        
        xrange = range(x1, x2-1, -1) if x1 > x2 else range(x1, x2+1)
        yrange = range(y1, y2-1, -1) if y1 > y2 else range(y1, y2+1)

        if x1 == x2:
            for y in yrange:
                board[y, x1] += 1
        elif y1 == y2:
            for x in xrange:
                board[y1, x] += 1
        else:
            pass
                
    return len(np.where(board >= 2)[0])


print("Task 1 Result:", solve_task1(x))


@timing
def solve_task2(x):
    
    board = None
    
    lines = []
    for xx in x:
        p1, p2 = xx.split(' -> ')
        x1, y1 = p1.split(',')
        x2, y2 = p2.split(',')
        
        lines.append([int(x1), int(y1), int(x2), int(y2)])
    
    lines = np.array(lines)
    board = np.zeros(shape=(lines.max()+1, lines.max()+1))
    
    for x1, y1, x2, y2 in lines:
        
        xrange = range(x1, x2-1, -1) if x1 > x2 else range(x1, x2+1)
        yrange = range(y1, y2-1, -1) if y1 > y2 else range(y1, y2+1)
        
        if x1 == x2:
            for y in yrange:
                board[y, x1] += 1
        elif y1 == y2:
            for x in xrange:
                board[y1, x] += 1
        else:
            for x, y in zip(list(xrange), list(yrange)):
                board[y, x] += 1
                
    return len(np.where(board >= 2)[0])


print("Task 2 Result:", solve_task2(x))


