# Answer #1: QPRYCIOLU
# Answer #2: 16162

grid = {}
cur = (0,0)
with open('input/19') as f:
    for y, line in enumerate(f):
        for x, char in enumerate(line.replace('\n', '')):
            if char != ' ':
                grid[(y,x)] = char
                if y == 0:
                    cur = (y,x)

path = ''
directions = [[1,0], [0,1],[-1,0],[0,-1]]
dire = 0
while True:
    if not cur in grid:
        break
    pos = grid[(cur)]
    path += pos
    if pos == '+':
        for i, d in enumerate(directions):
            if (i+2)% 4 == dire:
                continue
            if (cur[0] + d[0], cur[1] + d[1]) in grid:
                break
        dire = i
    cur = (cur[0] + directions[dire][0], cur[1] + directions[dire][1])

print('Answer #1: {}'.format(''.join([char for char in path if char not in '+-|'])))
print('Answer #2: {}'.format(len(path)))