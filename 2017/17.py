# Answer #1: 1642
# Answer #2: 33601318

step_count = 301

import sys
sys.path.append('..')
from w8m8 import progressbar

cur_idx = 0
code = [0]
for i in range(2017):
    cur_idx = (cur_idx + step_count) % (i+1) + 1
    code.insert(cur_idx, i+1)

print('Answer #1: {}'.format(code[code.index(2017)+1]))

# Zero is always at the beginning of the code
# Save value if it have index 1
cur_idx = 0
best = -1
n_iter = 50000000
for i in range(n_iter):
    cur_idx = (cur_idx + step_count) % (i+1) + 1
    best = i + 1 if cur_idx == 1 else best
    progressbar(i/n_iter) if i % 100000 == 0 else None
print('\033[KAnswer #2: {}'.format(best))

