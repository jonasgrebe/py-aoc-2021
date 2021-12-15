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

DAY = 2


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
    h = 0
    d = 0
    
    for command in x:
        s, n = command.split()
        n = int(n)
        if s == 'forward':
            h += n
        elif s == 'down':
            d += n
        else:
            d -= n
    
    return h * d


print("Task 1 Result:", solve_task1(x))


@timing
def solve_task2(x):
    h = 0
    d = 0
    aim = 0
    
    for command in x:
        s, n = command.split()
        n = int(n)
        
        if s == 'forward':
            h += n
            d += aim * n
        elif s == 'down':
            aim += n
        else:
            aim -= n
    
    return h * d


print("Task 2 Result:", solve_task2(x))
