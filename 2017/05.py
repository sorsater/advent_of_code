# Answer #1: 376976
# Answer #2: 29227751

with open('input/05') as f:
    instr = [int(line) for line in f]

def part1(instr):
    i, cntr = 0, 0
    try:
        while True:
            new_i = i + instr[i]
            instr[i] += 1
            i = new_i
            cntr += 1
    except IndexError:
        return cntr

def part2(instr):
    i, cntr = 0, 0
    try:
        while True:
            new_i = i + instr[i]
            instr[i] += 1 if instr[i] < 3 else -1
            i = new_i
            cntr += 1
    except IndexError:
        return cntr


print('Answer #1: {}'.format(part1(instr[:])))
print('Answer #2: {}'.format(part2(instr[:])))





