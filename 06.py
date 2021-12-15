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


DAY = 6


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
    
    fishes = [int(f) for f in x[0].split(',')]
    fishes = [fishes.count(i) for i in range(9)]

    for d in range(80):
        
        new_fishes = fishes[0]
        for i in range(8):
            fishes[i] = fishes[i+1]
        fishes[6] += new_fishes
        fishes[8] = new_fishes
            
    return sum(fishes)


print("Task 1 Result:", solve_task1(x))


@timing
def solve_task2(x):
        
    fishes = [int(f) for f in x[0].split(',')]
    fishes = [fishes.count(i) for i in range(9)]

    for d in range(256):
        
        new_fishes = fishes[0]
        for i in range(8):
            fishes[i] = fishes[i+1]
        fishes[6] += new_fishes
        fishes[8] = new_fishes
            
    return sum(fishes)


print("Task 2 Result:", solve_task2(x))


