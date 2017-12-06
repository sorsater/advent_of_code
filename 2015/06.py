# Answer #1: 569999
# Answer #2: 17836115

import re

re0 = r'(\w+) (\d+),(\d+) through (\d+),(\d+)'

with open('input/06') as f:
    cmds = [re.findall(re0, line)[0] for line in f]

grid_1 = []
grid_2 = []
for x in range(1000):
    grid_1.append([False] * 1000)
    grid_2.append([0] * 1000)

for i, (instr, x_1, y_1, x_2, y_2) in enumerate(cmds):
    print('Progress: {0:.0f}%'.format(100 * (i+1) / len(cmds)), end='\r')
    for x in range(int(x_1), int(x_2) + 1):
        for y in range(int(y_1), int(y_2) + 1):
            if instr == 'toggle':
                grid_1[y][x] = not grid_1[y][x]
                grid_2[y][x] += 2
            elif instr == 'on':
                grid_1[y][x] = True
                grid_2[y][x] += 1
            else:
                grid_1[y][x] = False
                if grid_2[y][x] > 0:
                    grid_2[y][x] -= 1

print('Answer #1:', sum([sum(g) for g in grid_1]))
print('Answer #2:', sum([sum(g) for g in grid_2]))
