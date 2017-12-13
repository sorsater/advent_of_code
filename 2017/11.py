# Answer #1: 715
# Answer #2: 1512

with open('input/11') as f:
    instr = f.read().split(',')

visited = []
x, y = 0, 0
# Axial coordinates
walk = {
    'n': [0,-1],
    'ne': [1,-1],
    'se': [1,0],
    's': [0,1],
    'sw': [-1,1],
    'nw': [-1,0],
}
max(x1, y1, z1)
for inst in instr:    
    _x, _y = walk[inst]
    x += _x
    y += _y
    visited.append(max(x,y,-(x+y)))

print('Answer #1: {}'.format(max(x,y,-(x+y))))
print('Answer #2: {}'.format(max(visited)))
