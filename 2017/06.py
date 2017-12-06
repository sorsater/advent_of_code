Answer #1: 11137
Answer #2: 1037

with open('input/06') as f:
    regs = [int(a) for a in f.read().split('\t')]

seen = {str(regs): 0}
cntr = 1
while True:
    best = max(regs)
    best_idx = regs.index(best)
    regs[best_idx] = 0

    for i in range(best):
        best_idx += 1
        regs[best_idx%len(regs)] += 1

    if str(regs) in seen:
        print('Answer #1: {}'.format(len(seen)))
        print('Answer #2: {}'.format(cntr - seen[str(regs)]))
        break

    seen[(str(regs))] = cntr
    cntr += 1
