# Answer #1: 170
# Answer #2: 247

import re

def hlf(regs, r):
    regs[r[0]] /= 2
    return 1

def tpl(regs, r):
    regs[r[0]] *= 3
    return 1

def inc(regs, r):
    regs[r[0]] += 1
    return 1

def jmp(regs, r):
    return int(r[0])

def jie(regs, r):
    return int(r[1]) if (regs[r[0]] % 2 == 0) else 1

def jio(regs, r):
    return int(r[1]) if (regs[r[0]] == 1) else 1

patterns = {
    r'hlf (\w+)': hlf,
    r'tpl (\w+)': tpl,
    r'inc (\w+)': inc,
    r'jmp (\S+)': jmp,
    r'jie (\w+), (\S+)': jie,
    r'jio (\w+), (\S+)': jio,
}

with open('input/23') as f:
    cmds = [line.strip() for line in f]

def main(a=0, b=0):
    regs = {
        'a': a,
        'b': b,
    }
    idx = 0
    while idx < len(cmds):
        cmd = cmds[idx]
        for key, func in patterns.items():
            match = re.match(key, cmd)
            if match:
                idx += func(regs, match.groups())
                break
        else:
            print('No match:', cmd)

    return regs['b']

print('Answer #1:', main(a=0, b=0))
print('Answer #2:', main(a=1, b=0))