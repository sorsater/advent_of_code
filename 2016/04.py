# Answer #1: 361724
# Answer #2: 482

rooms = []
with open("input/04", 'r') as f:
	for line in f:
		rooms.append(line.split())

sumSID = 0
for r in rooms:
	r = r[0]

	SID = int(r[-10:-7])
	csum = r[-6:-1]

	code = r[0:-10]
	code = code.replace("-","")
	code = ''.join(sorted(code))

	# Assume correct
	correct = 1
	# For each character in checksum
	for i in range(5):
		topC = 0
		# loop over all characters
		for c in code:
			tmpC = code.count(c)
			if(tmpC > topC):
				topC = tmpC
				value = c
		# Not correct
		if(csum[i] != value):
			correct = 0
			break
		code = code.replace(value,"")

	if(correct):
		sumSID += SID

print("Answer #1:", sumSID)

res = []
for r in rooms:
	r = r[0]

	SID = int(r[-10:-7])
	code = r[0:-3]
	newCode = ""

	for c in code:
		if(c == '-'):
			newCode += " "
		else:
			# Shift the message SID steps
			newCode += chr(((ord(c)+SID-97)%26)+97)
	if("north" in newCode):
		res.append([SID, newCode])

print("Answer #2:", res[0][0])
