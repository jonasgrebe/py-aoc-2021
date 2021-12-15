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


DAY = 14


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
    
    template = x[0]
    rules = {}
    
    for line in x[2:]:
        x, y = line.split(' -> ')
        if x in rules:
            raise IllegalArgumentError
        else:
            rules[x] = y
    
    for _ in range(10):
        
        inserts = []
        
        for i in range(len(template)-1):
            x = template[i:i+2]
            if x in rules:
                y = rules[x]
                inserts.append((i+1, y))
        
        for ins in inserts[::-1]:
            idx, y = ins
            template = template[:idx] + y + template[idx:]
        
    max_cnt = 0
    min_cnt = len(template)
    for c in set(template):
        cnt = template.count(c)
        print(c, cnt)
        max_cnt = max(max_cnt, cnt)
        min_cnt = min(min_cnt, cnt)
    
    print(max_cnt, min_cnt)
    return max_cnt - min_cnt


print("Task 1 Result:", solve_task1(x))


@timing
def solve_task2(x):
    
    template = x[0]
    rules = {}
    
    for line in x[2:]:
        x, y = line.split(' -> ')
        if x in rules:
            raise IllegalArgumentError
        else:
            rules[x] = y
            
    occurences = {}
    for i in range(len(template)-1):
        x = template[i:i+2]
        if x in rules:
            if x not in occurences:
                occurences[x] = 0
            occurences[x] += 1
            
    update_rules = {}
    for x, y in rules.items():
        if x not in update_rules:
            update_rules[x] = []
            if x[0] + y in rules:
                update_rules[x].append(x[0]+y)
            if y + x[1] in rules:
                update_rules[x].append(y+x[1])
    
    for x in update_rules:
        if x not in occurences:
            occurences[x] = 0
        
   
    

    for s in range(40):
        #print(s, {k: v for k, v in occurences.items() if v > 0})
        
        new_occurences = {}
        for occ in occurences:
            
            if occurences[occ] == 0:
                continue
            
            if occ not in new_occurences:
                new_occurences[occ] = 0
            else:
                new_occurences[occ] -= occurences[occ]
            
            for update in update_rules[occ]:
                
                if update not in new_occurences:
                    if update in occurences:
                        new_occurences[update] = occurences[update]
                    else:
                        new_occurences[update] = 0

                new_occurences[update] += occurences[occ]
                
        #print({k: v for k, v in new_occurences.items() if v > 0})
        occurences = new_occurences
                
    cnts = {}
    for x, cnt in occurences.items():
        if x[0] not in cnts:
            cnts[x[0]] = 0
        if x[1] not in cnts:
            cnts[x[1]] = 0
            
        cnts[x[0]] += cnt
        cnts[x[1]] += cnt
        
    cnts[template[0]] += 1
    cnts[template[-1]] += 1
    
    for x in cnts:
        cnts[x] /= 2    
        
    vals = cnts.values()
    print(cnts)
    return int(max(vals) - min(vals))
    

print("Task 2 Result:", solve_task2(x))


