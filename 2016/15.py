# Answer #1: 122318
# Answer #2: 3208583

# The last disc is added to the input

import re

re0 = r'Disc #(\d+) has (\d+) positions; at time=(\d+), it is at position (\d+).'
eq = []

with open("input/15", "r") as f:
	for line in f:
		match = re.match(re0, line.splitlines()[0])
		if(match):
			di = match.groups()
			eq.append([int(di[0]) + int(di[3]), int(di[1])])

def find_time(eq):
	cnt = 0
	while True:
		for e in eq:
			if((cnt + e[0]) % e[1] != 0):
				break
		else:
			break
		cnt += 1
	return cnt

# Part one, ignore the last disc
print("Answer #1:", find_time(eq[:-1]))
print("Answer #2:", find_time(eq))


