# Answer #1: 1342
# Answer #2: 2074

part1 = 0
part2 = 0
with open('input/08') as f:
    for l in f:
        s = l.split()[0]
        part1 += len(s) - len(eval(s))
        part2 += 2 + s.count('\\') + s.count('"')

print('Answer #1:', part1)
print('Answer #2:', part2)
