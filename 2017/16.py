# Answer #1: pkgnhomelfdibjac
# Answer #2: pogbjfihclkemadn

with open('input/16') as f:
    cmds = f.read().split(',')

line_len = 16
line = [chr(97 + i) for i in range(line_len)]

def perform_dance(line, n_iter):
    seen_lines = []
    
    for n in range(n_iter):
        # When repeating cycle found, return what it will end on
        str_line = ''.join(line)
        if str_line in seen_lines:
            return seen_lines[n_iter % n]
        seen_lines.append(str_line)

        for cmd in cmds:
            if cmd[0] == 's':
                line = line[-int(cmd[1:]):] + line[:line_len-int(cmd[1:])]
            else:
                idx_1, idx_2 = map(int if cmd[0] == 'x' else line.index, cmd[1:].split('/'))
                line[idx_1], line[idx_2] = line[idx_2], line[idx_1]
    
    return ''.join(line)

print('Answer #1: {}'.format(perform_dance(line[:], 1)))
print('Answer #2: {}'.format(perform_dance(line[:], 1000000000)))
