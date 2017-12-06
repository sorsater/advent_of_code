# Answer #1: 10439961859
# Answer #2: 72050269

import itertools
from collections import Counter
from operator import mul
from functools import reduce

with open('input/24') as f:
    elems = [int(line.strip()) for line in f]

# Find the upper limit for looping
def find_ul(part_sum):
    ul_sum = 0
    for i, elem in enumerate(elems):
        ul_sum += elem
        if ul_sum > part_sum:
            return i - 1
    return len(elems)

def find_comb(elements, part_sum, idx):
    valid = []
    for comb in itertools.combinations(elements, idx):
        if sum(comb) == part_sum:
            valid.append(list(comb))
    return valid

def find_comb_prod(i, part_sum):
    valid = []
    for comb in itertools.combinations(elems, i):
        if sum(comb) == part_sum:
            # Add with their score
            valid.append([reduce(mul, comb), list(comb)])

    return valid

def part1():
    part_sum = int(sum(elems)/3)

    ul = find_ul(part_sum)

    # Try with lowest length first
    for i in range(1, ul + 1):

        valid = find_comb_prod(i, part_sum)

        if len(valid) > 0:
            valid.sort()
            # For lowest score, see if valid sublist
            for score, sublist in valid:
                tmp_elems = elems[:]
                for item in sublist:
                    tmp_elems.remove(item)

                for j in range(1, ul + 1):
                    for comb in itertools.combinations(tmp_elems, j):
                        # If one is found, the third is also ok
                        if sum(comb) == part_sum:
                            return score

res1 = part1()
print('Answer #1:', res1)

def part2():
    part_sum = int(sum(elems)/4)

    ul = find_ul(part_sum)

    for i in range(1, ul + 1):

        valid = find_comb_prod(i, part_sum)

        if len(valid) > 0:
            valid.sort()
            for score, sublist in valid:
                tmp_elems = elems[:]
                for item in sublist:
                    tmp_elems.remove(item)

                all_kids = []
                for j in range(1, ul + 1):
                    all_kids += find_comb(tmp_elems, part_sum, j)

                for a in all_kids:
                    for b in all_kids:
                        if len(Counter(a + b).keys()) == len(a + b):
                            for c in all_kids:
                                if len(Counter(a + b + c).keys()) == len(a + b + c):
                                    return score

res2 = part2()
print('Answer #2:', res2)
