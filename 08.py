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


DAY = 8


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
segs = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

nums_in = {
    'a': [0, 2, 3, 5, 6, 7, 8, 9],
    'b': [0, 4, 5, 6, 8, 9],
    'c': [0, 1, 2, 3, 4, 7, 8, 9],
    'd': [2, 3, 4, 5, 6, 8, 9],
    'e': [0, 2, 6, 8],
    'f': [0, 1, 3, 4, 5, 6, 7, 8, 9],
    'g': [0, 2, 3, 5, 6, 8, 9]
}

segs_of = {}
for seg in nums_in:
    for num in nums_in[seg]:
        if num not in segs_of:
            segs_of[num] = ()
        segs_of[num] += (seg, )

num_len = {num: len(segs_of[num]) for num in segs_of}
nums_with_len = {}

for num in num_len:
    l = num_len[num]
    if l not in nums_with_len:
        nums_with_len[l] = []
    nums_with_len[l].append(num)
    
print("NUM_LEN:", num_len)
print("NUMS_WITH_LEN:", nums_with_len)


# -

@timing
def solve_task1(x):
    
    cnt = 0
    for entry in x:
        patterns = entry.split()
        inputs, outputs = patterns[:-5], patterns[-4:]
        
        cnt += len([output for output in outputs if len(output) in [2, 3, 4, 7]])
        
    return cnt


print("Task 1 Result:", solve_task1(x))


@timing
def solve_task2(x):
    
    sum = 0
    for entry in x:
        tokens = entry.split()
        patterns, signals = tokens[:-5], tokens[-4:]

        patterns = list(map(set, patterns))

        pwl = {}
        for p in patterns:
            if len(p) not in pwl:
                pwl[len(p)] = [p]
            else:
                pwl[len(p)].append(p)
        
        c = {}
        
        p = [None] * 10
        
        p[8] = pwl[7][0]
        p[7] = pwl[3][0]
        p[1] = pwl[2][0]
        p[4] = pwl[4][0]
        
        
        for p5 in pwl[5]:
            if p[1].issubset(p5):
                p[3] = p5
                break
                
        for p5 in pwl[5]:
            if p5 == p[3]:
                continue
            
            elif len(p5 & p[4]) == 2:
                p[2] = p5
            else:
                p[5] = p5
        
        for p6 in pwl[6]:
            if len(p6 & p[1]) == 1:
                p[6] = p6
            elif len(p6 & p[4]) == 3:
                p[0] = p6
            else:
                p[9] = p6
                
        
        # determine codes
        c['a'] = list(p[7] - p[1])[0]
        c['f'] = list(p[1] - p[2])[0]
        c['c'] = list(p[7] - p[5])[0]
        c['d'] = list(p[8] - p[0])[0]
        c['b'] = list(p[4] - {c['c'], c['d'], c['f']})[0]
        c['g'] = list(p[9] - {c['a'], c['b'], c['c'], c['d'], c['f']})[0]
        c['e'] = list(p[8] - p[9])[0]
        
        c = {v: k for k, v in c.items()}
        
        for i in range(len(signals)):
            translated = list(map(lambda x: c[x], list(signals[i])))
            signals[i] = ''.join(translated)
            
        
        for i, signal in enumerate(signals):
            for digit in range(10):
                if set(signal) == set(segs_of[digit]):
                    sum += 10 ** (3 - i) * digit
        
    print(sum)

print("Task 2 Result:", solve_task2(x))




