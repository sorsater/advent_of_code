# Answer #1: 105
# Answer #2: 258

codes = []
with open("input/07", 'r') as f:
	for line in f:
		codes.append(line.split()[0])

count = 0
for code in codes:
	outside = True
	correct = 0
	line = ""
	for i, c in enumerate(code):
		line += c
		if(len(line) > 4):
			line = line[1:]
		if(len(line) == 4):
			if(line == line[::-1] and line[0] != line[1]):
				if(outside):
					correct = 1
				else:
					correct = -1
					break
		if(c == "["):
			outside = False
		if(c == "]"):
			outside = True
	if(correct == 1):
		count += 1

print("Answer #1:", count)

count = 0
for code in codes:
	correct = False
	outside = True
	line = ""
	invalid = "[]"
	supernet = []
	hypernet = []
	for i, c in enumerate(code):
		line += c
		if(len(line) > 3):
			line = line[1:]
		if(len(line) == 3):
			if(line == line[::-1] and line[0] != line[1] and line[1] not in invalid):
				if(outside):
					supernet.append(line)
				else:
					hypernet.append(line)
		if(c == "["):
			outside = False
		if(c == "]"):
			outside = True

	for hyper in hypernet:
		tmp = hyper[1] + hyper[0] + hyper[1]
		if(tmp in supernet):
			correct = True

	if(correct):
		count += 1
print("Answer #2:", count)

