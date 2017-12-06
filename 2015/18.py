# Answer #1: 768
# Answer #2: 781

import time
from copy import deepcopy

iterations = 100
animate = False

with open('input/18') as f:
    grid = [list(line.strip()) for line in f]

dim = [len(grid), len(grid[0])]

neighbours = (
    (-1,-1), (-1,0), (-1,1),
    (0,-1), (0,1),
    (1,-1), (1,0), (1,1),
)

def pretty_print(grid):
    [print(''.join([str(item) for item in row])) for row in grid]

def count_neighbours(grid, x, y):
    on = ''
    for _y, _x in neighbours:
        if 0 <= y + _y < dim[0]:
            if 0 <= x + _x < dim[1]:
                on += grid[y + _y][x + _x]

    return on.count('#')

def update(grid, part2):
    new_grid = [['-'] * dim[1] for i in range(dim[0])]

    for y, row in enumerate(grid):
        for x, item in enumerate(row):
            n = count_neighbours(grid, x, y)

            if n == 3 or (item == '#' and n == 2):
                new_grid[y][x] = '#'
            else:
                new_grid[y][x] = '.'

    if part2:
        new_grid[0][0] = '#'
        new_grid[0][dim[1]-1] = '#'
        new_grid[dim[0]-1][0] = '#'
        new_grid[dim[0]-1][dim[1]-1] = '#'

    return new_grid

def main(grid, part2):
    for i in range(iterations):
        grid = update(grid, part2)

        if animate:
            pretty_print(grid)
            time.sleep(0.2)

    return sum([row.count('#') for row in grid])

grid_cpy = deepcopy(grid)

part1 = main(grid, part2=False)
part2 = main(grid_cpy, part2=True)

print('Answer #1:', part1)
print('Answer #2:', part2)
