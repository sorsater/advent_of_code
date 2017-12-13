# Answer #1: 1624
# Answer #2: 3923436

firewalls = {}
with open('input/13') as f:
    for line in f:
        key, val = line.strip().split(':')
        firewalls[int(key)] = [int(val), int(val)*2-2]

def delay(delay=0, part2=False):
    caught = 0
    for layer in firewalls.keys():
        if (layer + delay) % firewalls[layer][1] == 0:
            if part2:
                return False
            caught += layer * firewalls[layer][0]

    return True if part2 else caught

print('Answer #1: {}'.format(delay()))

cntr = 0
while True:
    if delay(cntr, True):
        break
    cntr += 1
print('Answer #2: {}'.format(cntr))
