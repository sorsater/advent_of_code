# Answer #1: 152851
# Answer #2: 11797310782

cmds = []
with open("input/09", 'r') as f:
	for line in f:
		cmds.append(line.split()[0])

for cmd in cmds:
	length = 0
	rest = cmd

	while len(rest) > 0:
		if(rest[0] == '('):
			idx_x = rest.index('x')
			idx_p = rest.index(')')

			char = int(rest[1:idx_x])
			rep = int(rest[idx_x+1:idx_p])

			seq = rest[idx_p+1:idx_p+char+1]
			rest = rest[idx_p+len(seq):]

			length += rep * len(seq)
		else:
			length += 1
		rest = rest[1:]

	print("Answer #1:", length)

# Recursively splits up the string into a nested list
def split_up(part):
	p = []
	while len(part) > 0:
		if(part[0] == '('):
			idx_x = part.index('x')
			idx_p = part.index(')')

			char = int(part[1:idx_x])
			rep = int(part[idx_x+1:idx_p])

			seq = part[idx_p+1:idx_p+char+1]
			part = part[idx_p+len(seq):]

			# Have one more level of (?x=?)
			if(seq[0] == '('):
				p.append([rep, split_up(seq)])
			else:
				p.append([rep, seq])

		# Just normal character
		else:
			p.append([1, part[0]])
		part = part[1:]
	return p

# Recursively count the parts in the list
def count_part(l):
	# If list, call again
	if isinstance(l, list):
		if(isinstance(l[0], int)):
			return l[0] * count_part(l[1])
		else:
			tmp = 0
			for d in l:
				tmp += count_part(d)
			return tmp
	# Is string, return length
	else:
		return len(l)

# Just one cmd in problem file
for cmd in cmds:
	parts = []
	parts = split_up(cmd)
	length = 0
	for part in parts:
		length += count_part(part)

	print("Answer #2:", length)
