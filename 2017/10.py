# Answer #1: 48705
# Answer #2: 1c46642b6f2bc21db2a2149d0aeeae5d

len_list = 256

with open('input/10') as f:
    raw = f.read()

lengths_1 = [int(hej) for hej in raw.split(',')]
lengths_2 = [ord(char) for char in raw] + [17, 31, 73, 47, 23]

string = list(range(len_list))

# Takes list of int (string) and performs leng
def hash_me(string, lengths, iter):
    cur_pos, skip = 0, 0
    for _ in range(iter):
        for lenght in lengths:
            start_idx = (cur_pos) % len_list
            end_idx = (cur_pos + lenght) % len_list

            # No wrap around
            if end_idx >= start_idx:
                sub_string = string[start_idx:end_idx]
                sub_string = sub_string[::-1]
                string[start_idx:end_idx] = sub_string

            # Wrap around
            else:
                part1 = string[start_idx:]
                part2 = string[:end_idx]
                
                sub_string = (part1 + part2)[::-1]

                string[start_idx:] = sub_string[:len(part1)]
                string[:end_idx] = sub_string[len(part1):]

            cur_pos += lenght + skip
            skip += 1
    return string

seq1 = hash_me(string[:], lengths_1, 1)
print('Answer #1: {}'.format(seq1[0]* seq1[1]))

sparse_hash = hash_me(string[:], lengths_2, 64)

# For each block of 16 numbers
dense_hash = []
for i in range(0, len(sparse_hash), 16):
    res = 0
    for num in sparse_hash[i:i+16]:
        res ^= num
    dense_hash.append(res)

res = ''
for dense in dense_hash:
    res += format(dense, '02x')

print('Answer #2: {}'.format(res))

