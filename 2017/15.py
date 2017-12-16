# Answer #1: 619
# Answer #2: 290

a = 591
b = 393

a_mult = 16807
b_mult = 48271
mod = 2147483647
pow16 = 2**16
def pt1(a, b):
    cntr = 0
    for i in range(40000000):
        a = (a * a_mult) % mod
        b = (b * b_mult) % mod
        if a % pow16 == b % pow16:
            cntr += 1
            print(cntr, end='\r')
    return cntr

def pt2(a, b):
    cntr = 0
    for i in range(5000000):
        while True:
            a = (a * a_mult) % mod
            if a % 4 == 0:
                break
        while True:
            b = (b * b_mult) % mod
            if b % 8 == 0:
                break

        if a % pow16 == b % pow16:
            cntr += 1
            print(cntr, end='\r')
    return cntr

print('Answer #1: {}'.format(pt1(a, b)))
print('Answer #2: {}'.format(pt2(a, b)))


