# Answer #1: 373
# Answer #2: 260

import re

pattern = r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)'

peggy_sue = {
    'children': [3, (lambda x,y: x==y)],
    'cats': [7, (lambda x,y: x>y)],
    'samoyeds': [2, (lambda x,y: x==y)],
    'pomeranians': [3, (lambda x,y: x<y)],
    'akitas': [0, (lambda x,y: x==y)],
    'vizslas': [0, (lambda x,y: x==y)],
    'goldfish': [5, (lambda x,y: x<y)],
    'trees': [3, (lambda x,y: x>y)],
    'cars': [2, (lambda x,y: x==y)],
    'perfumes': [1, (lambda x,y: x==y)],
}

def check_part1(pars, vals):
    for i, par in enumerate(pars):
        if not peggy_sue[par][0] == vals[i]:
            return False
    return True

def check_part2(pars, vals):
    for i, par in enumerate(pars):
        if not peggy_sue[par][1](vals[i], peggy_sue[par][0]):
            return False
    return True

sue_1 = ''
sue_2 = ''

with open('input/16') as f:
    for line in f:
        sue, par1, val1, par2, val2, par3, val3 = re.match(pattern, line).groups()

        pars = [par1, par2, par3]
        vals = [int(val1), int(val2), int(val3)]

        if check_part1(pars, vals):
            sue_1 = int(sue)

        if check_part2(pars, vals):
            sue_2 = int(sue)

print('Answer #1:', sue_1)
print('Answer #2:', sue_2)
