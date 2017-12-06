# Answer #1: 1834471
# Answer #2: 1420064

import time
from math import floor

tot = 3014387
def part1():
	elves = []
	for j in range(1,tot+1):
		elves.append([j,1])

	while len(elves) > 1:
		new_list = []

		# All elements, except the last one
		for i in range(len(elves)-1):
			if(elves[i][1] > 0):
				elves[i][1] += elves[i+1][1]
				elves[i+1][1] = 0
				new_list.append(elves[i])

		# The last element, wrap around
		if(elves[-1][1] > 0):
			elves[-1][1] += elves[0][1]
			new_list = new_list[1:] + [elves[-1]]

		# Updated list
		elves = new_list[:]

	return elves[0][0]


# Trying to use a linked list, because of time complexity with ordinary lists. Using the idea from adventofcode subreddit
def part2():
	class Elv():
		def __init__(self, nr):
			self.nr = nr
			self.prev = None
			self.next = None

		def delete_elv(self):
			self.prev.next = self.next
			self.next.prev = self.prev

	elvs = [Elv(i) for i in range(tot)]
	# Init pointers
	for i in range(tot):
		elvs[i].next = elvs[(i + 1) % tot]
		elvs[i].prev = elvs[(i - 1) % tot]

	current = elvs[0]
	middle = elvs[floor(tot / 2)]

	# Go through all elves
	for i in range(tot - 1):
		current = current.next

		middle.delete_elv()
		# Update the middle element
		if (tot - i) % 2 == 0:
			middle = middle.next
		else:
			middle = middle.next.next

	return current.nr + 1

start = time.time()
print("Answer #1:", part1())
print("Time:", time.time() - start)
start = time.time()
print()
print("Answer #2:", part2())
print("Time:", time.time() - start)