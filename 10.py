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


DAY = 10


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
scores_1 = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

openers = '([{<'
closers = ')]}>'

pairs = {k: v for k, v in zip(openers, closers)}

@timing
def solve_task1(x):
    
    def illegal_scores(line):
        stack = []
        for c in line:
            if c in openers:
                stack.append(c)
            elif c in closers:
                opener = stack.pop()
                if pairs[opener] != c:
                    return scores_1[c]
        return 0
           
    x_scores = list(map(illegal_scores, x))
    
    return sum(x_scores)


# -

print("Task 1 Result:", solve_task1(x))

# +
scores_2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

openers = '([{<'
closers = ')]}>'

pairs = {k: v for k, v in zip(openers, closers)}

@timing
def solve_task2(x):
    
    def is_not_corrupted(line):
        stack = []
        for c in line:
            if c in openers:
                stack.append(c)
            elif c in closers:
                opener = stack.pop()
                if pairs[opener] != c:
                    return False
        return True
           
    x = list(filter(is_not_corrupted, x))
    
    def completion_scores(line):
        stack = []
        for c in line:
            if c in openers:
                stack.append(c)
            elif c in closers:
                opener = stack.pop()
        
        comp = list(map(lambda o: pairs[o], stack[::-1]))
        score = 0
        for c in comp:
            score *= 5
            score += scores_2[c] 
        
        return score
        
    points = sorted(list(map(completion_scores, x)))    
    
    return points[len(points) // 2]


# -

print("Task 2 Result:", solve_task2(x))


