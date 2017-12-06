# Answer #1: 664
# Answer #2: 640

import re
import itertools

pattern = r'(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)'

people = set()
config = {}
with open('input/13') as f:
    for line in f:
        match = re.match(pattern, line)
        if match:
            p1, gain_lose, val, p2 = match.groups()
            config[p1 + p2] = int(val) if gain_lose == 'gain' else -int(val)
            people.add(p1)

def find_optimum_seating(people):
    costs = []
    for perm in itertools.permutations(list(people)):
        tmp_cost = config[perm[0] + perm[-1]]
        tmp_cost += config[perm[-1] + perm[0]]
        for i in range(len(perm) - 1):
            tmp_cost += config[perm[i] + perm[i+1]]
            tmp_cost += config[perm[i+1] + perm[i]]
        costs.append(tmp_cost)
    return max(costs)

print('Answer #1:', find_optimum_seating(people))

for p in people:
    config[p + 'Michael'] = 0
    config['Michael' + p] = 0

people.add('Michael')

print('Answer #2:', find_optimum_seating(people))