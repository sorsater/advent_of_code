# Answer #1: 1393
# Answer #2: 1292

with open('input/01') as f:
    code = f.read()

res1 = sum([int(code[i]) for i in range(len(code)) if code[i] == (code + code[0])[i+1]])
print('Answer #1: {}'.format(res1))

res2 = sum([int(code[i]) for i in range(len(code)) if code[i] == (code + code)[i+len(code)//2]])
print('Answer #2: {}'.format(res2))