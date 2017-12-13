# Answer #1: 10616
# Answer #2: 5101

with open('input/09') as f:
    a = f.read()

i = 0
res = 0
depth = 0
garbage = False
garbage_cnt = 0
while True:
    if i >= len(a):
        break
    
    char = a[i]
    i += 1

    if char == '!':
        i += 1
        continue
    elif char == '<':
        if not garbage:
            garbage = True
            continue
    if garbage:
        if char == '>':
            garbage = False
        else:
            garbage_cnt += 1
    else:
        if char == '{':
            depth += 1
            res += depth
        elif char == '}':
            depth -= 1

print('Answer #1: {}'.format(res))
print('Answer #2: {}'.format(garbage_cnt))