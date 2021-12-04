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


DAY = 4


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
    N = 5
    
    lines = x
    draws = list(map(int, lines[0].split(',')))
    
    lines = list(filter(lambda l: len(l)>0, lines[1:]))
    
    boards = np.array([[list(map(int, l.split())) for l in lines[i:i+N]] for i in range(0, len(lines), N)])
    hits = np.zeros_like(boards, dtype=bool)
    
    for k, d in enumerate(draws):
        
        hits[np.where(boards == d)] = True
        
        for b_idx, b_hits in enumerate(hits):
            
            for i in range(N):
                if b_hits[i,:].sum() == N or b_hits[:,i].sum() == N:
                    return (boards * ~hits)[b_idx].sum() * d

    return None


solve_task1(x)


@timing
def solve_task2(x):
    N = 5
    
    lines = x
    draws = list(map(int, lines[0].split(',')))
    
    lines = list(filter(lambda l: len(l)>0, lines[1:]))
    
    boards = np.array([[list(map(int, l.split())) for l in lines[i:i+N]] for i in range(0, len(lines), N)])
    hits = np.zeros_like(boards, dtype=bool)
    
    board_wins = np.zeros(len(boards))
    for k, d in enumerate(draws):
        
        hits[np.where(boards == d)] = True
        
        for b_idx, b_hits in enumerate(hits):
            
            if board_wins[b_idx] == 1:
                continue
            
            for i in range(N):
                if b_hits[i,:].sum() == N or b_hits[:,i].sum() == N:
                    
                    board_wins[b_idx] = 1
                    if board_wins.sum() == len(boards):
                        return (boards * ~hits)[b_idx].sum() * d

    return None


solve_task2(x)


