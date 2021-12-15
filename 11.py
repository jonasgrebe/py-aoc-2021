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


DAY = 11


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
    
    octos = np.array([np.array(list(line), dtype=int) for line in x])
        
    def get_overloads():
        overloads = np.where(octos > 9)
        overloads = {(y, x) for y, x in zip(overloads[0], overloads[1])}
        return overloads
    
    total_flashes = 0
    for _ in range(100):
        octos += 1
        
        overloads = get_overloads()
        flashed = set()
        has_flashed = np.zeros_like(octos, dtype=bool)
        
        def flash(y, x):
            if has_flashed[y, x]:
                return
            y_min = max(y-1, 0)
            y_max = min(y+1, octos.shape[0]-1)
            x_min = max(x-1, 0)
            x_max = min(x+1, octos.shape[1]-1)

            octos[y_min: y_max+1, x_min: x_max+1] += 1
            has_flashed[y, x] = True
            flashed.add((y, x))
        
        while overloads:
            y, x = overloads.pop()
            flash(y, x)
            new_overloads = get_overloads()
            overloads = overloads.union(new_overloads - flashed)
        
        total_flashes += has_flashed.sum()
        octos[has_flashed] = 0
        
    return total_flashes
        


print("Task 1 Result:", solve_task1(x))


@timing
def solve_task2(x):
    
    octos = np.array([np.array(list(line), dtype=int) for line in x])
        
    def get_overloads():
        overloads = np.where(octos > 9)
        overloads = {(y, x) for y, x in zip(overloads[0], overloads[1])}
        return overloads
    
    for step in range(10000):
        octos += 1
        
        overloads = get_overloads()
        flashed = set()
        has_flashed = np.zeros_like(octos, dtype=bool)
        
        def flash(y, x):
            if has_flashed[y, x]:
                return
            y_min = max(y-1, 0)
            y_max = min(y+1, octos.shape[0]-1)
            x_min = max(x-1, 0)
            x_max = min(x+1, octos.shape[1]-1)

            octos[y_min: y_max+1, x_min: x_max+1] += 1
            has_flashed[y, x] = True
            flashed.add((y, x))
        
        while overloads:
            y, x = overloads.pop()
            flash(y, x)
            new_overloads = get_overloads()
            overloads = overloads.union(new_overloads - flashed)
        
        octos[has_flashed] = 0
        
        if has_flashed.all():
            return step + 1
        


print("Task 2 Result:", solve_task2(x))


