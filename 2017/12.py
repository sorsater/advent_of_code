# Answer #1: 152
# Answer #1: 186

pipes = {}
with open('input/12') as f:
    for line in f:
        key, values = line.split('<->')
        pipes[int(key)] = [int(val) for val in values.strip().split(',')]

# From the start node visit all children until done
def count_group(start):
    q = [start]
    visited = set({start})
    while q:
        for elem in pipes[q.pop()]:
            if elem not in visited:
                visited.add(elem)
                q.append(elem)
    return visited

print('Answer #1: {}'.format(len(count_group(0))))

# Go through all pipes, remove a chunk of visited nodes
keys = set(pipes.keys())
num_groups = 0
while keys:
    for g in count_group(list(keys)[0]):
        keys.remove(g)
    num_groups += 1

print('Answer #2: {}'.format(num_groups))
