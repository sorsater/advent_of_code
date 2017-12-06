# Answer #1: 2592
# Answer #2: 2360

table = {
    '>' : [ 1,  0],
    '<' : [-1,  0],
    '^' : [ 0, -1],
    'v' : [ 0,  1],
}

with open('input/03') as f:
    cmds = f.read()

visited_1 = set()
visited_2 = set()
x, y = 0, 0
visited_1.add((x, y))
coords = [0, 0, 0, 0]
visited_2.add((0, 0))

for i, cmd in enumerate(cmds):
    offset = 0 if i % 2 == 0 else 2

    x += table[cmd][0]
    y += table[cmd][1]

    coords[offset] += table[cmd][0]
    coords[1 + offset] += table[cmd][1]

    visited_1.add((x, y))

    visited_2.add((coords[0], coords[1]))
    visited_2.add((coords[2], coords[3]))

print('Answer #1:', len(visited_1))
print('Answer #1:', len(visited_2))
