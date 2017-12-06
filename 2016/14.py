# Answer #1: 18626
# Answer #2: 20092
import hashlib

hashdict = {}
hashdict_2016 = {}

salt = "ngcjuoqr"
correct = []

# Checks if md5 contains 3 following characters
def contains_triple(md5):
	for ch in range(len(md5)-2):
		if(md5[ch] == md5[ch+1] == md5[ch+2]):
			return md5[ch]
	return ''

# Checks if md5 contains 5 following characters
def contains_quintuple(md5, char):
	for ch in range(len(md5)-4):
		# Faster than a for loop
		if(char == md5[ch] == md5[ch+1] == md5[ch+2] == md5[ch+3] == md5[ch+4]):
			return True
	return False

# Read/set dictionary with key, part1
def get_set_hash(key):
	if not key in hashdict:
		md5 = hashlib.md5((key).encode('utf-8')).hexdigest()
		hashdict[key] = md5
	return hashdict[key]

# Read/set dictionary with key, part2
def get_set_hash_2016(key):
	if not key in hashdict_2016:
		md5 = hashlib.md5((key).encode('utf-8')).hexdigest()
		for i in range(2016):
			md5 = hashlib.md5((md5).encode('utf-8')).hexdigest()
		hashdict_2016[key] = md5
	return hashdict_2016[key]

# Check if the given idx is valid
def find_values(md5, idx, normal):
	char = contains_triple(md5)
	if(char != ''):
		for i in range(1, 1001):
			key = salt + str(i + idx)
			if(normal):
				md5 = get_set_hash(key)
			else:
				md5 = get_set_hash_2016(key)
			if(contains_quintuple(md5, char)):
				correct.append(str(idx))
				print(len(correct), end="\r")
				if(len(correct) == 64):
					return True
				break
	return False

def main(normal):
	global correct
	correct = []
	idx = 0
	while 1:
		key = salt + str(idx)
		if(normal):
			md5 = get_set_hash(key)
		else:
			md5 = get_set_hash_2016(key)
		if(find_values(md5, idx, normal)):
			break
		idx += 1

main(True)
print("Answer #1:", correct[-1])

main(False)
print("Answer #2:", correct[-1])
