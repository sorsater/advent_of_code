# Answer #1: 1045
# Answer #2: 265

import re
from queue import PriorityQueue
from copy import deepcopy

regex = r'/dev/grid/node-x(\d+)-y(\d+)'

seen_grids = set()

def read_file():
	grid = []
	with open("input/22", 'r') as f:
		for line in f:
			if line[:4] != '/dev':
				continue
			node, size, used, avai, proc = line.split()
			x, y = [int(c) for c in re.match(regex, node).groups()]
			if y > len(grid) - 1:
				grid.append([])
			grid[y].append([x, y, int(size[:-1]), int(used[:-1]), int(avai[:-1])])
	return grid

def show_grid(grid, goal):
	for y in range(len(grid)):
		line = ""
		for x in range(len(grid[0])):
			elem = grid[y][x]
			if x == 0 and y == 0:
				line += '(.)'
			elif elem[3] == 0:
				line += ' _ '
			elif goal[0] == x and goal[1] == y:
				line += ' G '
			elif elem[3] > grid[0][0][2]:
				line += ' # '
			else:
				line += ' . '
		print(line)

def part1(orig_grid):
	cnt = 0
	cmds = [item for sublist in orig_grid for item in sublist]
	for A in cmds:
		for B in cmds:
			if A[0] == B[0] and A[1] == B[1]: # Same coordinates
				continue
			if A[3] == 0:
				continue
			#if B[2] - B[3] >= A[3]:
			if B[4] >= A[3]:
				cnt += 1
	return cnt

orig_grid = read_file()
print("Answer #1:", part1(orig_grid))
# Part 2.
print("\
\nFrom '-' to next to 'G' is 94.\
\nMove one step takes 5 moves (34 in total). Then a final move.\
\n\nThis gives: 94 + 34 * 5 + 1 = 265")
show_grid(orig_grid, [len(orig_grid[0]) - 1, 0])
print("Answer #2: 265")
