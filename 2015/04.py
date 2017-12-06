# Answer #1: 117946
# Answer #2: 3938038

import hashlib

code = 'ckczppom'

def md5_me(n):
    c = 0
    while True:
        c += 1
        md5 = hashlib.md5((code + str(c)).encode('utf-8')).hexdigest()
        if(md5[:n] == '0' * n):
            return c

print('Answer #1:', md5_me(5))
print('Answer #2:', md5_me(6))
