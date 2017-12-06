# Answer #1: hxbxxyzz
# Answer #2: hxcaabcc

pw = 'hxbxwxba'
invalid = [chr(inv) for inv in [105, 108, 111]]

def is_valid(pw):
	req = set()
	straigt = False
	for i, char in enumerate(pw):
		if char in invalid:
			return False
		if i >= 1:
			if pw[i] == pw[i-1]:
				req.add(pw[i])
		if i >= 2:
			if pw[i] == pw[i-1] + 1 == pw[i-2] + 2:
				straigt = True

	return len(req) >= 2 and straigt

def increment(pw):
	next_pw = []

	# If invalid character, increment all
	for i, val in enumerate(pw):
		if val in invalid:
			next_pw.append(val + 1)
			for j in range(i, len(pw) - 1):
				next_pw.append(ord('a'))
			return next_pw
		else:
			next_pw.append(val)

	# Increment x->a, eg. xxzzz to xyaaa
	for i in range(len(next_pw) - 1, -1, -1):
		if next_pw[i] != ord('z'):
			next_pw[i] += 1
			break
		else:
			next_pw[i] = ord('a')

	return next_pw

def pretty(pw):
	return ''.join([chr(v) for v in pw])

def find_next(pw):
	while not is_valid(pw):
		pw = increment(pw)
	return pw

pw = [ord(c) for c in pw]

part1 = find_next(pw)
print("Answer #1:", pretty(part1))

pw = increment(part1)
part2 = find_next(pw)
print("Answer #2:", pretty(part2))

