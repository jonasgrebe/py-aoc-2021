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


DAY = 7


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
    crabs = np.array(list(map(int, x[0].split(','))))
    return int(np.abs(crabs - np.median(crabs)).sum())


print("Task 1 Result:", solve_task1(x))


@timing
def solve_task2(x):
    crabs = np.array(list(map(int, x[0].split(',')))).astype(int)
    fuels = []
    
    print(0.5 * (2 * crabs - 1))
    
    positions = list(range(crabs.min(), crabs.max()))
    for pos in positions:
        delta = np.abs(crabs - pos)
        fuels.append((delta * (delta + 1) / 2).sum())
    
    return int(np.min(fuels))
        


print("Task 2 Result:", solve_task2(x))


