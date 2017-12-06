# Answer #1: bdfhgeca
# Answer #2: gdfcabeh

import re
import itertools

re0 = r'swap position (\d+) with position (\d+)'
re1 = r'swap letter (\w) with letter (\w)'
re2 = r'reverse positions (\d+) through (\d+)'
re3 = r'rotate left (\d+) steps?'
re4 = r'rotate right (\d+) steps?'
re5 = r'move position (\d+) to position (\d+)'
re6 = r'rotate based on position of letter (\w)'

w = ['a','b','c','d','e','f','g','h']
# Goal for part 2
goal = "fbgdceah"

cmds = []
with open("input/21", 'r') as f:
	for line in f:
		cmds.append(line)

def show_w(w, v):
	res = ""
	for i in w:
		res += i
	if(v):
		print(res)
	if(res == goal):
		return True

def swap_position(w, cmd):
	tmp1 = w[int(cmd[0])]
	tmp2 = w[int(cmd[1])]

	w[int(cmd[0])] = tmp2
	w[int(cmd[1])] = tmp1
	return w

def swap_letter(w, cmd):
	idx1 = w.index(cmd[0])
	idx2 = w.index(cmd[1])

	tmp1 = w[idx1]
	tmp2 = w[idx2]

	w[idx1] = tmp2
	w[idx2] = tmp1
	return w

def reverse(w, cmd):
	tmp1 = int(cmd[0])
	tmp2 = int(cmd[1])

	w[tmp1:tmp2+1] = w[tmp1:tmp2+1][::-1]
	return w

def rotate_left(w, cmd):
	step = int(cmd[0])
	step = step%len(w)

	w = w[step:] + w[:step]
	return w

def rotate_right(w, cmd):
	step = int(cmd[0])
	step = step%len(w)

	w = w[-step:] + w[:-step]
	return w

def rotate_based(w, cmd):
	tmp1 = cmd[0]
	idx = w.index(tmp1)

	step = idx + 1
	if(idx >= 4):
		step += 1

	step = step%len(w)
	w = w[-step:] + w[:-step]

	return w

def move(w, cmd):
	idx1 = int(cmd[0])
	idx2 = int(cmd[1])
	elem = w.pop(idx1)

	w.insert(idx2, elem)
	return w

regFunc = {
	re0: swap_position,
	re1: swap_letter,
	re2: reverse,
	re3: rotate_left,
	re4: rotate_right,
	re5: move,
	re6: rotate_based
}


# Part 1
for cmd in cmds:
	for regex, func in regFunc.items():
		match = re.match(regex, cmd)
		if(match):
			w = func(w, match.groups())
			break

print("Answer #1: ", end="")
show_w(w, True)

# Part 2
for perm in itertools.permutations(w):
	w = list(perm)
	original = w[:]

	for cmd in cmds:
		for regex, func in regFunc.items():
			match = re.match(regex, cmd)
			if(match):
				w = func(w, match.groups())
				break

	if(show_w(w, False)):
		print("Answer #2: ", end="")
		show_w(original, True)
		break
