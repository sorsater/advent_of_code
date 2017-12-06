# Answer #1: 1939
# Answer #2: 19999535

# Read data
curr_row = []
with open("input/18", "r") as f:
	[[curr_row.append(tile == '.') for tile in line.split()[0]] for line in f]

# The only tiles that matters are the one to the right and to the left
def main(curr_row, nr_rows):
	row_length = len(curr_row)
	nr_safe = sum(curr_row)

	for i in range(nr_rows-1):
		new_row = [curr_row[1]]

		# All elements in the middle. Need to be the same to be safe
		[new_row.append(curr_row[i-1] == curr_row[i+1]) for i in range(1, row_length - 1)]

		new_row.append(curr_row[-2])

		nr_safe += sum(new_row)

		curr_row = new_row[:]
	return nr_safe

print("Answer #1:", main(curr_row, 40))
print("Answer #2:", main(curr_row, 400000))