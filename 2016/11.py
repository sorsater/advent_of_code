# Answer #1: 33
# Answer #2: 57

import re
import time
from itertools import combinations
from copy import deepcopy
from queue import Queue

start = time.time()
re0 = r'a ([A-z -]+)'

with open('input/11', 'r') as f:
	floors_raw = [re.findall(re0, line.replace('and', ',')) for line in f]

floors = []
elems = []
for floor in floors_raw:
	new_floor = []
	for item in floor:
		elem = item.split()
		new_floor.append(elem[0][0].upper() + elem[0][1] + elem[1][0].upper())
	floors.append(new_floor)
	elems += new_floor

elems.sort()

# Used for debugging
def show_floors(board, elev):
	for i, f in enumerate(board[::-1]):
		res = 'F' + str(4-i)
		if(3-i == elev):
			res += ' E '
		else:
			res += ' . '
		for el in elems:
			if el in f:
				res += ' ' + el + ' '
			else:
				res += '  .  '
		print(res)

# Check if the current configuration is valid
def is_move_valid(floor, elems, add_together=True):
	if add_together:
		config = floor + elems
	else:
		config = list(set(floor) - set(elems))

	for item in config:
		if item[-1] == 'G':
			break
	else:
		return True

	# Need to check M:s
	for item in config:
		if item[-1] == 'G':
			continue
		if not item[:-1] + 'G' in config:
			return False
	else:
		return True

# Return all valid moves from the configuration
def valid_moves(path, elevator):
	moves = sum([[x for x in combinations(path[elevator], i)] for i in [1, 2]], [])

	# Test combinations with the elements
	valid_moves = []
	for move in moves:
		move = list(move)

		if not is_move_valid(path[elevator], move, add_together=False):
			continue

		# Test to move up
		if elevator < 3:
			if is_move_valid(path[elevator+1], move):
				valid_moves.append([1, move])

		# Test to move down
		if elevator > 0:
			if is_move_valid(path[elevator-1], move):
				valid_moves.append([-1, move])
	return valid_moves

def config_to_string(floors, elevator):
	string = str(elevator)
	for i, floor in enumerate(floors):
		types = [item[-1] for item in floor]
		types.sort()
		string += str(i) + ''.join(types)

	return string

def main():
	#show_floors(floors_cpy, 0)

	q = Queue()
	q.put([0, floors, 0])
	seen_states = set()

	while not q.empty():
		elevator, floor, moves = q.get()

		new_paths = valid_moves(floor, elevator)

		for up_down, items in new_paths:
			# +1 for Up, -1 for Down
			new_elevator = elevator + up_down

			new_floors = deepcopy(floor)
			for item in items:
				new_floors[elevator].remove(item)
				new_floors[new_elevator].append(item)

			config = config_to_string(new_floors, new_elevator)

			# Ignore already checked states
			if config not in seen_states:
				# All elements on highest floor
				if len(new_floors[3]) == len(elems):
					return moves + 1
				q.put([new_elevator, new_floors, moves + 1])
				seen_states.add(config)

print('Answer #1:', main())
floors[0] += ['ElG', 'ElM', 'DiG', 'DiM']
elems += ['ElG', 'ElM', 'DiG', 'DiM']
print('Answer #2:', main())
#print('Time: {0:.3f}'.format(time.time() - start))
