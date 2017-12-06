# Answer #1: 11100110111101110
# Answer #2: 10001101010000101

length1 = 272
length2 = 35651584
puzzle_input = '10111100110001111'

def create_data(data):
	orig_data = data[:]
	data_new = []
	for bit in data[::-1]:
		data_new.append((bit+1)%2)
	return orig_data + [0] + data_new

def create_checksum(data):
	checksum = []
	for i in range(0, len(data), 2):
		tmp = data[i:i+2]
		if(tmp[0] == tmp[1]):
			checksum.append(1)
		else:
			checksum.append(0)
	return checksum

def main(seq, length):
	data = []
	for d in seq:
		data.append(int(d))

	while len(data) < length:
		data = create_data(data[:])

	data = data[:length]

	while len(data) % 2 == 0:
		data = create_checksum(data[:]) 

	res = ""
	for bit in data:
		res += str(bit)
	return res

print("Answer #1:", main(puzzle_input, length1))
print("Answer #2:", main(puzzle_input, length2))