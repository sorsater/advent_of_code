# Answer #1: 2414bc77
# Answer #2: 437e60fc

import hashlib
import time

code = "wtnhxymk"
pw = ""
c = 0
for i in range(8):
	while 1:
		tmp = hashlib.md5((code + str(c)).encode('utf-8')).hexdigest()
		c += 1
		if(tmp[0:5] == "00000"):
			pw += tmp[5]
			break

print("Answer #1:",pw)

pw = ['-','-','-','-','-','-','-','-']
c = 0

valid = "01234567"
for i in range(8):
	while 1:
		tmp = hashlib.md5((code + str(c)).encode('utf-8')).hexdigest()
		c += 1
		if(tmp[0:5] == "00000"):
			if(tmp[5] in valid):
				idx = int(tmp[5])
				if(pw[idx] == '-'):
					pw[idx] = tmp[6]
					break

r = ""
for c in pw:
	r += c

print("Answer #2:",r)
