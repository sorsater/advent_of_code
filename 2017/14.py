# Answer #1: 8140
# Answer #2: 1182

# Normal import with number doesn't work
hash_me = __import__('10').hash_me
knot_hash = __import__('10').knot_hash

hash_start = 'jxqlasbh'

grid = []
cnt = 0
for i in range(128):
    line = knot_hash('{}-{}'.format(hash_start, i), False)
    cnt += str(line).count('1')
    grid.append([int(a) for a in line])

print('Answer #1: {}'.format(cnt))

regions = 0
visited = set()
def dfs_me(row, col):
    if not (0 <= row < 128 and 0 <= col < 128):
        return
    if not ((row, col)) in visited and grid[row][col] == 1:
        visited.add((row, col))
        dfs_me(row+1, col)
        dfs_me(row-1, col)
        dfs_me(row, col+1)
        dfs_me(row, col-1)

for row in range(128):
    for col in range(128):
        if not ((row, col)) in visited and grid[row][col] == 1:
            dfs_me(row, col)
            regions += 1

print('Answer #2: {}'.format(regions))

