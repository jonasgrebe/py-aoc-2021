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


DAY = 3


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
    x = list(map(list, x))
    x = np.array(x, dtype=int)
    
    gamma = np.round(np.mean(x, axis=0))
    epsilon = 1 - gamma

    gamma = int(''.join([f'{int(l)}' for l in gamma]), 2)
    epsilon = int(''.join([f'{int(l)}' for l in epsilon]), 2)
    
    return gamma * epsilon


print("Task 1 Result:", solve_task1(x))


@timing
def solve_task2(x):
    x = list(map(list, x))
    x = np.array(x, dtype=int)
    
    x_oxygen = x.copy()
    x_co_two = x.copy()
    
    for i in range(x.shape[1]):
        
        most_common = np.mean(x_oxygen[:, i])
        if most_common >= 0.5:
            most_common = 1
        else:
            most_common = 0
            
        least_common = np.mean(x_co_two[:, i])
        if least_common < 0.5:
            least_common = 1
        else:
            least_common = 0
            
        if len(x_oxygen) > 1:
            x_oxygen = x_oxygen[np.where(x_oxygen[:, i] == most_common)]
      
        if len(x_co_two) > 1:
            x_co_two = x_co_two[np.where(x_co_two[:, i] == least_common)]   
        
            
    oxygen = x_oxygen[0]
    co_two = x_co_two[0]
    
            
    oxygen = int(''.join([f'{int(l)}' for l in oxygen]), 2)
    co_two = int(''.join([f'{int(l)}' for l in co_two]), 2)

    return oxygen * co_two

print("Task 2 Result:", solve_task2(x))
