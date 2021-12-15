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


DAY = 15


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


x = readlines()


@timing
def solve_task1(x):
    
    grid = np.array([list(line) for line in x], dtype=int)    
    
    nodes = {(0, 0)}
    distances = {(0, 0): 0}
    distances[0, 0] = 0
    
    visited = set()
    
    target = (grid.shape[0]-1, grid.shape[1]-1)
    
    while nodes:
        node = sorted(list(nodes), key=lambda n: distances[n]).pop(0)
            
        visited.add(node)
        
        if node == target:
            break
        
        neighbors = []
        y, x = node
        
        if y > 0:
            neighbors.append((y-1, x))
        if x > 0:
            neighbors.append((y, x-1))
        if y < grid.shape[0]-1:
            neighbors.append((y+1, x))
        if x < grid.shape[1]-1:
            neighbors.append((y, x+1))
            
        neighbors = list(filter(lambda n: n not in visited, neighbors))   

        for n in neighbors:
            explored_distance = distances[(y, x)] + grid[n[0], n[1]]
            if n not in distances or explored_distance < distances[n]:
                distances[n] = explored_distance
            
        nodes = nodes.union(neighbors)
        nodes.remove(node)
        

    return distances[target]

print("Task 1 Result:", solve_task1(x))


@timing
def solve_task2(x):
    
    tile = np.array([list(line) for line in x], dtype=int)

    def get_grid_value(y, x):
        ty = y // tile.shape[0]
        tx = x // tile.shape[1]
        
        ry = y % tile.shape[0]
        rx = x % tile.shape[1]
        
        v = tile[ry, rx]
        
        if ty == 0 and tx == 0:
            return v
        
        if ty == 0:
            v = 1 + get_grid_value(y, x - tile.shape[1])
        else:
            v = 1 + get_grid_value(y - tile.shape[0], x)
        
        return v if v <= 9 else 1
    
    nodes = {(0, 0)}
    distances = {(0, 0): 0}
    distances[0, 0] = 0
    
    visited = set()
    
    target = (tile.shape[0]*5-1, tile.shape[1]*5-1)
    
    while nodes:
        node = sorted(list(nodes), key=lambda n: distances[n]).pop(0)
            
        visited.add(node)
        
        if node == target:
            break
        
        neighbors = []
        y, x = node
        
        if y > 0:
            neighbors.append((y-1, x))
        if x > 0:
            neighbors.append((y, x-1))
        if y < tile.shape[0]*5-1:
            neighbors.append((y+1, x))
        if x < tile.shape[1]*5-1:
            neighbors.append((y, x+1))
            
        neighbors = list(filter(lambda n: n not in visited, neighbors))   

        for n in neighbors:
            explored_distance = distances[(y, x)] + get_grid_value(n[0], n[1])
            if n not in distances or explored_distance < distances[n]:
                distances[n] = explored_distance
            
        nodes = nodes.union(neighbors)
        nodes.remove(node)
    
    return distances[target]


print("Task 2 Result:", solve_task2(x))
