# Answer #1: 1642
# Answer #2: 33601318

step_count = 301

cur_idx = 0
code = [0]
for i in range(1, 2017+1):
    cur_idx = (cur_idx + step_count) % len(code)
    code.insert(cur_idx+1, i)
    cur_idx += 1

print('Answer #1: {}'.format(code[code.index(2017)+1]))

cur_idx = 0
best = -1
# Zero is always at the beginning
# Save just the value if it is after 0
for i in range(1, 50000000+1):
    cur_idx = (cur_idx + step_count) % i
    if cur_idx == 0:
        best = i
    cur_idx += 1
print('Answer #2: {}'.format(best))

