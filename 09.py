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


DAY = 9


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
x = list(map(list, x))
x = np.array(x, dtype=int)
print(x.shape)


# +
def get_local_minima(x):
    h, w = x.shape
    
    x = np.pad(x, ((1,1),(1,1)), mode='constant')
    x[0], x[h+1] = x[2], x[h-1]
    x[:,0], x[:,w+1] = x[:, 2], x[:,w-1]
    
    presence = np.ones_like(x, dtype=bool)
    
    for i in range(x.shape[0]-1):
        presence[i] &= (x[i] - x[i+1]) < 0
    for i in range(1, x.shape[0]):
        presence[i] &= (x[i] - x[i-1]) < 0
        
    for j in range(x.shape[1]-1):
        presence[:, j] &= (x[:, j] - x[:, j+1]) < 0
    for j in range(1, x.shape[1]):
        presence[:, j] &= (x[:, j] - x[:, j-1]) < 0
    
    return presence[1:-1, 1:-1]

@timing
def solve_task1(x):
    presence = get_local_minima(x) 
    return (x + 1)[presence].sum()


# -

print("Task 1 Result:", solve_task1(x))


@timing
def solve_task2(x):
    local_minima = get_local_minima(x) 
    
    remaining = np.ones_like(x, dtype=bool)
    remaining[x == 9] = False
    
    x = np.pad(x, ((1,1),(1,1)), mode='constant')
    remaining = np.pad(remaining, ((1,1), (1,1)), mode='constant')
    
    def recursive_summation(i, j):
        s = 1
        remaining[i, j] = False
        
        if remaining[i+1, j]:
            s += recursive_summation(i+1, j)
        if remaining[i-1, j]:
            s += recursive_summation(i-1, j)
        if remaining[i, j+1]:
            s += recursive_summation(i, j+1)
        if remaining[i, j-1]:
            s += recursive_summation(i, j-1)
        
        return s
    
    i_locs, j_locs = np.where(local_minima)
    basin_sizes = []
    for i, j in zip(i_locs, j_locs):
        s = recursive_summation(i+1, j+1)
        basin_sizes.append(s)
    
    return np.prod(sorted(basin_sizes)[-3:])


print("Task 2 Result:", solve_task2(x))


