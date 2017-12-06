# Anser #1: 111754
# Anser #2: 65402

import json
import re

with open('input/12') as f:
    data = json.load(f)


# Part1, just convert to string and count numbers
def count(data):
    return sum([int(n) for n in re.findall(r'-?\d+', str(data))])
print('Answer #1 (naive):', count(data))

# Part2
def count_numbers(data, normal):
    res = []
    def unpack_data(data):
        if isinstance(data, dict):
            if normal or 'red' not in data.values():
                [unpack_data(value) for key, value in data.items()]
        elif isinstance(data, list):
            [unpack_data(item) for item in data]
        elif isinstance(data, int):
            res.append(data)
    unpack_data(data)
    return sum(res)

# Part 1
res = count_numbers(data, True)
print('Answer #1:', res)

# Part 2
res = count_numbers(data, False)
print('Answer #2:', res)