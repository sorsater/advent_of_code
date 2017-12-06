# Answer #1: 535
# Answer #2: 212

import re

pattern = '(\w+) => (\w+)'

# Dictionary for all rules
chemist = {}
with open('input/19') as f:
    for line in f:
        match = re.match(pattern, line.strip())
        if match:
            key, value = match.groups()
            chemist[key] = chemist.get(key, []) + [value]
        else:
            if len(line.strip()) > 0:
                code = line.strip()
                break

# Longest key
len_keys = max([len(key) for key in chemist.keys()])

def one_iteration(code):
    unique = set()
    for i in range(len(code)):
        for key, val in chemist.items():
            for idx in range(1, len_keys + 1):
                if i + idx > len(code):
                    continue
                if code[i:i+idx] != key:
                    continue
                for v in val:
                    tmp = code[:i] + v + code[i+idx:]
                    unique.add(tmp)
    return list(unique)

part1 = len(one_iteration(code))
print('Answer #1:', part1)

# Part 2
# Tried brute force, didn't finish.
# Formula for calculating the nr of reactions needed
# All reactions are either 1 element -> 2 elements or 1 element -> ? Rn ? Ar.
# The first character have always the length 1.
# If the length in the middle are longer than 1 there exists element 'Y' in it.
# So, count all elements, remove all Rn, Ar, remove all Y and finally 1

nr_elem = sum([1 if str.isupper(char) else 0 for char in code])
print('Answer #2:', nr_elem - code.count('Rn') - code.count('Ar') - 2 * code.count('Y') - 1)

