# Answer #1: DDRUDLRRRD
# Answer #2: 398

import hashlib

doors_open = "bcdef"
dirs = ["U", "D", "L", "R"]
dirs_cord = [[0,-1],[0,1],[-1,0],[1,0]]

# Create new md5
def get_md5(code):
	return hashlib.md5((code).encode('utf-8')).hexdigest()

# If the new direction is valid in x,y and open door
def valid_move(code, idx, new_x, new_y):
	if not code[idx] in doors_open:
		return False
	tmp_x = new_x + dirs_cord[idx][0]
	tmp_y = new_y + dirs_cord[idx][1]
	if(tmp_x < 0 or tmp_x > 3):
		return False
	if(tmp_y < 0 or tmp_y > 3):
		return False

	return True

# Find all new valid steps
def get_new_code(passcode, new_x, new_y):
	md5 = get_md5(passcode)[:4]
	valid_moves = []
	for i in range(len(dirs)):
		if(valid_move(md5, i, new_x, new_y)):
			valid_moves.append(i)
	return valid_moves

# Find all valid paths.
# The first valid path is the shortest
# The last valid path is the longest
def main(passcode):
	paths = [['', 0, 0]]
	path_length = []
	# While still unfinished paths
	while len(paths):
		new_paths = []
		# For all existing paths
		for path in paths:
			p = path[0]
			x = path[1]
			y = path[2]
			# Reached the end node. Append to the result
			if(x == 3 and y == 3):
				res = p
				path_length.append([p,len(p)])
			else:
				new_directions = get_new_code(passcode + p, x, y)
				# New valid moves
				if(len(new_directions)):
					for direction in new_directions:
						tmp_d = dirs[direction]
						tmp_x = x + dirs_cord[direction][0]
						tmp_y = y + dirs_cord[direction][1]

						new_paths.append([p + tmp_d, tmp_x, tmp_y])
		# Iterate again
		paths = new_paths[:]

	# Return the actual code for the shortest path_length
	# and the length of the longest path
	return [path_length[0][0], path_length[-1][1]]

res = main('hhhxzeay')

print("Answer #1:", res[0])
print("Answer #2:", res[1])
