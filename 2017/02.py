# Answer #1: 32020
# Answer #2: 236

with open('input/02') as f:
    sheet = [[int(num) for num in line.split()] for line in f]

res1 = sum([max(line) - min(line) for line in sheet])
print('Answer #1: {}'.format(res1))

res2 = sum([sum([x // y for j, y in enumerate(line) for i, x in enumerate(line) if i != j and x % y == 0]) for line in sheet])
print('Answer #2: {}'.format(res2))