# Answer #1: 1624
# Answer #2: 3923436

firewalls = {}
with open('input/13') as f:
    for line in f:
        key, val = line.strip().split(':')
        firewalls[int(key)] = [int(val), int(val)*2-2]

def delay(delay=0):
    for layer, length in firewalls.items():
        if (layer + delay) % length[1] == 0:
            yield layer * length[0]

print('Answer #1: {}'.format(sum([x for x in delay()])))

cntr = 0
while True:
    try:
        next(delay(cntr))
    except StopIteration:
        break
    cntr += 1
print('Answer #2: {}'.format(cntr))
