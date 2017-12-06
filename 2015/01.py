# Answer #1: 232
# Answer #1: 1783

with open('input/01') as f:
    values = [line for line in f]

def part1():
    up = values[0].count('(')
    down = values[0].count(')')
    return up - down

def part2():
    floor = 0
    for i, char in enumerate(values[0]):
        floor += 1 if char == '(' else -1
        if floor < 0:
            return i + 1

print('Answer #1:', part1())
print('Answer #2:', part2())
