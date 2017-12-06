# Answer #1: 1304
# Answer #2: 18

limit = 150

from itertools import combinations

with open('input/17') as f:
    containers = [int(line.strip()) for line in f]

res = {}
for i in range(1, len(containers)):
   for comb in combinations(containers, i):
       if sum(comb) == limit:
           res[len(comb)] = res.get(len(comb), 0) + 1

print('Answer #1:', sum([val for val in res.values()]))
print('Answer #2:', res[min([key for key in res.keys()])])
