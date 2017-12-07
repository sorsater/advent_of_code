# Answer #1: mwzaxaj
# Answer #2: 1219

import re
from collections import Counter

re_leaf = r'(\w+) \((\d+)\)'
re_node = r'(\w+) \((\d+)\) -> (.*)'

with open('input/07') as f:
    regs = [line.strip() for line in f]

# Store all data
discs = {}
leafs = {}
nodes = {}
for reg in regs:
    nodes_match = re.match(re_node, reg)
    leaf_match = re.match(re_leaf, reg)
    if nodes_match:
        name, number, children = nodes_match.groups()
        children = children.split(', ')
        nodes[name] = (int(number), children)
    elif leaf_match:
        name, number = leaf_match.groups()
        leafs[name] = int(number)
    else:
        print('No match: ', reg)
        break
        
    name, number = leaf_match.groups()
    discs[name] = int(number)

part1 = ''
part2 = ''
while True:
    if len(nodes) == 1:
        part1 = list(nodes.keys())[0]
        break
    new_nodes = {}
    new_leafs = []
    # Iterate through all nodes with children
    for name, (number, children) in nodes.items():
        new_children = []
        nums = []
        # Remove childrens if leafs
        for child in children:
            if child not in leafs:
                new_children.append(child)
            else:
                nums.append(leafs[child])

        # Detect wrong disc, part2
        if not part2 and len(set(nums)) > 1:
            for key, val in Counter(nums).items():
                if val == 1:
                    odd_boy = key
                else:
                    ok_boy = key

            orig_val = discs[children[nums.index(odd_boy)]]
            part2 = orig_val - (odd_boy - ok_boy)

        # Update for next iteration
        if len(new_children) > 0:
            new_nodes[name] = (number + sum(nums), new_children)
        else:
            new_leafs.append((number + sum(nums), name))

    nodes = new_nodes
    for number, name in new_leafs:
        leafs[name] = number

print('Answer #1: {}'.format(part1))
print('Answer #2: {}'.format(part2))