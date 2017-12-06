# Answer #1: 329356
# Answer #2: 4666278

puzzle_input = '3113322113'
seq = [int(char) for char in puzzle_input]

iterations = 50
res = []
for i in range(iterations):
    new_seq = []
    prev = seq[0]
    prev_cnt = 0
    for curr in seq:
        if curr == prev:
            prev_cnt += 1
        else:
            new_seq += [prev_cnt, prev]
            prev_cnt = 1

        prev = curr
    new_seq += [prev_cnt, prev]

    seq = new_seq[:]
    print('Progress: {0:.0f}%'.format(100*(i+1)/iterations), end='\r')
    res.append(len(seq))

print('Answer #1:', res[39])
print('Answer #2:', res[49])
