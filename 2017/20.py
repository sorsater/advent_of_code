# Answer #1: 161
# Answer #2: 438

import re
from copy import deepcopy

r = re.compile(r'p=<(.*)>, v=<(.*)>, a=<(.*)>')

particles = list(enumerate([[list((eval(m))) for m in r.match(line).groups()] for line in open('input/20')]))

def man_dist(pos):
    return sum([abs(x) for x in pos])

def calc_next(p, v, a):
    n_p, n_v = [], []
    for i in range(3):
        n_p.append(p[i] + v[i] + a[i])
        n_v.append(v[i] + a[i])
    return n_p, n_v

try:
    print()
    kill_list = set()
    best = 0
    while True:
        parts = []
        visited = {} 
        closests = []
        alive_cnt = len(particles)   
        for n, (p, v, a) in particles:
            if n in kill_list:
                alive_cnt -= 1
            n_p, n_v = calc_next(p, v, a)
            closests.append([man_dist(n_p), n])
            if str(n_p) in visited:
                kill_list.add(visited[str(n_p)])
                kill_list.add(n)
            visited[str(n_p)] = n
            parts.append((n, (n_p, n_v, a)))
        best = min(closests)[1]
        particles = deepcopy(parts)
        print('\033[F Cancel when converged: {}'.format(best))
        print('\033[K Cancel when converged: {}'.format(alive_cnt), end='\r')
except KeyboardInterrupt:
    print('\033[F\033[F')
    print('\033[KAnswer #1: {}'.format(best))
    print('\033[KAnswer #2: {}'.format(alive_cnt))

