# Answer #1: 665280
# Answer #2: 705600

goal = 29000000

import time
import math

start = time.time()

# Find upper limit
def find_upper():
    house = 1
    while True:
        presents = 0
        for i in range(1, house + 1):
            if house % i == 0:
                presents += i * 10
        if presents >= goal:
            return house
        house = math.ceil(house * 1.2)

limit = find_upper()
print('Upper limit:', limit)

houses_1 = [0] * limit
houses_2 = [0] * limit
for nr in range(1, limit):
    cnt = 0
    for elv in range(nr, limit, nr):
        houses_1[elv] += nr * 10
        if cnt < 50:
            houses_2[elv] += nr * 11
            cnt += 1

result_1 = next(i for i in range(len(houses_1)) if houses_1[i] >= goal)
result_2 = next(i for i in range(len(houses_2)) if houses_2[i] >= goal)

print('Answer #1:', result_1)
print('Answer #2:', result_2)
print('Time: {0:.2f} seconds'.format(time.time()- start))