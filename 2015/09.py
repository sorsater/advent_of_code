# Answer #1: 117
# Answer #2: 909

import re
import itertools
re0 = r'(\w+) to (\w+) = (\d+)'

cities = set()
paths = {}

with open('input/09') as f:
    for line in f:
        match = re.match(re0, line.strip())
        if match:
            c0, c1, di = match.groups()
            cities.add(c0)
            cities.add(c1)
            paths[c0 + c1] = int(di)
            paths[c1 + c0] = int(di)

# Tests all combinations of cities and calculate their cost
costs = [(sum([paths[c + comb[i+1]] for i, c in enumerate(comb[:-1])])) for comb in itertools.permutations(list(cities))]

print('Answer #1:', min(costs))
print('Answer #2:', max(costs))