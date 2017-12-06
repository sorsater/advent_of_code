# Answer #1: 383
# Answer #2: 265

with open('input/04') as f:
    codes = [line.strip().split() for line in f]

part1 = sum([1 for code in codes if len(code) == len(set(code))])
print('Answer #1: {}'.format(part1))

part2 = sum([1 for code in codes if len(code) == len(set([''.join(sorted(word)) for word in code]))])    
print('Answer #2: {}'.format(part2))