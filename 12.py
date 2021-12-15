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


DAY = 12


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
import itertools

@timing
def solve_task1(x):
    
    def is_small(cave):
        return cave.islower()
    
    def is_big(cave):
        return not is_small(cave)
        
    rules = {}
    for r0, r1 in [line.split('-') for line in x]:
        if r0 not in rules:
            rules[r0] = []
        rules[r0].append(r1)
        
        if r1 not in rules:
            rules[r1] = []
        rules[r1].append(r0)
        
        
    def visitable(path, node):
        if r1 == 'start':
            return False
        if is_big(node):
            return True
        else:
            return node not in path

        
    def expansion(path):
        
        if path[-1] == 'end':
            return [path]
        
        if path[-1] not in rules:
            return []
        
        return [path + (r1,) for r1 in rules[path[-1]] if visitable(path, r1)]

    
    paths = [('start',)]
    
    changes = True
    while changes:
        changes = False
        expansions = [expansion(path) for path in paths]
        
        
        paths = []
        for exp in expansions:
            paths.extend(exp)
            
        for path in paths:
            if path[-1] != 'end':
                changes = True

        
    return len(paths)
# -

print("Task 1 Result:", solve_task1(x))

# +
import itertools

@timing
def solve_task2(x):
    
    def is_small(cave):
        return cave.islower()
    
    def is_big(cave):
        return not is_small(cave)
        
    rules = {}
    for r0, r1 in [line.split('-') for line in x]:
        if r0 not in rules:
            rules[r0] = []
        rules[r0].append(r1)
        
        if r1 not in rules:
            rules[r1] = []
        rules[r1].append(r0)
        
        
    def visitable(path, node):
        if node == 'start':
            return False
        if is_big(node) or node == 'end':
            return True
        else:
            small_nodes = list(filter(is_small, path))
            #print(small_nodes)
            count_nodes = list(map(lambda n: path.count(n), small_nodes))
            
            #print(path, node, max(count_nodes) <= 1)
            return max(count_nodes) <= 1 or node not in path
                

        
    def expansion(path):
        
        if path[-1] == 'end':
            return [path]
        
        if path[-1] not in rules:
            return []
        
        return [path + (r1,) for r1 in rules[path[-1]] if visitable(path, r1)]

    
    paths = [('start',)]
    
    changes = True
    while changes:
        changes = False
        expansions = [expansion(path) for path in paths]
        
        
        paths = []
        for exp in expansions:
            paths.extend(exp)
            
        for path in paths:
            if path[-1] != 'end':
                changes = True

        
    return len(paths)
# -

print("Task 2 Result:", solve_task2(x))




