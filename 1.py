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
        print(f'took: {(te-ts): 2.4f} sec')
        return result
    return wrap


# -


DAY = 1


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


x = readnumpy()


@timing
def solve_task1(x):
    c = 0
    for i in range(1, len(x)):
        if x[i] > x[i-1]:
            c += 1
    return c


solve_task1(x)


@timing
def solve_task2(x):
    c = 0
    for i in range(1, len(x)-2):
        if x[i:i+3].sum() > x[i-1:i+2].sum():
            c += 1
    return c


solve_task2(x)


