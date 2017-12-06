# Answer #1: 86
# Answer #2: 127

width, height = 40,45
fav_number = 1364
start_x, start_y = 1, 1

max_steps = 50

grid = []
visited = []

def wall(x, y):
	return "{0:b}".format(x*x + 3*x + 2*x*y + y + y*y + fav_number).count('1') % 2 != 0
	
def create_grid():
	global grid
	grid = []
	for y in range(height):
		tmp = []
		for x in range(width):
			if(wall(x, y)):
				tmp.append('#')
			else:
				tmp.append('.')
		grid.append(tmp)
	
def show_grid():
	idx = "  "
	for x in range(len(grid[0])):
		if(x < 10):
			idx += " "
		idx += str(x)
	print(idx)
	for i, g in enumerate(grid):
		line = str(i) + " "
		if(i < 10):
			line += " "
		for e in g:
			line += e + " "
		print(line)

def show_visited():
	for d in visited:
		print(d)

def check_neighbour(x, y, i, j):
	if(x+i < 0 or x+i >= width):
		return False
	if(y+j < 0 or y+j >= height):
		return False

	if(visited[y+j][x+i] != 9):
		return False

	if(grid[y+j][x+i] == '#'):
		return False

	if(i == 1 and j == 0):
		d = 3
	elif(i == -1 and j == 0):
		d = 1
	elif(i == 0 and j == 1):
		d = 0
	elif(i == 0 and j == -1):
		d = 2

	visited[y+j][x+i] = d
	
	return True
	
def bfs(goal_x, goal_y, brk):

	#return False
	global visited
	visited = []
	for y in range(height):
		tmp = []
		for x in range(width):
			tmp.append(9)
		visited.append(tmp)

	q = [[start_x, start_y]]

	depth = 0
	while len(q) > 0:
		curr = q.pop(0)
		x = curr[0]
		y = curr[1]
		
		if(x == goal_x and y == goal_y):
			return True

		if(check_neighbour(x,y,0,1)):
			q.append([x,y+1])
		if(check_neighbour(x,y,0,-1)):
			q.append([x,y-1])
		if(check_neighbour(x,y,1,0)):
			q.append([x+1,y])
		if(check_neighbour(x,y,-1,0)):
			q.append([x-1,y])
		depth += 1
		
	return False

def backtrack(goal_x, goal_y):
	x = goal_x
	y = goal_y
	count = 0
	while not(x == start_x and y == start_y):
		d = visited[y][x]

		if(d == 0):
			y -= 1
		elif(d == 1):
			x += 1
		elif(d == 2):
			y += 1
		elif(d == 3):
			x -= 1

		count += 1
	return count

def find_path(goal_x, goal_y, brk):
	if(bfs(goal_x, goal_y, brk)):
		return backtrack(goal_x, goal_y)
	else:
		return -1

# Part 1
create_grid()
goal_x, goal_y = 31, 39
res = find_path(goal_x, goal_y, False)
print("Answer #1:", res)

create_grid()

# Part 2
steps = 0
for x in range(width):
	for y in range(height):
		# No need to check further away
		if(x + y < max_steps):
			create_grid()
			if(grid[y][x] == '.'):
				c = find_path(x, y, True)
				if(c > -1 and c <= max_steps):
					steps += 1

print("Answer #2:", steps)
