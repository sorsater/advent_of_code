# Answer #1: 16076
# Answer #2: 2797

import re

regexes = {
    r'(\w+) -> (\w+)': (lambda x: x),
    r'(\w+) AND (\w+) -> (\w+)': (lambda w1, w2: w1 & w2),
    r'(\w+) OR (\w+) -> (\w+)': (lambda w1, w2: w1 | w2),
    r'(\w+) RSHIFT (\d+) -> (\w+)': (lambda w1, x: w1 >> int(x)),
    r'(\w+) LSHIFT (\d+) -> (\w+)': (lambda w1, x: w1 << int(x)),
    r'NOT (\w+) -> (\w+)': (lambda w: 65535 - w),
}

with open('input/07') as f:
    cmds = [line.strip() for line in f]

def main(prev):
    cmds_copy = cmds[:]
    wires = {}

    while not 'a' in wires:
        for i in range(len(cmds_copy) -1, -1, -1):
            cmd = cmds_copy[i]
            for reg, func in regexes.items():
                match = re.match(reg, cmd)
                if match:
                    try:
                        t_wire = match.groups()[-1]
                        if prev > 0 and t_wire == 'b':
                            wires[t_wire] = prev
                        else:
                            wires[t_wire] = func(*[int(wires.get(val, val)) for val in match.groups()[:-1]])
                        del cmds_copy[i]
                        break
                    except:
                        break
    return wires['a']

part1 = main(0)
part2 = main(part1)

print("Answer #1:", part1)
print("Answer #2:", part2)