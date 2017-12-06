# Answer #1: 502
# Answer #2: 724

from itertools import permutations, combinations
from queue import Queue

board = []
with open('input/24') as f:
    for line in f:
        board.append([ch for ch in line.split()[0]])

positions = {}
chars = []
pairs = {}
paths = []
# Create dictionary of numbers and their coordinates
for y, b in enumerate(board):
    # Print board
    #print("".join(b))
    for x, t in enumerate(b):
        if t not in '.#':
            positions[t] = [x, y]
            chars.append(t)

# Find valid neighbours to position
def neighbors(b, x, y):
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    moves = []
    for direction in directions:
        tmp_x = x + direction[0]
        tmp_y = y + direction[1]
        if (0 <= tmp_x < len(b[0]) and 0 <= tmp_y < len(b)):
            if b[tmp_y][tmp_x] != '#':
                moves.append([tmp_x, tmp_y])
    return moves

# Find cheapest path
def find_path(start, goal):
    b = [l[:] for l in board]

    q = Queue()
    q.put([start, 0])

    while not q.empty():
        top = q.get()
        if top[0] == goal:
            return top[1]
        x = top[0][0]
        y = top[0][1]

        for move in neighbors(b, x, y):
            b[move[1]][move[0]] = '#'
            q.put([move, top[1] + 1])

# Calculate the distance for all pairs
for comb in combinations(chars, 2):
    res = find_path(positions[comb[0]], positions[comb[1]])
    pairs[comb[0] + comb[1]] = res
    pairs[comb[1] + comb[0]] = res

# Generate all possible paths excluding 0
chars.remove('0')
for perm in permutations(chars):
    paths.append(perm)

# Test all possible paths
def calculate_cost(part2=False):
    costs = []
    for path in paths:
        path = tuple('0') + path
        if part2:
            path = path + tuple('0')

        tmp_cost = 0
        for i in range(len(path) - 1):
            tmp_cost += pairs[path[i] + path[i+1]]
        costs.append(tmp_cost)

    return min(costs)

print("Answer #1:", calculate_cost())
print("Answer #2:", calculate_cost(part2=True))