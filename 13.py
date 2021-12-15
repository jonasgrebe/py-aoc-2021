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


DAY = 13


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


# +
@timing
def solve_task1(x):
    
    coords = [line.split(',') for line in x if ',' in line]
    coords = np.array(coords, dtype=int)
            
    folds = list(filter(lambda l: l.startswith('fold'), x))
    folds = list(map(lambda l: l.replace('fold along ', ''), folds))
    folds = list(map(lambda l: l.split('='), folds))    
    
    w, h = coords.max(axis=0)    
    grid = np.zeros((h+1, w+1), dtype=bool)
    
    for cx, cy in coords:
        grid[cy, cx] = True
        
    for direction, line in folds:
        line = int(line)
        h, w = grid.shape
        
        if direction == 'x':    
            new_grid = np.zeros((h, 2 * line + 1), dtype=bool)
            new_grid[:,:w] = grid
            grid = new_grid
                    
            grid[:,:line] += np.fliplr(grid[:,-line:])
            grid = grid[:,:line]
            
        else:
            new_grid = np.zeros((2 * line + 1, w), dtype=bool)
            new_grid[:h,:] = grid
            grid = new_grid
                
            grid[:line,:] += np.flipud(grid[-line:,:])
            grid = grid[:line,:]
        
        return grid.sum()
    
        
# -

print("Task 1 Result:", solve_task1(x))


@timing
def solve_task2(x):
    
    coords = [line.split(',') for line in x if ',' in line]
    coords = np.array(coords, dtype=int)
            
    folds = list(filter(lambda l: l.startswith('fold'), x))
    folds = list(map(lambda l: l.replace('fold along ', ''), folds))
    folds = list(map(lambda l: l.split('='), folds))    
    
    w, h = coords.max(axis=0)    
    grid = np.zeros((h+1, w+1), dtype=bool)
    
    for cx, cy in coords:
        grid[cy, cx] = True
        
    for direction, line in folds:
        line = int(line)
        h, w = grid.shape
        
        if direction == 'x':    
            new_grid = np.zeros((h, 2 * line + 1), dtype=bool)
            new_grid[:,:w] = grid
            grid = new_grid
                    
            grid[:,:line] += np.fliplr(grid[:,-line:])
            grid = grid[:,:line]
            
        else:
            new_grid = np.zeros((2 * line + 1, w), dtype=bool)
            new_grid[:h,:] = grid
            grid = new_grid
                
            grid[:line,:] += np.flipud(grid[-line:,:])
            grid = grid[:line,:]
        
    display = [''.join(list(map(str, x))).replace('0', '.').replace('1', 'X') for x in grid.astype(int)]
    
    
    for l in display:
        print(l)
        

print("Task 2 Result:", solve_task2(x))


